#!/usr/bin/env python3

import argparse
import time
import sys
import os

from datetime import datetime, timedelta, timezone

class Netdev:
    def __init__(self, name, params = []):
        self.name = name
        self.params = params
        self.stat_dir = "/sys/class/net/{}/statistics".format(self.name)
        if not os.path.exists(self.stat_dir):
            raise AttributeError("{} does not exist for {}".format(self.stat_dir,
                                                                   self.name))
        if len(params) == 0:
            self.params = os.listdir(self.stat_dir)

        self.d = {} # key is param, value is [prev, next]
        for param in self.params:
            self.d[param] = [0, 0]

        self.last = datetime.now()
        self.curr = datetime.now()

    def capture(self):
        t = datetime.now()
        for param in self.params:
            with open(self.stat_dir + "/" + param, "r") as f:
                v = int(f.read().strip())
                self.d[param].append(v)
                self.d[param].pop(0)
        self.last = self.curr
        self.curr = t

    def calculate(self):
        d = {}
        elapsed = (self.curr - self.last).total_seconds()
        for param in self.params:
            prev, curr = self.d[param]
            d[param] = round((curr - prev) / elapsed, 2)
        return d

    def json(self):
        d = self.calculate()
        return {
            "name": self.name,
            "timestamp": self.curr.replace(tzinfo = timezone.utc).timestamp(),
            **d
        }
            
    def printl(self):
        d = self.calculate()
        items = sorted(d.items(), key = lambda x: x[0])
        o = " ".join(map(lambda x: "{}:{}".format(x[0], x[1]), items))
        return self.name + " " + o
        

def main():

    prog = "pnstat"
    desc = "(Simply) print netdev statistics (per second)"

    parser = argparse.ArgumentParser(prog = prog, description = desc)
    parser.add_argument("-n", "--netdev", action = "append", default = [],
                        help = "target netdev(s) (default all netdevs)")
    parser.add_argument("-i", "--interval", type = float, default = 1.0,
                        help = "interval")
    parser.add_argument("-c", "--count", type = int, default = -1,
                        help = "count (default infinite)")
    parser.add_argument("-o", "--output", type = argparse.FileType("w"),
                        default = sys.stdout,
                        help = "output file (default stdout)")
    parser.add_argument("-j", "--json", action = "store_true",
                        help = "output as jsonl")
    parser.add_argument("-k", "--keys",
                        choices = ["default", "witherrors", "all"],
                        default = "default",
                        help = "keys to be gathered")
    args = parser.parse_args()

    if args.keys == "default":
        params = [
            "rx_bytes", "rx_packets", "tx_bytes", "tx_packets"
        ]
    elif args.keys == "witherrors":
        params = [
            "rx_bytes", "rx_packets", "rx_errors", "rx_dropped",
            "tx_bytes", "tx_packets", "tx_errors", "tx_dropped",
        ]
    elif args.keys == "all":
        params = []

    if len(args.netdev) == 0:
        args.netdev = os.listdir("/sys/class/net") # all netdevs

    netdevs = [Netdev(x, params = params) for x in args.netdev]

    nextat = datetime.now() + timedelta(seconds=args.interval)
    for netdev in netdevs:
        netdev.capture()

    while True:
        time.sleep((nextat - datetime.now()).total_seconds())
        nextat = datetime.now() + timedelta(seconds=args.interval)
        for netdev in netdevs:
            netdev.capture()
            
        for netdev in netdevs:
            if args.json:
                o = netdev.json()
            else:
                o = netdev.printl()
            print(o, file = args.output)
            args.output.flush()

        if args.count > 0:
            args.count -= 1
            if args.count == 0:
                break

if __name__ == "__main__":
    main()
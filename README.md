
# pnstat

`pnstat` prints netdev statistics. `pnstat` usage is simple and it is
designed for (my) network-related experiments.


```console
$ ./pnstat -h
usage: pnstat [-h] [-n NETDEV] [-i INTERVAL] [-c COUNT] [-o OUTPUT] [-j]
              [-k {default,witherrors,all}] [--per-second]

(Simply) print netdev statistics

options:
  -h, --help            show this help message and exit
  -n NETDEV, --netdev NETDEV
                        target netdev(s) (default all netdevs)
  -i INTERVAL, --interval INTERVAL
                        interval
  -c COUNT, --count COUNT
                        count (default infinite)
  -o OUTPUT, --output OUTPUT
                        output file (default stdout)
  -j, --json            output as jsonl
  -k {default,witherrors,all}, --keys {default,witherrors,all}
                        keys to be gathered
  --per-second          print values in per-second basis
```

## How to use

```console
git clone https://github.com/upa/pnstat
cd pnstat
./pnstat
```


```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0  --per-second
enp6s0 rx_bytes:1006.71 rx_packets:15.98 tx_bytes:699.1 tx_packets:2.0
enp1s0f0np0 rx_bytes:0.0 rx_packets:0.0 tx_bytes:0.0 tx_packets:0.0
enp6s0 rx_bytes:443.42 rx_packets:6.99 tx_bytes:1312.28 tx_packets:3.0
enp1s0f0np0 rx_bytes:0.0 rx_packets:0.0 tx_bytes:0.0 tx_packets:0.0
^C⏎
```

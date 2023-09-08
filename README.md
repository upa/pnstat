
# pnstat

`pnstat` prints netdev statistics (in per-second basis). `pnstat`
usage is simple and it is designed for (my) network-related
experiments.


```console
$ ./pnstat -h
usage: pnstat [-h] [-n NETDEV] [-i INTERVAL] [-c COUNT] [-o OUTPUT] [-j]
              [-k {default,witherrors,all}]

(Simply) print netdev statistics (per second)

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
```

## How to use

```console
git clone https://github.com/upa/pnstat
cd pnstat
./pnstat
```

- Simple usage:

```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0
enp6s0 rx_bytes:1006.71 rx_packets:15.98 tx_bytes:699.1 tx_packets:2.0
enp1s0f0np0 rx_bytes:0.0 rx_packets:0.0 tx_bytes:0.0 tx_packets:0.0
enp6s0 rx_bytes:443.42 rx_packets:6.99 tx_bytes:1312.28 tx_packets:3.0
enp1s0f0np0 rx_bytes:0.0 rx_packets:0.0 tx_bytes:0.0 tx_packets:0.0
^C⏎
```

- With JSONL output (including timestamp):

```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0 -j
{'name': 'enp6s0', 'timestamp': 1694188485.732952, 'rx_bytes': 335.57, 'rx_packets': 3.99, 'tx_bytes': 816.96, 'tx_packets': 3.0}
{'name': 'enp1s0f0np0', 'timestamp': 1694188485.733095, 'rx_bytes': 0.0, 'rx_packets': 0.0, 'tx_bytes': 0.0, 'tx_packets': 0.0}
{'name': 'enp6s0', 'timestamp': 1694188486.734213, 'rx_bytes': 263.67, 'rx_packets': 3.99, 'tx_bytes': 1432.19, 'tx_packets': 3.0}
{'name': 'enp1s0f0np0', 'timestamp': 1694188486.734362, 'rx_bytes': 0.0, 'rx_packets': 0.0, 'tx_bytes': 0.0, 'tx_packets': 0.0}
{'name': 'enp6s0', 'timestamp': 1694188487.73565, 'rx_bytes': 413.41, 'rx_packets': 2.0, 'tx_bytes': 365.47, 'tx_packets': 1.0}
{'name': 'enp1s0f0np0', 'timestamp': 1694188487.735799, 'rx_bytes': 0.0, 'rx_packets': 0.0, 'tx_bytes': 0.0, 'tx_packets': 0.0}
^C⏎
```

- With error/drop counters:

```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0 --keys witherrors
enp6s0 rx_bytes:1917.59 rx_dropped:1.0 rx_errors:0.0 rx_packets:23.97 tx_bytes:1132.57 tx_dropped:0.0 tx_errors:0.0 tx_packets:4.99
enp1s0f0np0 rx_bytes:0.0 rx_dropped:0.0 rx_errors:0.0 rx_packets:0.0 tx_bytes:0.0 tx_dropped:0.0 tx_errors:0.0 tx_packets:0.0
enp6s0 rx_bytes:2347.08 rx_dropped:1.0 rx_errors:0.0 rx_packets:37.95 tx_bytes:992.76 tx_dropped:0.0 tx_errors:0.0 tx_packets:3.0
enp1s0f0np0 rx_bytes:0.0 rx_dropped:0.0 rx_errors:0.0 rx_packets:0.0 tx_bytes:0.0 tx_dropped:0.0 tx_errors:0.0 tx_packets:0.0
enp6s0 rx_bytes:2223.24 rx_dropped:1.0 rx_errors:0.0 rx_packets:36.95 tx_bytes:357.56 tx_dropped:0.0 tx_errors:0.0 tx_packets:1.0
enp1s0f0np0 rx_bytes:0.0 rx_dropped:0.0 rx_errors:0.0 rx_packets:0.0 tx_bytes:0.0 tx_dropped:0.0 tx_errors:0.0 tx_packets:0.0
^C⏎
```

- Full items:

```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0 --keys all
enp6s0 collisions:0.0 multicast:1.0 rx_bytes:1096.62 rx_compressed:0.0 rx_crc_errors:0.0 rx_dropped:1.0 rx_errors:0.0 rx_fifo_errors:0.0 rx_frame_errors:0.0 rx_length_errors:0.0 rx_missed_errors:0.0 rx_nohandler:0.0 rx_over_errors:0.0 rx_packets:14.98 tx_aborted_errors:0.0 tx_bytes:1424.21 tx_carrier_errors:0.0 tx_compressed:0.0 tx_dropped:0.0 tx_errors:0.0 tx_fifo_errors:0.0 tx_heartbeat_errors:0.0 tx_packets:6.99 tx_window_errors:0.0
enp1s0f0np0 collisions:0.0 multicast:0.0 rx_bytes:0.0 rx_compressed:0.0 rx_crc_errors:0.0 rx_dropped:0.0 rx_errors:0.0 rx_fifo_errors:0.0 rx_frame_errors:0.0 rx_length_errors:0.0 rx_missed_errors:0.0 rx_nohandler:0.0 rx_over_errors:0.0 rx_packets:0.0 tx_aborted_errors:0.0 tx_bytes:0.0 tx_carrier_errors:0.0 tx_compressed:0.0 tx_dropped:0.0 tx_errors:0.0 tx_fifo_errors:0.0 tx_heartbeat_errors:0.0 tx_packets:0.0 tx_window_errors:0.0
enp6s0 collisions:0.0 multicast:2.0 rx_bytes:365.55 rx_compressed:0.0 rx_crc_errors:0.0 rx_dropped:1.0 rx_errors:0.0 rx_fifo_errors:0.0 rx_frame_errors:0.0 rx_length_errors:0.0 rx_missed_errors:0.0 rx_nohandler:0.0 rx_over_errors:0.0 rx_packets:5.99 tx_aborted_errors:0.0 tx_bytes:1514.13 tx_carrier_errors:0.0 tx_compressed:0.0 tx_dropped:0.0 tx_errors:0.0 tx_fifo_errors:0.0 tx_heartbeat_errors:0.0 tx_packets:2.0 tx_window_errors:0.0
enp1s0f0np0 collisions:0.0 multicast:0.0 rx_bytes:0.0 rx_compressed:0.0 rx_crc_errors:0.0 rx_dropped:0.0 rx_errors:0.0 rx_fifo_errors:0.0 rx_frame_errors:0.0 rx_length_errors:0.0 rx_missed_errors:0.0 rx_nohandler:0.0 rx_over_errors:0.0 rx_packets:0.0 tx_aborted_errors:0.0 tx_bytes:0.0 tx_carrier_errors:0.0 tx_compressed:0.0 tx_dropped:0.0 tx_errors:0.0 tx_fifo_errors:0.0 tx_heartbeat_errors:0.0 tx_packets:0.0 tx_window_errors:0.0
^C⏎
```

- Full itmes in JSONL:

```console
$ ./pnstat -n enp6s0 -n enp1s0f0np0 --keys all -j
{'name': 'enp6s0', 'timestamp': 1694188581.555415, 'tx_errors': 0.0, 'rx_length_errors': 0.0, 'rx_packets': 7.99, 'tx_carrier_errors': 0.0, 'tx_dropped': 0.0, 'rx_missed_errors': 0.0, 'rx_over_errors': 0.0, 'tx_aborted_errors': 0.0, 'rx_crc_errors': 0.0, 'rx_frame_errors': 0.0, 'rx_nohandler': 0.0, 'tx_fifo_errors': 0.0, 'multicast': 1.0, 'tx_packets': 4.99, 'tx_window_errors': 0.0, 'rx_bytes': 629.2, 'collisions': 0.0, 'rx_dropped': 1.0, 'tx_bytes': 1140.55, 'tx_heartbeat_errors': 0.0, 'rx_fifo_errors': 0.0, 'rx_errors': 0.0, 'tx_compressed': 0.0, 'rx_compressed': 0.0}
{'name': 'enp1s0f0np0', 'timestamp': 1694188581.555799, 'tx_errors': 0.0, 'rx_length_errors': 0.0, 'rx_packets': 0.0, 'tx_carrier_errors': 0.0, 'tx_dropped': 0.0, 'rx_missed_errors': 0.0, 'rx_over_errors': 0.0, 'tx_aborted_errors': 0.0, 'rx_crc_errors': 0.0, 'rx_frame_errors': 0.0, 'rx_nohandler': 0.0, 'tx_fifo_errors': 0.0, 'multicast': 0.0, 'tx_packets': 0.0, 'tx_window_errors': 0.0, 'rx_bytes': 0.0, 'collisions': 0.0, 'rx_dropped': 0.0, 'tx_bytes': 0.0, 'tx_heartbeat_errors': 0.0, 'rx_fifo_errors': 0.0, 'rx_errors': 0.0, 'tx_compressed': 0.0, 'rx_compressed': 0.0}
```

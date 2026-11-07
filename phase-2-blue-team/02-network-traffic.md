# Blue Team: Network Traffic Analysis

## The TCP 3-Way Handshake
Learned how connections are established: SYN -> SYN-ACK -> ACK. Attackers abuse this using SYN Flood attacks (Denial of Service).

## Wireshark Filters
- `dns`: Shows DNS queries (finding IP addresses).
- `tcp.flags.syn == 1 and tcp.flags.ack == 0`: Shows SYN packets to detect potential SYN flood attacks.

## Tcpdump (Command Line)
Used `sudo tcpdump -i eth0 -c 5` to capture 5 packets on the network interface.

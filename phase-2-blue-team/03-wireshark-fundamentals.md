# Blue Team: Wireshark Fundamentals

## The 3 Panes
1. Packet List (Overview)
2. Packet Details (Layers: Ethernet, IP, TCP, Data)
3. Packet Bytes (Raw Hex/ASCII - Good for finding hidden malware strings)

## Essential Filters
- `tcp.flags.syn == 1 and tcp.flags.ack == 0`: Shows connection attempts (SYN packets). Useful for detecting SYN Floods.
- `dns`: Shows DNS lookups. Useful for spotting Command & Control (C2) domains.
- `http.request`: Shows unencrypted web requests.
- `http contains "password"`: Finds plaintext passwords in unencrypted traffic.

## Detecting Attacks
- **Port Scan:** One Source IP sending SYN packets to multiple ports on one target.
- **Brute Force:** Repeated connection attempts to a single port (like SSH port 22).

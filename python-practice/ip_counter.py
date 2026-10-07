ip_list = ["192.168.1.5", "10.0.0.3", "192.168.1.5", "172.16.0.8", "10.0.0.3", "192.168.1.5"]

ip_counts = {}

for ip in ip_list:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

for ip, count in ip_counts.items():
    print(f"{ip} -> {count} attempts")

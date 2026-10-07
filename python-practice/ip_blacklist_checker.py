# Step 1: Create a set of blacklisted IPs
blacklist = {"192.168.1.5", "10.0.0.3", "172.16.0.8"}

# Step 2: Create a list of incoming IPs
incoming = ["192.168.1.5", "8.8.8.8", "10.0.0.3", "1.1.1.1", "192.168.1.5"]

# Step 3: Loop through the incoming IPs
for ip in incoming:
    # Step 4: If the IP is in the blacklist, print BLOCKED
    if ip in blacklist:
        print(f"[BLOCKED] {ip}")
    # Step 5: If not, print ALLOWED
    else:
        print(f"[ALLOWED] {ip}")

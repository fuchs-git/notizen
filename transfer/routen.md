```bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Do the Forwarding
iptables -A FORWARD -i tun0 -eth0 -m state RELATED, ESTABLISH -j ACCEPT
iptables -A FORWARD -i eth0 -o tun0 -j ACCEPT

# ADD nat
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o tun0 -j MASQUERADE
```

```bash
# on Windows
route add 10.10.10.0 mask 255.255.255.0 <router ip>
```



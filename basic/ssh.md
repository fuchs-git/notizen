# ssh
## Session Port Forwarding
ssh> mit `CTRL+~ + C`

```bash
pi@raspberrypi:~ $ 
ssh> -L 8000:127.0.0.1:8000
Forwarding port.
```

## Tunneling + Blocken von remote commands
```bash
ssh -i intense -N -L5001:localhost:5001 Debian-snmp@10.10.10.195
```
- -i <keyfile>
- -N "Do not execute a remote command. This is useful for just forwarding ports (protocol version 2 only)."


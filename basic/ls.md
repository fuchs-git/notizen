# ls
## Timestamp anzeigen
```bash
┌──(fuchs㉿kali)-[~/notes]
└─$ ls -lt --time-style=full-iso
insgesamt 60
drwxr-xr-x 7 fuchs fuchs 4096 2021-03-22 10:11:22.331774069 +0100 Notes
drwxr-xr-x 2 fuchs fuchs 4096 2021-03-21 21:01:16.398228058 +0100 web
-rwxrwxrwx 1 fuchs fuchs  430 2021-03-08 14:54:35.097316486 +0100 better_shell
drwxr-xr-x 2 fuchs fuchs 4096 2021-03-05 18:48:54.564557533 +0100 rev
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.913560240 +0100 windows
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.909560240 +0100 tools
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.869560239 +0100 other
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.853560238 +0100 hidden
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.825560237 +0100 burp
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.825560237 +0100 dns
-rwxrwxrwx 1 fuchs fuchs  671 2020-01-28 02:59:00.518529000 +0100 network_data-transfer
-rwxrwxrwx 1 fuchs fuchs  214 2020-01-28 02:59:00.518529000 +0100 priv_checker
-rwxrwxrwx 1 fuchs fuchs  620 2020-01-23 02:15:08.918840000 +0100 linux_commandos
-rwxrwxrwx 1 fuchs fuchs  283 2020-01-23 02:15:08.918840000 +0100 nmap
-rwxrwxrwx 1 fuchs fuchs  132 2019-07-13 11:47:49.899921000 +0200 suid_owners
```
(bei hinteren Nullen wurden die Daten kopiert)

## Nur erzeugte Daten anzeigen
```bash
┌──(fuchs㉿kali)-[~/notes]
└─$ ls -lt --time-style=full-iso | grep -v 000
insgesamt 60
drwxr-xr-x 7 fuchs fuchs 4096 2021-03-22 10:11:22.331774069 +0100 Notes
drwxr-xr-x 2 fuchs fuchs 4096 2021-03-21 21:01:16.398228058 +0100 web
-rwxrwxrwx 1 fuchs fuchs  430 2021-03-08 14:54:35.097316486 +0100 better_shell
drwxr-xr-x 2 fuchs fuchs 4096 2021-03-05 18:48:54.564557533 +0100 rev
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.913560240 +0100 windows
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.909560240 +0100 tools
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.869560239 +0100 other
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.853560238 +0100 hidden
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.825560237 +0100 burp
drwxr-xr-x 2 fuchs fuchs 4096 2021-02-12 18:15:06.825560237 +0100 dns
```

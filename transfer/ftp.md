# Methoden zum verbinden
## SSL Certifikat akzeptieren
```bash
$ lftp
lftp :~> set ftp:ssl-force true
lftp :~> set ssl:verify-certificate no
lftp :~> connect 10.10.10.208
lftp 10.10.10.208:~> login fuchs
Passwort: 
lftp fuchs@10.10.10.208:~> 
```
 
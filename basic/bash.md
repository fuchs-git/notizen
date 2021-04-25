# bash
## Schleifen
```bash
└─$ for((i=0;i<5;i++)); do curl 206.189.121.131:31647/index.php?id=$i; echo "";done
User does not exist
superadmin
test
admin
administrator
```

```bash
└─$ for i in {0..5}; do curl 206.189.121.131:31647/index.php?id=$i; echo "";doneUser does not exist
User does not exist
superadmin
test
admin
administrator
```

## PATH
```bash
┌──(fuchs㉿kali)-[~/htb/bucket]
└─$ export PATH=$(pwd):$PATH
┌──(fuchs㉿kali)-[~/htb/bucket]
└─$ echo $PATH
/home/fuchs/htb/bucket:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/fuchs/bin
```


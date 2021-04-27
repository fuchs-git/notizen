# BetterShell
```bash
python -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
/usr/local/bin/python -c 'import pty; pty.spawn("/bin/sh")'
```
In den Hintergrund mit "Strg+Z"
```bash
stty -a
stty raw -echo
stty rows 49 (siehe -a)
stty cols 185 (siehe -a)
```
In den Vordergrung mit "fg"

Funktionen wie Strg+l importieren
```bash
export TERM=xterm
```

## Fenstergröße anpassen
```bash
──(fuchs㉿kali)-[~]
└─$ stty -a
speed 38400 baud; rows 25; columns 80; line = 0;
...[snip]...
```
Setzen der Werte:
```bash
stty rows 25 columns 80
```

## Switch User
```bash
cat /etc/passwd | grep user
"user":/usr/bin/lshell
cat /etc/shells
su -s /bin/bash "user"
```
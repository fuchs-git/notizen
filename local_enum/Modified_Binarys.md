# Finden von modifizierten Binarys 
Anhand des Timestamps ist es möglich manipulierte Binarys zu finden.

```bash
──(fuchs㉿kali)-[~]
└─$ $PATH
bash: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/fuchs/bin: Datei oder Verzeichnis nicht gefunden
┌──(fuchs㉿kali)-[~]
└─$ for i in /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin /usr/local/games /usr/games /home/fuchs/bin; do ls -la --time-style=full $i | grep -v '00000\|->'; done
...[snip]...
drwxr-xr-x  2 root  root       131072 2021-04-02 08:58:40.141412294 +0200 .
drwxr-xr-x 15 root  root         4096 2021-02-12 17:45:37.638494378 +0100 ..
-rwxr-xr-x  1 fuchs fuchs    85229580 2021-03-21 19:19:02.722117360 +0100 obsidian
...[snip]...
drwxr-xr-x  2 fuchs fuchs 4096 2021-04-02 22:25:56.878314307 +0200 .
drwxr-xr-x 32 fuchs fuchs 4096 2021-04-04 08:20:25.996556925 +0200 ..
-rwxr-xr-x  1 fuchs fuchs  155 2021-03-29 19:11:30.665706518 +0200 backup.sh
-rwxrwxrwx  1 fuchs fuchs   32 2019-11-23 02:37:56.261048000 +0100 close
```

Die Files wie backup.sh  wurden manuell angelegt,

```bash
for i in "PATH" do ls -la --time-style=full $i | grep -v '00000\|->'; done
```

* "->" Links aus der Ausgabe entfernen
*  "\|" Trennzeichen bei grep -v

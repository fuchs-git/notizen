# Find
## Daten einer Gruppe finden
```bash
find / -group staff -ls 2>/dev/null
find / -group staff -ls 2>/dev/null | less -S
```
## Daten eines Nutzers finden
```bash
find / -user fuchs -ls 2>/dev/null
find / -user fuchs -ls 2>/dev/null | less -S
```
Verzeichnisse ausschließen mit [[grep]]
```bash
find / -user fuchs -ls 2>/dev/null | grep -v proc
find / -user fuchs -ls 2>/dev/null | grep -v 'proc\|sys' | less -S
```
## Daten eines Zeitraums finden
```bash
find / -newermt "2021-03-12" ! -newermt "2021-03-21" -ls 2>/dev/null | less -S
```

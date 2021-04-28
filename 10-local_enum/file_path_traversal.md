# Zugriff auf Dateien

## Welche Dienste werden ausgeführt
> /proc/sched_debug 
> suchen nach ".service"

## Offene Ports finden
> /prc/net/tcp {udp}
> Zeigt jeden Port der "offen" ist in hex
> python -c 'print(0x50)'  ->  80

## Eigenen Nutzer herrausfinden
> /proc/self/environ
> hat der Nutzer ein home-dir -> /etc/passwd

## Config Files


## SSH Keys


## SNMP
> /etc/snmp

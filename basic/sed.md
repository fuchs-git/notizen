## Stream EDitor - Kurzreferenz
### Beispiele:
| Kommando | Beschreibung |
| --- | --- | 
| sed -n '/Muster/p' <File> | Ausgabe aller Zeilen, die "Muster" enthalten |
| sed -n '/Muster/,/^$/p' <File> | Zeilenausgabe ab "Muster" bis zur nächsten Leerzeile | |sed '/Muster/d' <File> | Löschen aller Zeilen, die "Muster" enthalten |
| sed 's/Muster/Ersatz/' <File> | Löschen oder Ersetzen von Mustern |
| sed -i 's/Muster/Ersatz/' <File> | <File> wird überschrieben |
| sed 's/abc/def/;s/ghi//;s/jkl//' <File> | mehrere Kommandos |

### Weiteres:
| Kommando | Beschreibung |
| --- | --- | 
| tr -d '\\n' | alle Zeilenumbrüche entfernen (ist mit sed deutlich komplizierter) |
| tr '\\n' ' ' | alle Zeilenumbrüche durch Leerzeichen ersetzen |
| grep -v ^$ | löscht alle Leerzeilen |

#### Tags
#tr [[grep]]
	
#### Referenzen
https://nathansen.de/linux/sed
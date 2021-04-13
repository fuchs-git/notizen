# Links
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

# Option 1
```sql
String query = "SELECT account_balance FROM user_data WHERE user_name = "
          + request.getParameter("customerName");
try {
      Statement statement = connection.createStatement( ... );
      ResultSet results = statement.executeQuery( query );
}      
```
Der Nutzer kontrolliert "customerName", welches direkt durch SQL-Verarbeitet wird.

```sql
String custnme = request.getParameter("customerName");
// Input Validation
String query = "SELECT account_balance FROM user_data WHERE user_name = ? ";
PreparedStatement pstmt = connection-prepareStatement( query );
pstmt.setString( 1, custname);
ResultSet results = pstmt.executeQuery( );
```

# Option 2
- Stored Procedures

# Option 3 
Whitelist Input Validation

## Nur Buchstaben zulassen
```php
if(!/^[a-z]+$/.test(username)){
    throw new Error('Invalid user name');
}
DB.query("UPDATE user SET username='"+username+"'",cb);
```


# Anfällig für SQL Injection
```php
public Boolean authenticate (String name, String pass)

{

Statement stmt = this.conn.createStatement();

String sql = “SELECT name FROM user WHERE name=’ ” + name + “ ’ AND     passwd =’ ” + pass + “ ‘ ”;

ResultSet results = stmt.executeQuery(sql);

return results.first();

}
```

# Sicher
```php
public Boolean authenticate (String name, String pass)

{

PreparedStatement pstmt;

String sql = “SELECT name FROM user WHERE name = ? AND passwd =? ”;

pstmt = this.conn.prepareStatement(sql);

pstmt.setString(0, name);

pstmt.setString(1, pass);

ResultSet results = pstmt.executeQuery();

return results.first();

}
```

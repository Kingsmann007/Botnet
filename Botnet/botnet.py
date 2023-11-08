import requests
from requests.exceptions import ConnectTimeout
url = "https://www.instagram.com/"
def start():
    with open('options.txt', 'r') as f:
        for line in f:
            print(requests.get(url+line+"/"))
start()

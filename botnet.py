import requests
import urllib.request
from requests.exceptions import ConnectTimeout
url = "https://www.instagram.com/"
def start():
    with open('o.txt', 'r') as file:
        for line in file:
            final_url = url + line
            final_url.replace(" ", "")
            if requests.get(final_url).status_code == 200:
                page = urllib.request.urlopen(final_url)
                print(page.read())
start()

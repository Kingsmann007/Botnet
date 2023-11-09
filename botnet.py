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
                lst = []
                for i in page.read():
                    lst.append(chr(i))
                j = False
                str = ""
                for i in lst:
                    if i=="ö":
                        if j:
                            j=False
                        else:
                            j=True
                    elif j:
                        str+=i
                print(str)
start()

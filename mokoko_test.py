import time
import random
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
base_url = 'https://loawa.com/char/%EC%A0%84%EC%9E%90%EB%A7%88%EB%A3%A8'

while True :
    i = []
    try:
        json_string = requests.get(base_url, headers=headers)
    except :
        time.sleep(3)
        continue
    if json_string.status_code != 200:
        time.sleep(3)
        continue
    soup = BeautifulSoup(json_string.content, 'html.parser')
    mokoko = soup.find(attrs = {'class': 'd-none d-lg-block p-1 text-center'}).text[:]

    i.append(mokoko)

    print("지금까지 " + i[0] +"개의 모코코를 모았어요!")

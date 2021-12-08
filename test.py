import time
import random
import telepot
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
base_url = 'http://gall.dcinside.com/mgallery/board/view/?id=elsa&no=74842&_rk=Hc2&page=1'

while True:
    try:
        json_string = requests.get(base_url, headers=headers)
    except :
        time.sleep(3)
        continue
    if json_string.status_code != 200:
        time.sleep(3)
        continue
    soup = BeautifulSoup(json_string.content, 'html.parser')
    comments = soup.find(attrs={'class': 'gall_comment'}).text[3:]
    print("현재 댓글 :" + " " + comments + "개")

    # comment가 6개 이상이면 "비상비상" 이라는 내용을 채널에 보내기 (나중에 수정하기, 능력 되면 댓글 갯수로 엮어주기)#
    if int (comments) >= 6:
        siren = '비상비상'
        telegram_token = '1198419292:AAHOvtMnNOJfZOAoHQ47qWm9h5eTMM7jBqc'
        bot = telepot.Bot(token=telegram_token)
        bot.sendMessage(chat_id='-1001407476163', text=siren)

    time.sleep(random.uniform(1, 3))





# 예전에 쓰던거 #
# import sys
# import io
# import time
# import random
# import telepot
# import requests
# import urllib.request
# import urllib3
# from bs4 import BeautifulSoup
#
# while True:
#
#     try:
#         sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
#         sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
#         #
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#         base_url = 'https://gall.dcinside.com/mgallery/board/view/?id=elsa&no=74842&_rk=Hc2&page=1'
#         json_string = requests.get(base_url, headers=headers).text
#         soup = BeautifulSoup(json_string, 'html.parser')
#         comments = soup.find(attrs={'class':'gall_comment'}).text[3:]
#
#         time.sleep(random.uniform(1, 3))
#         # comment가 6개 이상이면 "비상비상" 이라는 내용을 채널에 보내기 (나중에 수정하기, 능력 되면 댓글 갯수로 엮어주기)#
#
#         if int (comments) >= 9 :
#
#             time.sleep(1)
#
#             while True:
#                 siren = '비상비상'
#                 telegram_token = '1198419292:AAHOvtMnNOJfZOAoHQ47qWm9h5eTMM7jBqc'
#                 bot = telepot.Bot(token = telegram_token)
#                 bot.sendMessage(chat_id = '-1001407476163', text = siren)
#
#
#
#                 break
#         else :
#             print("현재 댓글 :" + " " + comments + "개")
#
#         if soup.status_code != 200:
#             time.sleep(3)
#             continue
#
#     except (ConnectionError, TimeoutError):
#         time.sleep(30)
#         continue
#     time.sleep(30)
#
#
#     # token = '1198419292:AAHOvtMnNOJfZOAoHQ47qWm9h5eTMM7jBqc'
#     # mc = '1081789001'
#     # bot = telepot.Bot(token)
#     # bot.sendMessage(mc, 'Hello World.')














# 되는거(알려준거)

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
# #
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# base_url = 'https://gall.dcinside.com/mgallery/board/view/?id=elsa&no=74842&_rk=Hc2&page=1'
# json_string = requests.get(base_url, headers=headers).text
# soup = BeautifulSoup(json_string, 'html.parser')
# # comm = soup.find_all('ul').find('li')
# comments = soup.find(attrs={'class':'gall_comment'}).text[3:]
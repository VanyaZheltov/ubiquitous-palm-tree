import requests
import json
from bs4 import BeautifulSoup

def get_answer(word):
    html = requests.get('http://akudakova.beget.tech/tables/cmds/').text
    soup = BeautifulSoup(html, 'html5lib')
    qa = soup.find('p').text
    a = json.loads(qa.replace("'",'"'))
    a = {word.lower() : a[word]
    for word in a}
    quests = []
    for q in a:
        quests.append(q.lower())
    if word.lower() in quests:
        return a[word.lower()]
    else:
    	return "Я вас не понял"


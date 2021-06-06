import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('Games.csv','w', newline='\n')
test = csv.writer(file)
test.writerow(['Title','Rating'])


p = {'view': 'detailed','page': 0}
url = 'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered'

while p['page']<10:
    r = requests.get(url, params=p, headers={'user-agent': 'Chrome/91.0.4472.77'})
    # print(r)
    #Response dagvibruna [403], amitom viyeneb user-agent

    content = r.text



    soup = BeautifulSoup(content, 'html.parser')
    b = soup.find('div', class_ = 'browse movie new_releases')
    # print(b)
    games = b.find_all('td', class_ = 'clamp-summary-wrap')

    for each in games:
        title = each.find('a', class_='title').text  # ar viyeneb {'Accept-Language': 'en-US'}, radgan araferi ar utargmnia
        rating = each.a.text.strip()



        print(title)

        test.writerow([title, rating])
    p['page']+=1
    sleep(randint(4,12))

file.close()
#yvelaferi mushaobs idealurad


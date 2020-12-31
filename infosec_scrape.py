import requests
from bs4 import BeautifulSoup


url = "https://infosecindustry.com/news/"
r = requests.get(url)

yelp_soup = BeautifulSoup(r.text, 'html.parser')
count = 0

links = yelp_soup.findAll('div', {'class': 'item-details'})

print('\t' + 'Good morning Derek! here are the first 5 articles from infosecindustry.com. Have a good day!' + '\n')
count = 0


for stuff in links:
    title = stuff.findAll('h3', {'class': 'entry-title td-module-title'})[0].text
    a_tag = stuff.find('a')
    print(title)
    print(a_tag['href'])
    print('\n')
    count = count + 1
    if count == 5:
        break
    
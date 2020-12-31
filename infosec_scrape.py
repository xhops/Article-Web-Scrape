import requests
from bs4 import BeautifulSoup

#declare URL
url = "https://infosecindustry.com/news/"
r = requests.get(url)

yelp_soup = BeautifulSoup(r.text, 'html.parser')

links = yelp_soup.findAll('div', {'class': 'item-details'})

print('\t' + 'Good morning Derek! here are the first 5 articles from infosecindustry.com. Have a good day!' + '\n')
count = 0


for stuff in links:
    title = stuff.findAll('h3', {'class': 'entry-title td-module-title'})[0].text
    a_tag = stuff.find('a')
    print(title)
    print(a_tag['href'])
    print('\n')
    
    #Display only 5 articles
    count = count + 1
    if count == 5:
        break
    

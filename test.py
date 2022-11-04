import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


# this trick the server to think that we are connecting from a web browser
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


opener = AppURLopener()
writer = "robert-frost-poems"
data = opener.open('https://mypoeticside.com/poets/' + writer).read().decode()

# search and save the poem links
soup = BeautifulSoup(data, 'html.parser')
poem_list = soup.find(class_="list-poems")
links = poem_list.findAll('a')
results = ["https:" + link.get('href') for link in links]

# saves the title and content of each poem
titles = []
corpus = []
for page in results:
    data = opener.open(page).read().decode()
    soup = BeautifulSoup(data, 'html.parser')
    title = soup.find(class_='title-poem')
    poem = soup.find(class_='poem-entry')
    titles.append(title.getText())
    print(title.getText())
    corpus.append(poem.find('p').getText())

# saves to a .csv file all the poems
poems = pd.DataFrame({'title': titles, 'text': corpus})
poems.to_csv('poems.csv')
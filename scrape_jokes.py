import urllib3
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup
urlList = ['ugly', 'skinny', 'harrypotter', 'obama', 'crazy', 'scifi', 'anime', 'pokemon', 'stupid', 'political', 'fat']
urlList.extend(['poor', 'nerd', 'doctorwho', 'dark', 'white', 'misc', 'tall', 'short', 'videogame', 'uplifting', 'old'])
urlList.extend(['dirty', 'lazy', 'crosseyed', 'chatty', 'math', 'music', 'gameofthrones', 'religious', 'hairy', 'bald'])
i = 1
for each in tqdm(urlList):
    sys.stdout = open('DataSets//Yo-Mama-' + each + '.txt', 'w')
    url = "http://www.yomamajokesgalore.com/" + each + ".html"
    r = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(r, "html.parser")  # Beautiful soup object


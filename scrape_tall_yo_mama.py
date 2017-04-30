import urllib3
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup

sys.stdout = open('TallJoke.txt', 'w')
url = "http://www.jokes4us.com/yomamajokes/yomamasotalljokes.html"
r = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(r, "html.parser")  # Beautiful soup object

lContent = soup.find('div', attrs={'class': 'LeftContent'})
pList = lContent.findAll('p')
print(pList[0].text.strip())


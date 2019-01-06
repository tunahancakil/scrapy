import requests
from bs4 import BeautifulSoup

n11url = "https://www.n11.com/kitap"

r = requests.get(n11url)

soup = BeautifulSoup(r.content,"html.parser")

gelen = soup.find_all("div",{"class":"catalogview"})
print(gelen)

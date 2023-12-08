from bs4 import BeautifulSoup
import requests
try:
    source=requests.get('https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/')
    source.raise_for_status()

    soup=BeautifulSoup(source.text,'html.parser')
    name=soup.find(class_='itemName')
    print(name)
except Exception as e:
    print(e)



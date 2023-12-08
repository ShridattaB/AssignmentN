import requests
from bs4 import BeautifulSoup

req = requests.get("https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/")

soup = BeautifulSoup(req.content, "html.parser")
res = soup.title

print(res.get_text())

menu_items = soup.find_all('div', class_='itemName')

for item in menu_items:
    menu_name = item.get_text().strip()
    print(menu_name)

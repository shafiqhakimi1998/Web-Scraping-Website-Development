import requests
from bs4 import BeautifulSoup
import csv

url = "https://bubbleteamarket.com/ouvrir-bubble-tea/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
print(f"Le title de la page réfé no1 est : {title}")

data = []

info_items = soup.find_all("div", id="main-content")
for item in info_items:
    titles_2 = item.find_all("h2")
    titles_3 = item.find_all("h3")
    contenus = item.find_all("p")

    for title in titles_2:
        data.append([title.get_text().strip(), ""])
    for title in titles_3:
        data.append([title.get_text().strip(), ""])
    for content in contenus:
        data.append(["","",content.get_text().strip()])

with open(r'C:\Users\ICAMPUS\Documents\les_données_3.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Titre', 'Sub title','Contenu'])
    writer.writerows(data)

print("Les données sont prêtes.")
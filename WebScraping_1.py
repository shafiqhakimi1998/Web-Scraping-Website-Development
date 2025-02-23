import requests
from bs4 import BeautifulSoup
import csv

url = "https://fr.wikipedia.org/wiki/Th%C3%A9_aux_perles"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.title.text
print(f"Le title de la page réfé no1 est : {title}")


data = []

info_items = soup.find_all("div", class_="mw-body-content")
for item in info_items:
    titles = item.find_all("h2")
    contenus = item.find_all("p")
    for title in titles:
        data.append([title.get_text().strip(), ""])
        data.append(["", content.get_text().strip()])

with open('les_données.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Content'])
    writer.writerows(data)

print("Les données sont prêtes.")

import requests
from bs4 import BeautifulSoup
import csv

url="https://www.momentea.com/post/le-top-5-des-bubble-tea-classiques"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
title = soup.title.text
print(f"Le title de la page réfé no2 est : {title}")

data = []

sur_spans = soup.find_all("span", class_ = "GL2zY")
for sur_span in sur_spans:
    sous_spans = sur_span.find_all("span")
    for sous_span in sous_spans:
        print(f"Les Bubble tea sont : {sous_span.text}")
        data.append([title,sous_spans])

with open('les_données_2.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'sous_span.text'])  
    writer.writerows(data) 

print("Les données sont prêtes.")
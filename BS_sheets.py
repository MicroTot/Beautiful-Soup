from bs4 import BeautifulSoup
import requests
import csv

def scraped():
    scraps = []
    url = "https://www.google.com/"  #website url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    clean = soup.prettify()
    print(clean)
    # print(rows)
    rows = soup.find_all(class_= "")
    for r in rows:
        item1=r.find('h1').text
        item2=r.find('h2').text
        item3=r.find('h3').text
        item4=r.find('h4').text
        # print(item1, item2, item3, item4)
        scrap={
            'item1': item1,
            'item2': item2,
            'item3': item3,
            'item4': item4,
        }
        scraps.append(scrap)
    header = ['ITEM1', 'ITEM2', 'ITEM3', 'ITEM4', 'ITEM5']
    data = [item1, item2, item3, item4]
    with open('name.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
scraped()

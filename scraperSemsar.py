import requests
from requests import sessions
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
pageNumber = 3
carMake = [] #DONE
carLink = [] #DONT NEED
carLinkEn = [] #DONT NEED
carModel = [] #DONE
carPrice = [] #DONE
carYear = [] #DONE
carKilometer = [] #DONE
engineCapacity = [] #DONT NEED TILL NOW
Color = [] #DONT NEED TILL NOW
transmissionType = [] #DONT NEED TILL NOW
for i in range(1, pageNumber+1):
    url = 'https://www.carsemsar.com/en/egypt/search?page={}'.format(i)
    client = requests.session()
    HEADERS = ''
    response = client.get(url, headers=HEADERS, verify=True, allow_redirects=True)
    src_website = response.content
    scrap = BeautifulSoup(src_website, 'lxml')
    for titleMain in scrap.findAll('h3', {'class':'listing-title'}):
        hashV1 = titleMain.text.split()
        print(hashV1)
        carYear.append(hashV1[0])
        carMake.append(hashV1[1])
        carModel.append(hashV1[2])
    for kilometerMain in scrap.findAll('ul', {'class':'listing-details'}):
        hashV2 = kilometerMain.text.split()
        if hashV2[2] != 'Contact':
            carKilometer.append(hashV2[2])
        else:
            carKilometer.append('N/A')
        if hashV2[-1] != 'Seller':
            carPrice.append(hashV2[-1])
        else:
            carPrice.append('N/A')

    print('Page Number: ', i)


for i in range(len(carMake)):
    if carMake[i] == 'Mercedes-Benz':
        carMake[i] = carMake[i].replace('Mercedes-Benz', 'Mercedes')
    if carModel[i] == 'C-Class':
        carModel[i] = carModel[i].replace('C-Class', 'C')
    elif carModel[i] == 'E-Class':
        carModel[i] = carModel[i].replace('E-Class', 'E')
    elif carModel[i] == 'B-Class':
        carModel[i] = carModel[i].replace('B-Class', 'B')
    elif carModel[i] == 'A-Class':
        carModel[i] = carModel[i].replace('A-Class', 'A')
    elif carModel[i] == 'CLA-Class':
        carModel[i] = carModel[i].replace('CLA-Class', 'CLA')


df = pd.DataFrame({'carMake': carMake,
                   'carModel': carModel,
                   'carYear': carYear,
                   'carKilometer': carKilometer,
                   'carPrice': carPrice})

df.to_csv('semsar-dataset.csv')
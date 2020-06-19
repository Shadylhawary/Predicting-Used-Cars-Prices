import requests
from requests import sessions
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
pageNumber = 1100
carMake = []
carLink = []
carLinkEn = []
carModel = []
carPrice = []
carYear = []
carKilometer = []
engineCapacity = []
Color = []
transmissionType = []

for i in range(1, pageNumber+1):
    url = 'https://eg.hatla2ee.com/en/car/page/{}'.format(i)
    client = requests.session()
    HEADERS = ''
    response = client.get(url, headers=HEADERS, verify=True, allow_redirects=True)
    src_website = response.content
    scrap = BeautifulSoup(src_website, 'lxml')
    for titleMain in scrap.findAll('div', {'class':'newCarListUnit_header'}):
        #print(titleMain.text.split())
        hashV1 = titleMain.text.split()
        carMake.append(hashV1[0])
        carModel.append(hashV1[1])
        carYear.append(hashV1[-1])
    for kilometerMain in scrap.findAll('div', {'class':'newCarListUnit_metaTags'}):
        for kilometer in kilometerMain.findAll('span', {'class':'newCarListUnit_metaTag'}):
            #print(kilometer.text.split())
            hashV3 = kilometer.text.split()
            if len(hashV3) == 2 and hashV3[1] == 'Km':
                if hashV3[0] == '-':
                    carKilometer.append('N/A')
                else:
                    carKilometer.append(hashV3[0])
                    #print(hashV3[0])

    for priceMain in scrap.findAll('div', {'class':'main_price'}):
        #print(priceMain.text.split())
        hashV2 = priceMain.text.split()
        if hashV2[0] != '-':
            carPrice.append(hashV2[0])
        else:
            carPrice.append('N/A')
    print(f'Page Number: {i} of {pageNumber} Done...')


df = pd.DataFrame({'carMake': carMake,
                   'carModel': carModel,
                   'carYear': carYear,
                   'carKilometer': carKilometer,
                   'carPrice': carPrice})

df.to_csv('hatlaee-dataset3.csv')


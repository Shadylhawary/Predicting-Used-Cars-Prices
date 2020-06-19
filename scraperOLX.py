import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd


pageNumber = 100
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


def checker(l1, l2, l3):
    len1 = len(l1)
    len2 = len(l2)
    len3 = len(l3)
    val = [len(l1), len(l2), len(l3)]
    vaList = [l1, l2, l3]
    if len1 != len2 or len1 != len3:
        smaller = min(range(len(val)), key=val.__getitem__)
        vaList[smaller].append('N/A')
        checker(carModel, carYear, carKilometer)


for i in range(1, pageNumber+1):
    HEADERS = ''
    url = 'https://www.olx.com.eg/en/vehicles/cars-for-sale/?page={}'.format(i)
    CLIENT = requests.session()
    response = CLIENT.get(url, headers=HEADERS, verify=True, allow_redirects=True)
    #print(detail_page)
    src_website = response.content
    scrap = BeautifulSoup(src_website, 'lxml')
    for ads__item__info in scrap.findAll('div', {'class':'ads__item__info'}):
        #print(ads__item__info)
        for ads_carPrice in ads__item__info.findAll('p', {'class':'ads__item__price price'}):
            #print(ads_carPrice.text.split())
            hashV2 = ads_carPrice.text.split()
            carPrice.append(hashV2[0])
        for ads_carMake in ads__item__info.findAll('p', {'class':'ads__item__breadcrumbs'}):
            hashV1 = ads_carMake.text.split()
            #print(hashV1[4])
            #print(ads_carMake)
            carMake.append(hashV1[4])
        for ads_link in ads__item__info.findAll('a', {'class':'ads__item__ad--title'}):
            #print(ads_link.get('href'))
            carLink.append(ads_link.get('href'))

    print(f'Page Number: {i} of {pageNumber} Done...')


for i in range(0, len(carLink)): #----------- For Loop to Make All Links open in English Version of site------
    carLinkEn.append(carLink[i].replace('https://www.olx.com.eg/','https://www.olx.com.eg/en/'))

for k, i in enumerate(carLinkEn, start=0):
    url2 = i
    CLIENT2 = requests.session()
    HEADERS = ''
    response2 = CLIENT2.get(url2, headers=HEADERS, verify=True, allow_redirects=True)
    # print(detail_page)
    src_website2 = response2.content
    scrapPages = BeautifulSoup(src_website2, 'lxml')
    hashL1 = []
    #print(scrapPages)
    for mainTable in scrapPages.findAll('div', {'class':'clr descriptioncontent marginbott20'}):
        #print(mainTable)
        for itemsTable in mainTable.findAll('table', {'class':'item'}):
            #print(itemsTable)
            for testing in itemsTable.findAll('tr'):
                zz = testing.text.split()
                hashL1.append(zz)
        #print('List:  >> ', hashL1)
        for i in range(len(hashL1)):
            if 'Model' in hashL1[i]:
                #print(hashL1[i])
                try:
                    carModel.append(hashL1[i][1])
                except:
                    carModel.append('N/A')
            if 'Year' in hashL1[i]:
                #print(hashL1[i])
                try:
                    carYear.append(hashL1[i][1])
                except:
                    carYear.append('N/A')

            if 'Kilometers' in hashL1[i]:
                #print(hashL1[i])
                try:
                    carKilometer.append(hashL1[i][3])
                except:
                    carKilometer.append('N/A')
        checker(carModel, carYear, carKilometer)
        hashL1.clear()
    print(f'Link {k+1}  of  {len(carLinkEn)}')


df = pd.DataFrame({'carMake': carMake,
                   'carModel': carModel,
                   'carYear': carYear,
                   'carKilometer': carKilometer,
                   'carPrice': carPrice})

df.to_csv('OLX-dataset.csv')
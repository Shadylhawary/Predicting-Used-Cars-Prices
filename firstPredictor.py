from alg1 import getprediction

print('JUST ENTER CAR MAKE, MODEL, YEAR, KILOMETERS !!')




def getinput():
    input_make = input('Car Make: ')
    input_model = input('Car Model: ')
    try:
        input_year = int(input('Car Year: '))
    except:
        print('Enter Valid Integer')
        input_year = int(input('Car Year: '))
    try:
        input_kilometers = int(input('Car Kilometers: '))
    except:
        print('Enter Valid Integer')
        input_kilometers = int(input('Car Kilometers: '))
    return [input_make, input_model, input_year, input_kilometers]


def getpredict(encode):
    predict = getprediction(encode[0], encode[1], encode[2], encode[3])
    return predict


def encoder(li):
    encoded_kilo = 0
    ckilo = li[3]
    if ckilo < 100000:
        encoded_kilo = 0
    if 150000 > ckilo >= 100000:
        encoded_kilo = 1
    if 200000 > ckilo >= 150000:
        encoded_kilo = 2
    if 250000 > ckilo >= 200000:
        encoded_kilo = 3
    if 300000 > ckilo >= 250000:
        encoded_kilo = 4
    if 350000 > ckilo >= 300000:
        encoded_kilo = 5
    if 400000 > ckilo >= 350000:
        encoded_kilo = 6
    if 450000 > ckilo >= 400000:
        encoded_kilo = 7
    if 500000 > ckilo >= 450000:
        encoded_kilo = 8
    if 550000 > ckilo >= 500000:
        encoded_kilo = 9
    if 600000 > ckilo >= 550000:
        encoded_kilo = 10
    if 650000 > ckilo >= 600000:
        encoded_kilo = 11
    if 700000 > ckilo >= 650000:
        encoded_kilo = 12
    if 750000 > ckilo >= 700000:
        encoded_kilo = 13
    if 800000 > ckilo >= 750000:
        encoded_kilo = 14
    if 850000 > ckilo >= 800000:
        encoded_kilo = 15
    if 900000 > ckilo >= 850000:
        encoded_kilo = 16
    if 1000000 > ckilo >= 900000:
        encoded_kilo = 17
    if 1200000 > ckilo >= 1000000:
        encoded_kilo = 18
    if ckilo >= 1200000:
        encoded_kilo = 19
    return [li[0], li[1], li[2], encoded_kilo]


def decoder(result):
    if result == 0:
        return "The Car Price Ranges from 0 to 100,000"
    if result == 1:
        return "The Car Price Ranges from 100,000 to 150,000"
    if result == 2:
        return "The Car Price Ranges from 150,000 to 200,000"
    if result == 3:
        return "The Car Price Ranges from 200,000 to 250,000"
    if result == 4:
        return "The Car Price Ranges from 250,000 to 300,000"
    if result == 5:
        return "The Car Price Ranges from 300,000 to 350,000"
    if result == 6:
        return "The Car Price Ranges from 350,000 to 400,000"
    if result == 7:
        return "The Car Price Ranges from 400,000 to 450,000"
    if result == 8:
        return "The Car Price Ranges from 450,000 to 500,000"
    if result == 9:
        return "The Car Price Ranges from 500,000 to 550,000"
    if result == 10:
        return "The Car Price Ranges from 550,000 to 600,000"
    if result == 11:
        return "The Car Price Ranges from 600,000 to 650,000"
    if result == 12:
        return "The Car Price Ranges from 650,000 to 700,000"
    if result == 13:
        return "The Car Price Ranges from 700,000 to 750,000"
    if result == 14:
        return "The Car Price Ranges from 750,000 to 800,000"
    if result == 15:
        return "The Car Price Ranges from 800,000 to 850,000"
    if result == 16:
        return "The Car Price Ranges from 850,000 to 900,000"
    if result == 17:
        return "The Car Price Ranges from 900,000 to 1,000,000"
    if result == 18:
        return "The Car Price Ranges from 1,000,000 to 1,200,000"
    if result == 19:
        return "The Car Price is Higher Than 1,200,000 !"



def main():
    input_list = getinput()
    encoded_carinfo = encoder(input_list)
    predict = getpredict(encoded_carinfo)
    decoded = decoder(predict)
    print(decoded)


while True:
    main()

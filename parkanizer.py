#!/usr/bin/env python3

from os import path
import requests
import json

url = 'https://go.parkanizer.com/api/multiple-parking-lots/offers'
spotsLeftPath = '/tmp/parkanizer.tmp'

if not path.isfile(spotsLeftPath):
    f = open(spotsLeftPath, "x")
    f.write("0")
    f.close()

try:
    response = requests.get(url)
    parkings = json.loads(response.text)
except:
    sys.exit(1)

if len(parkings) > 0:
    for parking in parkings['parkingLots']:
        if parking['id'] == 'obc-plac-f':
            f = open(spotsLeftPath, "r")
            previousSpotsLeft = f.read()
            f.close()
            currentSpotsLeft = parking['startedPriceTables'][0]['spotsLeft']
            if int(previousSpotsLeft) != int(currentSpotsLeft) and int(currentSpotsLeft) != 0:
                f = open(spotsLeftPath, "w")
                f.write(str(currentSpotsLeft))
                f.close()
                currentPrice = parking['startedPriceTables'][0]['price']
                print('Wolnych miejsc: ' + str(currentSpotsLeft) + ' w cenie: ' + str(currentPrice) + '. Link: https://go.parkanizer.com/#/offers')

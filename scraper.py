import os
import sys
from bs4 import BeautifulSoup
import urllib

#open and read Website
handle = urllib.urlopen('https://cst-205-stephaniedoan.c9users.io/GasPrices.html')
web_data = handle.read()

#create soup object using website and parser
soup = BeautifulSoup(web_data, "html5lib")

#create object containing data from <td> html tag
data = soup('td')

#intialize lists and index
prices = []
locations = []
index = 0

#seperates locations and prices
for point in data:
    print(point.contents)
    if index == 0:
        locations.append(point.contents)

    elif index == 1:
        prices.append(point.contents)

    elif index % 2 == 0:
        locations.append(point.contents)

    else:
        prices.append(point.contents)

    index += 1

print('Prices:\n')
for price in prices:
    print(price)

print('Locations:\n')
for location in locations:   
    print(location.contents)
'''
#sorts prices from low to high
low_to_high = sort(prices)
print('Low to high')
print(low_to_high)
'''    
     
print('end program')

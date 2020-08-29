import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import ssl
import requests
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# item_name = input('Enter the item name:')
def product_fn(item_name=None):
	if ' ' in item_name:
		temp = item_name.split(' ')
		var = ''
		for i in range(len(temp)):
			var += temp[i] 
			if i != len(temp)-1:
				var += '%20'
		item_name = var
	    
	names = []
	prices = []
	ratings = []

	for i in range(2):
		response = requests.get('https://www.flipkart.com/search?q='+item_name+
		          '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i+1))
		data = response.text
		soup = BeautifulSoup(data,'html.parser')
		items = soup.find_all(class_='_3O0U0u')#dict of {class:.} won't work here👍
		for item in items:
			name = item.find('div',{'class':'_3wU53n'})
			price = item.find('div',{'class':'_1vC4OE _2rQ-NK'})
			rating = item.find('div',{'class':'hGSR34'})
			if None in (name, price, rating):
				continue
			names.append(name.text.strip())
			prices.append(price.text.strip())
			ratings.append(rating.text.strip())
	products = pd.DataFrame({'Product': names,'Price(in Rs.)': prices,'Rating':ratings})
	products['Price(in Rs.)'] = products['Price(in Rs.)'].map(lambda x: x.replace("₹",""))
	products['Price(in Rs.)'] = products['Price(in Rs.)'].map(lambda x: x.replace(",",""))
	products['Price(in Rs.)'] = products['Price(in Rs.)'].astype('int')
	products['Rating'] = products['Rating'].astype('float')
	products.to_csv('data.csv')

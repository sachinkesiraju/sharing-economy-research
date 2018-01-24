import csv
import json
import requests
import time
from collections import defaultdict

def writeToFile():
	with open('omni_listings.json', 'a') as data:
		json.dump(listing_data, data)

# Import company list from csv
listings = defaultdict(list) 
with open('omni data.csv') as data:
	reader = csv.DictReader(data)
	for row in reader: 
		for (k, v) in row.items():
			listings[k].append(v)
	listings = listings['id']

	listing_data = {}
	for listing in listings:
		print('requesting listing id:'+listing)
		response = requests.get(url="https://api.beomni.com/items/metadata?id=" + listing)
		data = json.loads(response.text)
		listing_data[listing] = data
		time.sleep(1)

	writeToFile()

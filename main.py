import pymongo
from pymongo import MongoClient
import pprint
from ac import AC
custom_id = 'malachi_custom-id'  # custom id

cluster = MongoClient(AC)
Itemdb = cluster["POE_DOCS"]
buyorderCollection = Itemdb["buyorder"]
currencyCollection = Itemdb["Currency"]
cardsCollection = Itemdb["Cards"]
accessoriesCollection = Itemdb["accessories"]
gemsCollection = Itemdb["gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["weapons"]
armourCollection = Itemdb["armour"]
flaskCollection = Itemdb["flasks"]
while True:
    post_list = []
    # Finds all the buy orders that the user entered and puts them in the list
    for doc in buyorderCollection.find({'custom_id': custom_id}):
        post_list.append(doc)
# this needs to search for post that match the buy order if they do break and alert the user

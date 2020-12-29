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

# Finds all the buy orders that the user entered and puts them in the list
while True:
    m = '0'
    for doc in buyorderCollection.find({'custom_id': custom_id}):
        item_collection = doc['item_type']
        item_name = doc['item_name']
        for matching_doc in currencyCollection.find({'typeLine': item_name}):

            wisper = '@' + matching_doc['accountName'] + ' Hi, I would like to buy your ' + matching_doc['typeLine'] + \
                ' listed in League (stash tab ' + matching_doc['stashname'] + \
                '; position ' + 'x:' + str(matching_doc['x']) + \
                ' ' + 'y:' + str(matching_doc['y']) + ')'
            m = 'Found match!'
            # replace this with GUI
    if m == 'Found match!':
        print(wisper)
        pass

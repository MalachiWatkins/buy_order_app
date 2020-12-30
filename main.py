import pymongo
from pymongo import MongoClient
import pprint
from ac import AC
import time
import json
custom_id = 'malachi_custom-id'  # custom id
cluster = MongoClient(AC)
Itemdb = cluster["POE_DOCS"]
currencyCollection = Itemdb["Currency"]
buyorderCollection = Itemdb["buyorder"]
cardsCollection = Itemdb["Cards"]
accessoriesCollection = Itemdb["accessories"]
gemsCollection = Itemdb["gems"]
jewelsCollection = Itemdb["Jewels"]
mapsCollection = Itemdb["Maps"]
weaponsCollection = Itemdb["weapons"]
armourCollection = Itemdb["armour"]


# Finds all the buy orders that the user entered and puts them in the list
button_pressed = 'PRESSED'  # change this to when a button is pressed
if button_pressed == 'PRESSED':
    loop = True
    cached_results = []
    while loop == True:

        for doc in Itemdb["buyorder"].find({'custom_id': custom_id}):
            # currencyCollection
            item_collection, item_name, item_price = doc['item_type'], doc['item_name'], doc['item_price']

            for matching_doc in Itemdb[item_collection].find({'typeLine': 'Blacksmith\'s Whetstone'}):
                print('yeet')
                whisper = '@' + matching_doc['accountName'] + ' Hi, I would like to buy your ' + matching_doc['typeLine'] + \
                    ' listed in League (stash tab ' + matching_doc['stashname'] + \
                    '; position ' + 'x:' + str(matching_doc['x']) + \
                    ' ' + 'y:' + str(matching_doc['y']) + ')'

                if whisper not in cached_results:
                    print(whisper)
                    cached_results.append(whisper)

import pymongo
from pymongo import MongoClient
from ac import AC
import time
import json

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

stop_button = ''  # change this to when a stop button is pressed
custom_id = 'malachi_custom-id'  # custom id
button_pressed = 'PRESSED'  # change this to when a button is pressed
if button_pressed == 'PRESSED':
    loop = True
    cached_results = []  # stores all the whispers to remove any dupes
    while loop == True:
        # finds the buy order params using your custom id
        for doc in Itemdb["buyorder"].find({'custom_id': custom_id}):
            item_collection, item_name, item_price = doc['item_type'], doc['item_name'], doc['item_price']
            # finds all the documents with matching params from the users buy order
            for matching_doc in Itemdb[item_collection].find({'typeLine': 'Blacksmith\'s Whetstone'}):
                # creates a whisper when it finds a mathching post
                whisper = '@' + matching_doc['accountName'] + ' Hi, I would like to buy your ' + matching_doc['typeLine'] + \
                    ' listed in League (stash tab ' + matching_doc['stashname'] + \
                    '; position ' + 'x:' + str(matching_doc['x']) + \
                    ' ' + 'y:' + str(matching_doc['y']) + ')'

                if whisper not in cached_results:  # checks if the post is a dupe if it is nothing happens if not appends it to a list
                    # this is where GUI alet goes
                    print('Found a match!')
                    cached_results.append(whisper)
        # if the stop button is pressed stop the loop
        if stop_button == 'PRESSED':
            loop = False

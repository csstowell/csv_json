
# import csv & json packages 
import csv
import json


# create file path to CSV file
csvFilePath = 'apple_concepts.csv'


# create JSON file path
jsonFilePath = 'json_apple_concepts.json'


# create an empty dictionary to store converted JSON data
data = {}


# open & read the CSV
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['ID']
        data[id]= rows


# create JSON file with jsonFilePath to write converted data
## create new json file & write data on it
with open(jsonFilePath, 'w') as jsonFile:
    # make it more readable
    jsonFile.write(json.dumps(data, indent=4))
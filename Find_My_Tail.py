import requests
import json

#GET USER LOCATION
send_url = "http://api.ipstack.com/check?access_key=420842183c2b670d8da092c6717024f0"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

#RADAR.IO API IMPLEMENTATION
headers = {
    'Authorization': 'prj_test_sk_b5cdcfa075785c7e9712db8ef351e34bbca32c17',
}

#MARKETS TO FIND CLOSE TO THE LOCATION OF THE USER
markets = ["Co op", "Tesco", "Sainsburys", "LIDL", "Asda", "Morrisons", "M&S", "Aldi", "Waitrose","Iceland market"]

#STORING ALL JSON RESPONSES FROM THE API
all_jsons = []
for i in markets:
	params = (
    	('query', i),
	    ('near', '{},{}'.format(latitude, longitude)),
    	('radius', '5000'),
	    ('limit', '10'),
	)

	response = requests.get('https://api.radar.io/v1/search/autocomplete', headers=headers, params=params)

	my_json = response.json()

	all_jsons.append(my_json)

#print(all_jsons)

#CREATING A NEW DIC TO STORE ALL THE IMPORTANT THINGS INSIDE THE PREVIOUS DIC
stores = {"stores": []}
import pprint
for i in range(0, len(all_jsons)):
	for j in range(0, len(all_jsons[i]['addresses'])):
		if 'placeLabel' in all_jsons[i]['addresses'][j] and all_jsons[i]['addresses'][j]['placeLabel'] in markets and int(all_jsons[i]['addresses'][j]['distance']) < 5001:
			#pprint.pprint(all_jsons[i]['addresses'][0]['placeLabel'])
			stores["stores"].append({"name": all_jsons[i]['addresses'][j]['placeLabel'],"address": all_jsons[i]['addresses'][j]['formattedAddress'], "distance": (str(round(float((all_jsons[i]['addresses'][j]['distance'])*0.000621),2))+" miles"), "latitude": all_jsons[i]['addresses'][j]['latitude'], "longitude": all_jsons[i]['addresses'][j]["longitude"], "link": "https://www.google.com/maps/search/?api=1&query={},{}".format(all_jsons[i]['addresses'][j]['latitude'],all_jsons[i]['addresses'][j]['longitude'])})
#pprint.pprint(stores["stores"])

#RETURN THE STORES DIC IN FORM OF A STRING
def stores_string():
	return str(stores["stores"])

#print(stores_string())
#https://www.google.com/maps/search/?api=1&query=51.3905399,-0.5067432



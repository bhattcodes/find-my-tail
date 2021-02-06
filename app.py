import requests

import json

send_url = "http://api.ipstack.com/check?access_key=420842183c2b670d8da092c6717024f0"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

#print(city)

headers = {
    'Authorization': 'prj_test_sk_b5cdcfa075785c7e9712db8ef351e34bbca32c17',
}

params = (
    ('query', 'LIDL'),
    ('near', '{},{}'.format(latitude, longitude)),
    ('radius', '4600'),
    ('limit', '10'),
)

response = requests.get('https://api.radar.io/v1/search/autocomplete', headers=headers, params=params)

my_json = response.json()

altAndLong = my_json['addresses'][0]['geometry']['coordinates']

data = {
  'description': 'LIDL',
  'type': 'circle',
  'coordinates': '[{},{}]'.format(altAndLong[0], altAndLong[1]),
  'radius': '100'
}

response2 = requests.put('https://api.radar.io/v1/geofences/', headers=headers, data=data)


import pprint
#pprint.pprint(my_json)

print(my_json['addresses'][1])
print(altAndLong)

#--------------------------------------
"""
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/LOCATIONS', methods=['GET'])
def api():
	listOfStores = []
	dicto = {}
	for i in range(0, len(my_json['addresses'])):
		dicto["Result {}".format(i)] = my_json['addresses'][i]
	return dicto

app.run()
"""


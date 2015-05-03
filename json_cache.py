import json

with open('data1.txt', 'w') as outfile:
    data = json.load(outfile)

print data


msg = {
    'reqtype': 'json',
    'api_key': 'bdc8d5a5',
    'api_secret': '0f3d8e42',
    'from': 12532715650,
    'to': 9252572545,
    'text': 'Hello world!'
    }
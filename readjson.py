import requests as r
import json

def read():
    g = r.get(
        'https://api.data.gov.in/resource/2297dfd8-2ba7-49a6-b53f-8796568d4753?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json')

    with open('accident.json', 'w') as f:
        json.dump(g.json(), f, indent=2)


#import requests as r
import keys
import requests as r
import json
from os import write


def get_crypt():
    api_url = 'https://api.nomics.com/v1/markets?key=' + keys.key
    output = r.get(api_url)
    data = output.text
    datFile = open('data_out.json', '+w')
    datFile.write(data)


get_crypt()

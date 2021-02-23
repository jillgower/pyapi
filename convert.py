#!/usr/bin/python3
import requests

url = "https://pokeapi.co/api/v2/pokemon/bulbasaur/"
def json_conv(url):
    json2python = requests.get(url).json() # code goes here!
    return json2python # the value of json2python is the whole dictionary of bulbasaur!

json_conv(url)
# print(json_conv(poke_api))
print(json_conv(url))


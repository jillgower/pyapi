#!/usr/bin/python3

import json

def main():
    with open("challenge.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)
    return datadecoded
    #print(type(datadecoded))
    
def parsed(data):
    for x in data:
        print("Name: " + x["name"])
        print("Email: " + x["email"])
        print("Phone: " + x["phone"])
        print("Address: " + x["address"])


parsed(main())

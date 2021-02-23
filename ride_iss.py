#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json
import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    #groundctrl = urllib.request.urlopen(MAJORTOM)
    # strip off the attachement (JSON) and read it
    # the problem here, is that it will read out as a string
    # helmet = groundctrl.read()
    helmet = requests.get(MAJORTOM).json()

    # show that at this point, our data is str
    # we want to convert this to list / dict
    print(helmet)

    #helmetson = json.loads(helmet.decode("utf-8"))

    # this should say bytes
    print(type(helmet))

    # this should say dict
    print(type(helmet))

    print(helmet["number"])

    # this returns a LIST of the people on this ISS
    print(helmet["people"])

    # list the FIRST astro in the list
    print(helmet["people"][0])

    # list the SECOND astro in the list
    print(helmet["people"][1])

    # list the LAST astro in the list
    print(helmet["people"][-1])

    # display every item in a list
    for astro in helmet["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmet["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])

if __name__ == "__main__":
    main()


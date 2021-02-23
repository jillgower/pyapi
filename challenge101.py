#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

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

    #helmetson = json.loads(helmet.decode("utf-8"))

    # this should say bytes


    # this returns a LIST of the people on this ISS


    # display every item in a list

    # display every item in a list
    print("People in space:" +  str(helmet["number"]))
    for astro in helmet["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"] +" on the" +  astro["craft"])



if __name__ == "__main__":
    main()


#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## get date to be returned##
    req_date = input("Give me the date for picture/video in YYYY-MM-DD format: ")
    ## make a call to NASAAPI with our key
    # apodresp = requests.get(NASAAPI + nasacreds)

    ## build api call with date & creds ##
    apodresp = requests.get(NASAAPI + "date=" + req_date + "&thumbs=true&" + nasacreds)
    ## strip off json
    apod = apodresp.json()

#    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])
    media = (apod["media_type"])
    # if this is a video, send thumbnail url, otherwise just the url to the pic.
    if media == "video":
        print(apod["thumbnail_url"])
    else:
        print(apod["url"])


if __name__ == "__main__":
    main()


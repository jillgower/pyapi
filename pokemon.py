import requests
import wget
# PLAYER 1 (Abe)
def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    url= "https://pokeapi.co/api/v2/pokemon/" + choice + "/"
    return url
# PLAYER 2 (Jill)
def json_conv(url):
    json2python = requests.get(url).json()
    return json2python
# PLAYER 3 (Collin)
def api_slice(json2python):
    poke_pic = json2python["sprites"]["front_default"]
    return poke_pic
# PLAYER 4 (Fei)
def wget_pic(poke_pic):
    wget.download(poke_pic, '/home/student/static/')
def main():
    wget_pic(api_slice(json_conv(api_pull())))
main()

fruitlist= ["strawberries",21,"orange",["corn","broccoli"],"grapes"]
heroes= {"hulk": ["most dangerous","dumbest"],"spiderman": "least dangerous, pretty sharp","blackwidow": {"danger_level": "kinda dangerous", "intellect": "smartest"}}
dang= ["strawberries",21,"orange",["corn","broccoli"],{"hulk": ["most dangerous","dumbest"],"spiderman": "least dangerous, pretty sharp","blackwidow": {"danger_level": "kinda dangerous", "intellect": "smartest"}}]


# from fruitlist,print: - grapes, broccoli
# from hereos, print: Hulk's intellect
# from dang, print: black widow's danger level

print(fruitlist[4], fruitlist[3][1])

print(heroes["hulk"][1])

print(dang[4]['blackwidow']['danger_level'])


#1. A restuarant menu with prices for each item
#2. High scores to an arcade game
#3. All of the months of the year
#4. All the items in your backpack
#5. Look up student emails by their names
#6. A shopping cart
#7.[Add a scenario of your own]

#Data Structures:Tuples.lists,,dictionaries,sets
print("Scenario#1: A restuarant menu with prices for each item")
print("best Structure: Dictionary; best to pair food with price in key/value")
menu = {
    "french Toast" : 12,
    "grand slam" : 12,
    "T- Bone steak": 18,
    "Avacado Toast" : 15
}
for key,item in menu. items ():
    print(key, ": ", item)

    print("Scenario2: All of the months of the year")
    print("best Structure: tuple: We need a collection that does not need to change")
    highscores=[
        100,
        105,
        110,
        99
    ]
    for score in highscores
    print(score)
    
    monthsinYear= (
        "January",
        "Februrary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    )
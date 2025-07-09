
#1. Create a list of items in your room you can potentially pack.
bedroom = ["shoes","clothes","socks","underwear","lotion","cologne","charger"]

#2. Create an empty list to represent your travel bag
travelbag = []
#4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this

#3. repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
print("PACK YOUR BAGS")
print("Enter your index of an index of an item you'd like to move from your room to your bag.")
print("Type'100' when you are done packing./n")
print ("Your bedroom:")
print(bedroom)

item = int(input("Item index:"))

while item !=100:
    travelbag. append (bedroom[item])
    bedroom.remove (bedroom[item])
    print("\n Your Bedroom:")
    print(bedroom)
    print("\nYour Travel Bag:")
    print(travelbag)
    item = int (input("item Index:" ))

    #5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring
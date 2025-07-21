import CreateClass

movies = ["Rush Hour", "Ninja Turtles Secret of the Ooze", "Spiderman2"]
games =  ["Madden 25", "MLB The Show 25", "NBA2k24", "SpiderMan 2"]

MyCollection = CreateClass.Collection(movies,games)

MyCollection.SetFavGame("NBA2k24")
MyCollection.SetFavMovie("Rush Hour")   
MyCollection.DisplayCollection()


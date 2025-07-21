# this program will allocate teams randomly from a list
#1. Import the random module
#2. Create a list of every genius
#3. Use the random module. to randomly shuffle the list
#4. Loop through the list and display each team's player
#5. Using an if statement to see if the user is happy with
#if not, it will shuffle again. If so, the program terminates

import random

# Create a list of players stored in the player variable
players = ["Kamari", "Max", "Braylen",
           "Ollie" ,"Xavier", "Avery",
           "Carl", "Walter", "Daren",
           "EJ", "Nahum", "Joaquin",
          "Marshawn", "Ja'Den", "Isaiah",
          "Kenlon", "Nishad", "Kauri",
          "Kriss", "Joseph", "Semaj",
          "Tay", "Taqari", "Jarmauri"]
           
def PickTeams(players):     # Create our function
    random. shuffle(players)   # Shuffle the list of players
    team1= players [:len (players)// 2] #Put the 1st half of the players into the 1st team
    teamCaptain1 = team1[random. randrange (0, 12)]

    print("TEAM 1")
    print ("Team 1 Captain: " + teamCaptain1)
    print (team1)

PickTeams(players)


def PickTeams (players): #Create our function
    random. shuffle (players) # Shuffle the list of players
    team2= players [: len (players)//2] # Put the 1st half of the players into the team
    teamCaptain2 = team2 [random. randrange (0,12)]

    print ("TEAM2")
    print ("Team 2 Captain:" + teamCaptain2)
    print (team2)
PickTeams(players)
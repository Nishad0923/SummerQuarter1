#0. Prompt the players for their names
#1. Prompt player 1 for RPS
#2. Prompt player 2 for RPS
#3. Compare p1 and p2 choices and decide a winner

def RPS():  
    print("Welcome to Rock Paper Scissors!")
  #Gather Player names
    player1 = input("Player 1, Please enter your name")
    player2 = input ("Player 2, please enter your name")
   #Gather player moves
    p1_Choice=input ((f"{player1}",Choose between, Rock, Paper & Scissors))
    
    while not IsValidMove (p1_Choice):
     print ("Invalid Move ! Please try again")
    p1_Choice= input ((f"{player1}", Choose between Rock, Paper & Scissors))
    
    p1_Choice = input(f"{player1}, choose between Rock,Paper & Scissors")
    p2_Choice = input(f"{player2}, choose between Rock, Paper & Scissors")

    #Compare player moves
    
    
    
    if p1_Choice == "rock" and p2_Choice == "scissors":
        print (f"Rock beats scissors,{player1} wins!") 
    elif p1_Choice == "paper" and p2_Choice == "rock":
        print (f"paper beats rock,{player1} wins!") 
    elif p1_Choice == "scissors", {player1} wins!

    elif  p2_Choice == "rock" and p1_Choice == "scissors":
          print (f"Rock beats scissors, {player2}" wins)
    
    elif p2_Choice == "paper" and p1_Choice == "rock":
        print(f"paper beats rock, {player2} Wins!")
    
    elif p2_Choice == "scissors" and p1_Choice == "paper":
        print (f"scissors beats paper, {player2} Wins!")

def IsValidMove(playermove):
    validMoves= ["rock", "paper","scissors"]
    if playermove in validMoves:
        return True    
    else:
        return False

RPS()

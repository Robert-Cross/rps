import time 
Rock= "Rock"
Paper = "Paper"
Scissors = "Scissors"
Player1 = "Player1"
Player2 = "Player2"
print("Welcome to R,P,S")
time.sleep(2)
print("Would you like to contune;")
print("Would you like to know more about the game?")
YN = input("")
if YN == "Yes":
    print("Rock,Paper,and Sci")
elif YN == "No":
    print("Ok,seems like you have the hang of things.")
time.sleep(2)
print("Do you have one or two players.")
player = input("") 
if player == "1":
    print("You need two players to play this game.")
elif player == "2":
    print("Lets play")
time.sleep(2)
print("pick Rock,Paper,or Scissors")
Rock = input
Paper = input 
Scissors = input

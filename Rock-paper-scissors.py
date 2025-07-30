from random import choice

options=["rock","paper","scissors"]


player_score=0
computer_score=0

i=0
while True:
   print(f"Round number {i+1}")
   player=input("choose from rock/paper/scissors\n")
   computer=choice(options)
   print(f"computer choice is {computer}")
   print(f"your choice is {player}")
   
   if (player==computer):
       print("this is draw")
   elif (player=="rock" and computer=="scissors" or player=="paper" and computer=="rock" or player=="scissors" and computer=="paper"  ):
      print("you won")
      player_score=player_score+1
   elif player in options:
      print("you loose")
      computer_score=computer_score+1
    
   else:
      print("invalid input,please enter rock/paper/scissors")
      continue
   i=i+1


   ask=input("Do you want to player another round yes/no\n")
   if(ask!="yes"):
      break
   else:
      continue


print("Thank you for playing")
print("Total round played",i)
if(player_score>computer_score):
   print("You are the overall winner")
   print("Your score is ",player_score)
   print("computer score is ",computer_score)
else:
   print("computer is the winner")
   print("computer score is ",computer_score)
   print("Your score is ",player_score)
   
   
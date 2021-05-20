import random,playsound
pc_score=0
user_score=0
print("WELCOME TO SNAKE WATER & GUN GAME")
l=["S","W","G"]
number_of_games=1
TIE=0
while(number_of_games<=10):
    print("USER TURN-:select","\n","1.S","\n","2.W","\n","3.G")
    user_turn=input()
    pc_turn = random.choice(l)
    if(user_turn=="S" and pc_turn=="S"):
        print("There is a tie")
        TIE+=1
    elif(user_turn=="S" and pc_turn=="W"):
        print("User won the Game")
        user_score=user_score+1
    elif(user_turn=="S" and pc_turn=="G"):
        print("Pc won the Game")
        pc_score=pc_score+1
    elif(user_turn == "G" and pc_turn == "G"):
        print("There is a tie")
        TIE += 1
    elif (user_turn == "G" and pc_turn == "W"):
        print("PC won the Game")
        pc_score = pc_score + 1
    elif (user_turn == "G" and pc_turn == "S"):
        print("User won the game")
        user_score=user_score+1
    elif(user_turn == "W" and pc_turn == "W"):
        TIE += 1
        print("There is a tie")
    elif (user_turn == "W" and pc_turn == "G"):
        print("User won the Game")
        user_score = user_score + 1
    elif(user_turn == "W" and pc_turn == "S"):
        print("User won the game")
        user_score=user_score+1
    number_of_games=number_of_games+1
print(f"USER SCORE {user_score}")
print(f"PC SCORE {pc_score}")
print(f"Numbers of tie: {TIE}")
if(user_score>pc_score):
    print("User won the game")
elif(pc_score>user_score):
    print("PC won the game")
else:
    print("No one won the game")




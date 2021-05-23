import random
number=random.randint(1,100)
no_of_guesses=0
user_number=None
while(user_number!=number):
    user_number=int(input("Enter the number of your choice-"))
    no_of_guesses=no_of_guesses+1
    if(user_number==number):
        print(f"Congrats!! You guessed the right number-({user_number})")
    elif(user_number>number):
        print("Lower number please")
    elif(user_number<number):
        print("Higher number please")
    with open("high_score.txt","a") as h:
        h.write(f"Guess_no-{no_of_guesses}\n")
print(f"No of guesses you took-{no_of_guesses}")

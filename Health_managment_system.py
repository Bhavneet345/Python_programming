def getdate():
    import datetime
    a=datetime.datetime.now()
    return a
def get_name(n):  ##Function for accepting client name#
    if(n==1):
        print("whether you want to retrieve(2) or add(1)")
        d=int(input())
        if(d==1):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if(c==1): #to add food item
                print("what do you want to add in food")
                food_add=input()
                f=open("harry_food.txt","a")
                f.write(str(getdate())+":"+food_add+"\n")
                print("successfully written")
                f.close()
               ##to add exercise done
            if(c==2):
                print("what do you want to add in exercise")
                exercise_add=input()
                f=open("harry_exercise.txt","a")
                f.write(str(getdate())+":"+exercise_add+"\n")
                print("successfully written")
                f.close()
        ##to read the content in the file
        elif(d==2):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if (c == 1):
                f = open("harry_food.txt")
                b=f.read()
                print(b)
                f.close()

            if (c == 2):
                f = open("harry_exercise.txt")
                b = f.read()
                print(b)
                f.close()
    ## to read and write the content to Rohan
    if (n == 2):
        print("whether you want to retrieve(2) or add(1)")
        d = int(input())
        if (d == 1):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if (c == 1):
                print("what do you want to add in food")
                food_add = input()
                f = open("Rohan_food.txt", "a")
                f.write(str(getdate())+":"+food_add+"\n")
                print("successfully written")
                f.close()

            if (c == 2):
             print("what do you want to add in exercise")
             exercise_add = input()
             f = open("Rohan_exercise.txt", "a")
             f.write(str(getdate()) + ":" + exercise_add + "\n")
             print("successfully written")
             f.close()

        elif (d == 2):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if (c == 1):
             f = open("Rohan_food.txt")
             b = f.read()
             print(b)
             f.close()

            if (c == 2):
             f = open("Rohan_exercise.txt")
             b = f.read()
             print(b)
             f.close()
    ##to read and write the content of Hamad
    if (n == 3):
        print("whether you want to retrieve(2) or add(1)")
        d = int(input())
        if (d == 1):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if (c == 1):
                print("what do you want to add in food")
                food_add = input()
                f = open("Hamad_food.txt", "a")
                f.write(str(getdate()) + ":" + food_add + "\n")
                print("successfully written")
                f.close()

            if (c == 2):
             print("what do you want to add in exercise")
             exercise_add = input()
             f = open("Hamad_exercise.txt", "a")
             f.write(str(getdate())+":"+exercise_add+"\n")
             print("successfully written")
             f.close()


        elif (d == 2):
            print("Enter 1 for food or 2 for exercise")
            c = int(input())
            if (c == 1):
             f = open("Hamad_food.txt")
             b = f.read()
             print(b)
             f.close()

            if (c == 2):
             f = open("Hamad_exercise.txt")
             b = f.read()
             print(b)
             f.close()


print("enter the number of client whose data you want","\n","1.Harry","\n","2.Rohan","\n","3.Hamad")
roll_no=int(input())
if(roll_no==1):
    get_name(1)
elif(roll_no==2):
    get_name(2)
elif(roll_no==3):
    get_name(3)
else:
    print("details not available")

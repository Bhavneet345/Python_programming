import time
from pygame import mixer
mixer.init()
if __name__=='__main__':
    print("Welcome Programmer\n")      ##Begins by welcoming the client##
    initial_eye=time.time()
    initial_activity=time.time()
    initial_water=time.time()
    water_sec=1200  ##in seconds
    eye_sec=1800    ##in seconds
    activity_sec=3600  ##in seconds
    water=1
    eye=1
    activity=1
    while(True):
        """Glasses of water"""           #for water break#
        if(time.time()- initial_water > water_sec):
            print("Water break")
            mixer.music.load("music.mp3")
            mixer.music.set_volume(0.01)
            mixer.music.play()
            statment = input("Enter your action-")
            if (statment == "Drank" or statment == "drank"):
                mixer.music.stop()
                with open("Water.txt", "a") as w:
                    w.write(statment +  "at"  + time.ctime() + "\n")
            initial_water = time.time()
        """Eye exercise"""
        if (time.time()- initial_eye > eye_sec):     #for eye break#
            print("Eye break")
            mixer.music.load("music.mp3")
            mixer.music.set_volume(0.01)
            mixer.music.play()
            statment = input("Enter your action-")
            if (statment == "Eye_Done" or statment == "eye_done"):
                mixer.music.stop()
                with open("Eye.txt", "a") as w:
                    w.write(statment +  "at"  + time.ctime()+"\n")
            initial_eye=time.time()
        """"Physical activity"""
        if (time.time() - initial_activity > activity_sec):  #for exercise activity break#
            print("Physical activity break")
            mixer.music.load("music.mp3")
            mixer.music.set_volume(0.01)
            mixer.music.play()
            statment = input("Enter your action-")
            if (statment == "Exercise done" or statment == "exercise done"):
                mixer.music.stop()
                with open("Eye.txt", "a") as w:
                    w.write(statment +  "at"  + time.ctime()+"\n")
            initial_activity=time.time()


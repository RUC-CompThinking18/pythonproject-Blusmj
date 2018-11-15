import time
import random
#import image small drawings are going to be used for if I attatch pictures to the project


def ch1():
   ch1=("yes","Yes","No","no") #Used for yes or no choices

def intro(): #Used to start the code and define
    print("...")
    time.sleep(2) #gives intervals of 2 seconds between prints
    print("... ")
    time.sleep(2)
    print ("You feel as though your floating.\n")
    time.sleep(3)
    print ("You attempt to feel around, but it feels as though your arms don't exist.\n")
    time.sleep(2)
    print ("What has happened to you?\n")
    time.sleep(4)
    print ("You feel that the body you moved in freely has been snatched away in the span of seconds\n")
    time.sleep(3)
    print ("The last thing you remember was the roaring of planes overhead and ear piercing whistle-like sounds.\n")
    time.sleep(2)
    print ("The thought of the memory gave a chilling sensation.\n")
    time.sleep(2)
    print ("After some time you see a light.\n")
    time.sleep(3)
    print ("With all the strength you had to muster you try to move towards it.\n ")
    time.sleep(2)
    print ("Each movement towards the light made you feel more strange than the last.\n")
    time.sleep(2)
    print ("As if your body was turning into jello.\n")
    time.sleep(2)
    print ("You emerge from the light and were greeted by rocks and giant blue crystal resting in the middle of the cave.\n ")
    time.sleep(3)
    print ("You take a step towards it...\n")
    time.sleep(3)
    print ("But immediately you notice that you don't have legs.\n")
    time.sleep(3)
    print ("You try to move as you used to, but to no avail.\n")
    time.sleep(2)
    print ("After trial and error you figure out that you can roll, but found that hopping around was more efficient.")
    time.sleep(3)
    print ("as you never felt tired or that you were straining yourself jumping up and down.\n")
    time.sleep(2)
    print ("After getting used to whatever your squishy feeling body turned into you face back towards the crystals.\n")

    ch1=str(raw_input("Will you take the crystals?(Y/N)\n"))#Choice 1
    if ch1 == "yes" or "Yes": #Selecting yes shows different events
      print ("Attempting to touch the crystals, they inturn dissolved inside of you after contact.\n")
    elif ch1 == "no" or "No":#Selecting no chooses different events  as well
      print ("You look at the crystal, but a strong feeling in your gut told you not to mess with it.\n")
    else:
      print("Not a valid response. Please Input yes or no.\n")
      while True:
        if ch1 !="yes" or "Yes" or "no" or "No":
         return ch1


#class self:
 #def__init__(self, item_type, name)
 #self.self_type = self_type
 #self.name = name
 #
intro()

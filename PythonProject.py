import time
import random

def ask_YN(question): #Ask yes or no question
   answer_YN=("yes","no) #Used for yes or no choices
   response= none
   while response not in answer_YN:
      response = input (question) not in answer_YN
      if response not in answer_YN:  #if it isn't yes or no prompts below code
         print("Not a valid response. Please Input yes or no.")
      return response

def intro(): #introduction
    print("Lorem ipsum dolor sit amet.")
    time.sleep(2) #gives intervals of 2 seconds between prints
    print("consectetur adipiscing elit. ")
    time.sleep(2)
    print (" Cras vel nisl ac leo tristique luctus in eu odio.")
    time.sleep(3)
    print ("Mauris massa ligula, dapibus at tincidunt lobortis, consequat non est.")
    intro()


class item:
   def__init__(self, item_type, name)
      self.item_type = item_type
      self.name = name

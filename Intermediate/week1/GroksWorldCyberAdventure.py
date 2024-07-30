#Define a function to show the intro information
def intro():
  print("Welcome to Grok's World Cyber Adventure!")
  print("You are a cyber security specialist")
  print("tracking down hackers in a virtual world.")
  print("There are portals to the")
  print("mainframe and data mines.")
  print("***********************")

#Define a function to get user portal choice and return the portal
def choose_portal():
  print("***********************")
  portal = input("Portal? (mainframe/data mines): ").lower()
  return portal

#Define a function to show output if the player chooses Mainframe
def mainframe_portal():
  print("***********************")
  print("You find digital footprints left by the hackers.")
  print("You follow them and catch the hackers in the act.")
  print("You have successfully secured the system!")

#Define a function to show output if they player chooses Data Mines
def data_mines_portal():
  print("***********************")
  print("You trigger a hidden trap set by the hackers!")
  print("You get caught in a loop of corrupted data") 
  print("The hackers escaped! Regroup and try again.")

#Define a function to give a clue based on the modulo of number chosen
def choose_clue(number):
  if number % 5 == 0:
    return "Grokker intercepted a message with the code MF!"
  elif number % 3 == 0:
    return "Grokker was sent a DM about hidden traps!"
  else: 
    return "Grokker hasn't had any intel on this cyber hunt."

#add your code here to complete the play_game() function  
def play_game():
  intro()
  num =  int(input("Enter an integer to receive some intel: ")) #Get user input asking for an integer to get an intel clue, and then save the input in a variable.
  print(choose_clue(num))#Call the choose_clue(number) function, sending the user's number input as an argument. And print the returned value
  a = choose_portal()
  if a == "mainframe":# checking if the user has inputed the a vaild response and which function to call
    mainframe_portal()
  elif a == "data mines":
    data_mines_portal()
  else:
    print("Please pick either mainframe or data mines.")  
  
  
# Start the game
play_game()
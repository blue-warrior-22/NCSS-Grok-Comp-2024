#This function takes an integer as an argument - roll 
#and returns a food value based on the value of roll
def choose_delicacy(roll):
  d = ""
  if roll <= 5:
     d ="pizza"
  elif roll >= 6 and roll <=14:
    d="fish and chips"
  elif roll >= 15 and roll <= 19:
    d="Chinese"
  elif roll == 20:
    d="Thai"
  da = "You should order "+ d
  return da
  

#Get input from the dice roll
d20 = int(input('What is the dice roll? '))

#Call the choose_delicacy function and save the value in a variable
delicacy = choose_delicacy(d20)

#Print out the results

print(delicacy)
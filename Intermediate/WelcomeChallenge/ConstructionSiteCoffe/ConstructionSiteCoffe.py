word = input("WHAT DRINK DO YOU WANT TO ORDER? ")
if word.islower():
  print("I DIDN'T HEAR YOUR ORDER!")
elif word.isupper():
  num = int(input("HOW MANY? "))
  print(f"{num} {word}S COMING RIGHT UP!")
else:
  print("I CAN'T UNDERSTAND YOU!")
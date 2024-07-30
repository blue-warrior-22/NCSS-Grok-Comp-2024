word = input("WHAT DRINK DO YOU WANT TO ORDER? ")
num = int(input("HOW MANY? "))

if word.isupper():
  print(f"{num} {word} COMING RIGHT UP!")
elif word.islower():
  print("I DIDN'T HEAR YOUR ORDER!")
else:
  print("I CAN'T UNDERSTAND YOU!")

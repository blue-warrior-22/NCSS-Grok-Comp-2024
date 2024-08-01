people = input("People in line: ")
occupied = int(input("Number of people inside: "))
people=people.split(",")
if occupied == 8:
  print("No more room!")
else:
  space=8-occupied
  allowed = ",".join(people[0:space])
  print(f"These people can enter: {allowed}")

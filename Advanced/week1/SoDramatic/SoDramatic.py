print("The Drama Tisers")
print("----------------\n")
print("Select an option below\n")
members = []

while True:
  action = input("<a>dd a new member, <p>rint members, <q>uit: ").lower()
  if action == "q":
    break
  if action == "a":
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    interest_act = input("Are you interested in acting? <y>es, <n>o: ")
    interest_prod = input("Are you interested in helping with the production? <y>es, <n>o: ")
    if not first or not last:
      print("You need to enter a first name AND a last name")
      print("Details have not been added. Please try again.\n")
    else:
      full = first + " " + last
      members.extend([full,interest_act,interest_prod])
    
  if action == "p":
    print("\nOur current list of members and preferences\n-------------------------------------------")
    print("\nMembers\n------")
    [print(members[i]) for i in range(0,len(members),3)]
    print("\nActors\n------")
    [print(members[i]) for i in range(0,len(members),3) if members[i+1].lower()=="y"]
    print("\nHelpers\n------")
    [print(members[i]) for i in range(0,len(members),3) if members[i+2].lower()=="y"]
    print()
  
    
      

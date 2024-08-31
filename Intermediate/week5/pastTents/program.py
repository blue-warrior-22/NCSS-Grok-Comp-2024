file = input("Enter a shopping list file: ")

duplicates = []

with open(file) as f:
  listS = f.readlines()
for i in listS:
  i = i.replace("\n","")
  if i not in duplicates:
    duplicates.append(i)

#sorted(duplicates)
duplicates.sort()
print("Final list:")
for i in duplicates:
  print(i)
a = input("Which tale shall we read? ")

with open(a) as file:
  fFile = file.read()

j = 0
b = fFile.split()
for i in b:
  if len(i) == 6:
    j+=1
print(f"That tale had {j} 6-letter words in it.")

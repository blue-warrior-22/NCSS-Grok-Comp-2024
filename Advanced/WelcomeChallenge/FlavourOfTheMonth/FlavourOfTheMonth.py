fla = []
for line in open('flavours.txt'):
  fla.append(line.rstrip())

word = input("Check flavour: ")

if word in fla:
  print("Done it already.")
else:
  print("Sounds good!")
fla = []
for line in open('flavours.txt'):
  fla.append(line.rstrip())
end = True
while end:
  word = input("Check flavour: ")

  if word in fla:
    print("Done it already.")
  elif word == "":
    end = False
  else:
    print("Sounds good!")
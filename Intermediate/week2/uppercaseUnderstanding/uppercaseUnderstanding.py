a = input("Sentence: ")

b = []
b = a.split()
c = 0
for i in b:
  if i.isupper():
    c+=1
print(f"Number of words in capitals: {c}")

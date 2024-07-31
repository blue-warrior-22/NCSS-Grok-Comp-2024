word = input("Team: ")
a = word
print(a.lower())
for i in range(len(word)):
  print(f"Give me a {a[i].upper()}!")
  
print(f"What does that spell? {word.upper()}!")
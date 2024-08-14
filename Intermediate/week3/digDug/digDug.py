a = []

while len(a) < 3:
  word = input("Channel name: ")
  if "dig" in word.lower():
    a.append(word)
a.sort()
a.reverse()
print(f"Proposals: {', '.join(a)}")
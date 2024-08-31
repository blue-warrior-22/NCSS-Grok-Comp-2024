data = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('cipher.txt') as f:
  for line in f:
    key, value = line.split()
    data[key] = int(value)
newMsg = []
msg = input('Secret Message: ')
msg = msg.split(' ')
for i in msg:
  for j in i:
    j = j.upper()
    if j in alphabet:
      newMsg.append(data[j])
    #newMsg.append(data[])
#print(f'There are {data[msg]} grams of {ord(msg)} in this recipe. Yum!')
print("Code:", ' '.join(str(x) for x in newMsg))
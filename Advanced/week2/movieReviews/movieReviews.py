import csv 
import json 

filename = 'movies.csv'
with open('reviews.json', 'r') as filej:
    dataj = json.load(filej)
data = []
with open(filename, mode='r', newline='') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Add the row dictionary to the list
        data.append(row)

k =1
a = []

print("Movie ratings:")
for i in data:
  #print(f"i: {i} \n")
  
  #print(len(b))
  a = dataj.get(str(k))
  if i != None:
   if a != None:
    print(f"{i['id']}. {i['title']}: {sum(a)/len(a):3.2f}")
  k+=1
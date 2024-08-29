countries = {}

while len(countries) < 3:
  name = input('Name: ')
  food = input('Country to bring food from: ')
  if food in countries.values():
    print(f"Someone already chose {food}!")
  else:countries[name] = food
print("Final Food Club countries:")
for name, food in countries.items():
  print(f'{name} is bringing food from {food}')

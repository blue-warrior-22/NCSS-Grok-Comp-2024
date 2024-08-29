tasks = {}

while True:
  ingredient = input('Ingredient: ')
  if ingredient == "": break
  quantity = int(input('Quantity: '))
  if ingredient in tasks.keys():
    tasks[ingredient] += quantity
  else:tasks[ingredient] = quantity
print("Total ingredients collected:")
for ingredient, quantity in tasks.items():
  print(f'{ingredient}: {quantity}')
  

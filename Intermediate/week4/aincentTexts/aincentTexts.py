first, second, third = input("Enter the 3 text fragment file names in the correct order: ").split()

with open(first) as file_1:
  part_1 = file_1.read()

with open(second) as file_2:
  part_2 = file_2.read()

with open(third) as file_3:
  part_3 = file_3.read()

ancient_text = f"{part_1}{part_2}{part_3}"
print("Complete Incantation:")
print(ancient_text)

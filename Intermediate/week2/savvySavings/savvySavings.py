# Get user input to use in the for loop range arguments
# and savings calculations
savings = 0
months = 0
item = input("What item do you want to buy? ")
cost = int(input("Item cost $: "))
save_amount = int(input("Savings amount $: "))
duration = int(input("How many months? "))
step_increment = int(input("How often will you save? "))
# Print the results of the savings time calculations
# months are needed to save to reach the item price
n = save_amount
for i in range(step_increment-1,duration,step_increment):
 print(f"After {i+1} month(s) you will have saved ${n}")
 n += save_amount
if cost <= n:
 print(f"You saved ${cost} and have enough to buy your {item}!")
else:
 print(f"You need to save more to buy your {item}.")
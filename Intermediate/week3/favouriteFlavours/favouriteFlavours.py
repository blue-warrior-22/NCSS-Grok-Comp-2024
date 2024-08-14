top_20_flavours = [
    "Vanilla", "Chocolate", "Boysenberry", "Hokey Pokey",
    "Mint Chocolate Chip", "Cookies & Cream", "Salted Caramel",
    "Mango", "Strawberry", "Pavlova", "Rum Raisin", 
    "Chocolate Chip", "Rocky Road", "Lemon Sorbet", "Macadamia Nut",
    "Coffee", "Peanut Butter", "Raspberry Ripple", "Green Tea",
    "Passionfruit"
]

word = input("What is your favourite ice cream? ")
if word.title() in top_20_flavours:
  print(f"{top_20_flavours[top_20_flavours.index(word.title())]} is at position {top_20_flavours.index(word.title())+1} in the top 20 list.")
else:
  print(f"Your favourite flavour is too unique for this list!")
print(f"Top 20 ice cream flavours are: {', '.join(top_20_flavours)}")
    
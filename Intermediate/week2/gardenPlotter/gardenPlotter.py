#
#
#=================this code may not work in some terminals due to no support for unicode characters==================
#
#
typ = input("Garden type: ")
pvar = input("Plant varieties: ")
make = input("Items needed to make the garden: ")

pvar = pvar.split()
print(f"We are building a garden in the style of: {typ}")
print(f"Plants needed: {" 🌱 ".join(pvar)}")
print("To build the garden we will need:")
make = make.split()
for i in make:
  print(f"⚙️ {i}")
eevee = {
  "vaporeon": "Water type and their name is Rainer", 
  "jolteon": "Electric type and their name is Sparky", 
  "flareon": "Fire type and their name is Pyro", 
  "espeon": "Psychic type and their name is Sakura", 
  "umbreon": "Dark type and their name is Tamao", 
  "leafeon": "Grass type and their name is Linnea", 
  "glaceon": "Ice type and their name is Rea", 
  "sylveon": "Fairy type and their name is Kira"
}


a = input("Enter a pokemon: ")
a = a.lower()

if a in eevee:
  print(eevee[a])
else:
  print("That pokemon isn't in the dictionary")
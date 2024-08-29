character_props = {'Harry Potter': 'wand', 
                   'Hermione Granger': 'time-turner', 
                   'Ron Weasley': 'Deluminator', 
                   'Luke Skywalker': 'lightsaber', 
                   'Darth Vader': 'helmet', 
                   'Iron Man': 'arc reactor', 
                   'Spider-Man': 'web shooters', 
                   'Batman': 'batarang', 
                   'Wonder Woman': 'lasso of truth', 
                   'Katniss Everdeen': 'bow and arrow', 
                   'Indiana Jones': 'whip', 
                   'Thor': 'Mjolnir', 
                   'Captain America': 'shield', 
                   'Mario': 'super mushroom', 
                   'Pikachu': 'lightning bolt'}

my_character = input("Enter character name: ")

if my_character in character_props:
  prop = character_props [my_character]
  print(f"{my_character} needs a {prop}!")
else:
  print("Sorry, we don't know that character.")
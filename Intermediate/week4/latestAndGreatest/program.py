games = {'Granblue Fantasy: Relink': '12 January', 
         'Persona 3 Reload': '19 January', 
         'Minecraft Legends': '26 January', 
         'Hogwarts Legacy': '09 February', 
         'Sonic Frontiers': '16 February', 
         'FIFA 24': '23 February', 
         'Final Fantasy VII Rebirth': '01 March', 
         'Kirby and the Forgotten Land': '08 March', 
         'Splatoon 3': '15 March', 
         'LEGO Star Wars: The Skywalker Saga': '05 April', 
         'Overwatch 2': '12 April', 
         'The Legend of Zelda: Breath of the Wild 2': '19 April', 
         'Pokémon Legends: Arceus': '03 May', 
         'Mario Strikers: Battle League': '10 May', 
         'Crash Bandicoot 4: It’s About Time': '17 May', 
         'Ratchet & Clank: Rift Apart': '07 June', 
         'Plants vs. Zombies: Battle for Neighborville': '14 June', 
         'Splatoon 3 Expansion Pass': '21 June', 
         'Minecraft Dungeons': '05 July', 
         'Animal Crossing: New Horizons': '12 July', 
         'Kirby Fighters 2': '19 July', 
         'Star Wars: Outlaws': '02 August', 
         'Monster Hunter Rise': '09 August', 
         'The Sims 5': '16 August', 
         'Fortnite: Save the World': '06 September', 
         'Mario Kart 9': '13 September', 
         'Apex Legends': '20 September', 
         'Halo Infinite': '04 October', 
         'Genshin Impact': '11 October', 
         'FIFA 25': '18 October', 
         'Among Us VR': '01 November', 
         'Pikmin 4': '08 November', 
         'Forza Horizon 5': '15 November', 
         'Super Smash Bros. Ultimate': '06 December', 
         'The Legend of Zelda: Tears of the Kingdom': '13 December', 
         'Yooka-Laylee and the Impossible Lair': '20 December'}

months_of_the_year = ['January', 'February', 'March', 'April', 'May', 'June', 
                      'July', 'August', 'September', 'October', 'November', 'December']

#type your code below

while True:
  a = input("Release month: ")
  if a in months_of_the_year:
    break
  print("Invalid month!")
print(f"The following games have a release date in {a.title()}...")
for i in games:
  if a in games[i]:
    print(i)
import random
random.seed(1)

print("Game of Scrambles!")
print("------------------")
print()

word_list = ['python', 'dinosaur', 'jumble', 'kangaroo', 'pumpkin'] 

# Write your solution below this line

def ScrambleWord(word):
   word = list(word)
   random.shuffle(word)
   return ''.join(word)

i=0
score = 0
for i in range(5):
   scrambledword = ScrambleWord(word_list[i])
   print(f"Scrambled word {i+1}: " + scrambledword)
   guess = input("Your guess: ")
   if guess.lower() == word_list[i]:
      score+=1
print()
print(f"Your final score is: {score} out of 5!")
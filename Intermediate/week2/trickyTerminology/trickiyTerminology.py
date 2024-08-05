#Create a list of hard words to check against
#in the complexity_check() function
hard_words = ["hippopotamus", "exaggerate", "dilemma", "they're", "zucchini", "should've",
              "could've", "camouflage", "unbelievable", "chameleon", "pharaoh", "entrepreneur",
              "vocabulary", "chrysanthemum", "surreptitious", "millennium", "necessary", "who's",
              "phenomenal", "ubiquitous"]

#Define a function to determine the complexity category
#with the word's complexity score as a parameter
def complexity_category(score):
  if score == 2:
    return "formidable"
  elif score == 1:
    return "tricky"
  else:
    return "breezy"

#Define a function to score a word's complexity
#with a word as the required parameter
def complexity_check(word):
  score = 0
  if len(word) > 7:
     score += 1
  # Write the rest of the complexity_check function here.
  if "'" in word:
    score += 1 
  if word in hard_words:
      return 2
  return score
# Ask the user to input a list of words separated by a space
# and then split the words into a list
b = []
print("Enter a list of words separated by a space")
a = input("Word list: ")
b = a.split()
for i in b:
  print(f"{i}: {complexity_category(complexity_check(i))}")
  
# Loop through the words list, calling the complexity_check function
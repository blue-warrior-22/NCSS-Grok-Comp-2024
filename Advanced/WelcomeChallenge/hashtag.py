# Write your hashtag function here.
def hashtag(words):
    words = words.title()
    words = words.replace(" ", "")
    print(f"#{words}")

# The following allows you to call and test your function, 
# using the provided examples. Make sure you comment them 
# out before marking.

# Run your `hashtag` function with the first example in the question.
msg = hashtag('Hello world')
print(msg)
  
# Run your `hashtag` function with the second example in the question.
msg = hashtag('Putting the FUN in FUNCTIONS')
print(msg)
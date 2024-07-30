# Write your hashtag function here.
def hashtag(words):
    word = words.title()
    worda = word.replace(" ", "")
    wordb = "#"+worda
    return wordb
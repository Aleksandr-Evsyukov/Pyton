from textblob import TextBlob

def pluralize(word, count):
    if count == 1:
        return word
    else:
        blob = TextBlob(word)
        return blob.words[0].pluralize()

print(pluralize('mouse', 1))
print(pluralize('mouse', 9))
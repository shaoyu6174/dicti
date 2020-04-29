import spacy

with open("freqlist.txt") as f:
    freqlist = f.read().splitlines()
with open("text.txt") as f:
    text = f.read()

nlp = spacy.load('en')
doc = nlp(text)
wordlist = []
for token in doc:
    if token.lemma_.lower() not in wordlist and token.lemma_.lower() not in freqlist:
        wordlist.append(token.lemma_.lower())

with open("input.txt", 'w') as f:
    for word in wordlist:
        if word.isalpha():
            f.write(word)
            f.write("\n")
    

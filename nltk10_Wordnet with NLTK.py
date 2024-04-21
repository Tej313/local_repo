# Import the WordNet corpus from NLTK
from nltk.corpus import wordnet

# Import WordNet corpus again (repeated import, unnecessary)
from nltk.corpus import wordnet

# Get the synsets (sets of synonyms) for the word "program"
syns = wordnet.synsets("program")

# Print the name of the first synset
print(syns[0].name())

# Print the name of the first lemma of the first synset
print(syns[0].lemmas()[0].name())

# Print the definition of the first synset
print(syns[0].definition())

# Print examples of usage for the first synset
print(syns[0].examples())

# Initialize empty lists for synonyms and antonyms
synonyms = []
antonyms = []

# Iterate over synsets of the word "good" in WordNet
for syn in wordnet.synsets("good"):
    # Iterate over lemmas in each synset
    for l in syn.lemmas():
        # Add synonyms to the synonyms list
        synonyms.append(l.name())
        # If antonyms exist, add them to the antonyms list
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

# Print the set of synonyms
print(set(synonyms))

# Print the set of antonyms
print(set(antonyms))

# Get WordNet synsets for the words "ship" and "boat"
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')

# Calculate the Wu-Palmer similarity between w1 and w2
print(w1.wup_similarity(w2))  # Output: 0.9090909090909091

# Get WordNet synsets for the words "ship" and "car"
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')

# Calculate the Wu-Palmer similarity between w1 and w2
print(w1.wup_similarity(w2))  # Output: 0.6956521739130435

# Get WordNet synsets for the words "ship" and "cat"
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')

# Calculate the Wu-Palmer similarity between w1 and w2
print(w1.wup_similarity(w2))

import nltk
from nltk.corpus import wordnet

synset = wordnet.synsets("say", pos='v')

print(synset[0].name())
print(synset[0].definition())
print(synset[0].lemmas())

    
   

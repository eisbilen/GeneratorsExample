import json
import spacy
import io

import numpy as np

from spacy.lang.en import English # updated
from spacy.lang.en.stop_words import STOP_WORDS

import textwrap

import spacy
from spacy import displacy
import en_core_web_sm

import spacy
from collections import Counter


from matplotlib.pyplot import plot, title, xlabel, ylabel, savefig, legend
from numpy import array
import matplotlib.pyplot as plt



# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en")

text_file = io.open('/Users/erdemisbilen/Angular/TRTWorld/articlesTXT/article_all.txt', 'r', encoding='utf-8')
my_doc = nlp(text_file.read())
text_file.close()


# all tokens that arent stop words or punctuations
words = [token.text for token in my_doc if token.is_stop != True and token.is_punct != True]

# noun tokens that arent stop words or punctuations
nouns = [token.text for token in my_doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]

# noun tokens that arent stop words or punctuations
verbs = [token.text for token in my_doc if token.is_stop != True and token.is_punct != True and token.pos_ == "VERB"]

# noun tokens that arent stop words or punctuations
dets = [token.text for token in my_doc if token.is_stop != True and token.is_punct != True and token.pos_ == "ADV"]


# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(5)
print(common_words)


# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(75)
print(common_nouns)


# five most common noun tokens
verb_freq = Counter(verbs)
common_verbs = verb_freq.most_common(5)
print(common_verbs)


# five most common noun tokens
det_freq = Counter(dets)
common_dets = det_freq.most_common(5)
print(common_dets)





N=5
x = np.arange(N)
width=0.35

noun, n_count = zip(*common_nouns)
verb, v_count = zip(*common_verbs)
det, d_count = zip(*common_dets)



fig, ax = plt.subplots()
ax.plot(noun, n_count, label="noun")
plt.xticks(rotation='vertical')
ax.grid()
ax.legend()

plt.show()







fig, ax = plt.subplots()

#plt1 = ax.bar(x - width/2, n_count, width, label='noun')
plt2 = ax.bar(x - width/2, v_count, width, label='verb')
plt3 = ax.bar(x + width/2, d_count, width, label='det')



ax.set_ylabel('Count')
ax.set_xlabel('Word')

ax.set_title('Word Frequency')

ax.set_xticks(x)
ax.set_xticklabels(zip(verb, det))


ax.legend()




fig.tight_layout()

plt.show()
savefig("word_count_plot.png")




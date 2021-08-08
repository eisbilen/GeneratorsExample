from word_forms.word_forms import get_word_forms
from word_forms.lemmatizer import lemmatize
print(lemmatize("help"))
print(get_word_forms(lemmatize("help"))['n'])

for word in get_word_forms(lemmatize("help"))['n']:
    print(word)
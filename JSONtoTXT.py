import json
import spacy
from spacy.lang.en import English # updated

raw_text = 'Hello, world. Here are two sentences.'
nlp = English()
nlp.add_pipe(nlp.create_pipe('sentencizer')) # updated


def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text


nameIndex = 0

with open('/Users/erdemisbilen/Angular/TRTWorld/articles_less.json') as json_file:
	
	data = json.load(json_file)
			
	for p in data:
			
		
		doc = nlp(article_body)
		sentences = [sent.string.strip() for sent in doc.sents]


		with open("article_" + str(nameIndex) + ".txt", "w") as text_file:
   			
			nameIndex += 1

   			for sentence in sentences:
   				sentence = lemmatize_text(sentence)
   				text_file.write(sentence)
   			
    		text_file.close()


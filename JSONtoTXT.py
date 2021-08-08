# json_to_txt.py 
# Reads news articles from a JSON file
# Splits the content into sentences
# Write each processed sentence into a text file
from __future__ import unicode_literals, print_function
import json
import spacy
import re
import Settings


print(spacy)

# Loads the spaCy small English language model
nlp = spacy.load('en_core_web_md')
json_data = []
 
def remove_special_chars(text):
	bad_chars = ["%", "#", '"', "*"] 
	for i in bad_chars: 
		text = text.replace(i, '')

	line_end = ["\n"] 
	for i in line_end: 
		text = text.replace(i, ' ')
	
	return text

def split_sentences(document):
	sentences = [sent.string.strip() for sent in document.sents]
	return sentences

def article_body_write(line, au):
	print(line)
	doc = nlp(line)
	sentences = split_sentences(doc)
	sentence_index = 0

	for sentence in sentences:
		sentence_index +=1
		print("Sentence #" + str(sentence_index) + "-" * 20)
		print(sentence)
		text_file.write(sentence + '\n')
		json_data.append({
			"sentence": sentence,
			"articel_url": au})

def article_title_write(line, au):
	print("Title" + line[0])
	text_file.write(line[0] + '\n')
 
	json_data.append({
		"sentence": line[0] ,
		"articel_url": au})

with open(Settings.ARTICLE_BODY_JSON_FILE) as json_file:
	data = json.load(json_file)
	
	with open(Settings.ARTICLE_SENTENCES_TXT_FILE, "w") as text_file:
		for p in data:

			article_title = p['article_title']
			article_body = p['article_body']
			article_url = p['article_url']

			article_body = remove_special_chars(article_body)

			article_title_write(article_title, article_url)			
			article_body_write(article_body, article_url)


      
  
	with open(Settings.ARTICLE_SENTENCES_FIRST_JSON_FILE, 'w') as outfile:
		json.dump(json_data, outfile)
        

	text_file.close()
import sqlite3
import json
import Settings
from datetime import datetime
import random
import re
import glob
import os

def extract__(s):
    return re.findall(r'\__(.+?)\__', s)

def extract_(s):
    return re.findall(r'\--(.+?)\--', s)

def extract___(s):
    return re.findall(r'\___(.+?)\___', s)

connection = sqlite3.connect("lingomooAPP.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
questions(question_id INTEGER PRIMARY KEY, article_url TEXT, sentence TEXT, sentence_length INTEGER, difficulty_score FLOAT, missing_word TEXT,
missing_word_pos TEXT, missing_word_definition TEXT, option1 TEXT, option2 TEXT, option3 TEXT, book INTEGER, image_file_name TEXT, missing_word_q INTEGER, correct_order_q INTEGER )"""

cursor.execute(command1)

image_files = glob.glob(Settings.IMAGE_FILES_FIREBASE)

count = 0
for image in image_files:   
    
    path, filename = os.path.split(image)
    
    question_cat = extract__(filename)[0]
    question_word = extract_(filename)[0]
    correct_answer = extract___(filename)[0]
    file_name = filename.split("__")[0] + ".jpg"
    print(file_name)
    print(question_cat)
    print(question_word)
    print(correct_answer)
    
    with open(Settings.ARTICLE_SENTENCES_PROCESSED_JSON_FILE) as json_file:
        data = json.load(json_file)
    
        for p in data:
            if file_name == p['image_file_name']:
                
                count = count + 1
                print(count)
                article_url = p['article_url']       
                sentence = p['sentence']
                sentence_length = p['sentence_length']
                difficulty_score = p['difficulty_score']
                missing_word = question_word
                missing_word_pos = p['missing_word_pos']
                missing_word_definition = p['missing_word_definition']
                image_file_name = file_name.replace(".", "__" + question_cat + "__" +  "--" + question_word + "--" + "___" + str(correct_answer) + "___missing_word_question.")
        
                option1 = p['option1']
                option2 = p['option2']
                option3 = p['option3']
        
                missing_word_q = 0
                correct_order_q = 0
        
                print(sentence)
        
                cursor.execute("INSERT INTO questions (article_url, sentence, sentence_length, difficulty_score, missing_word, missing_word_pos, missing_word_definition, option1, option2, option3, image_file_name, missing_word_q, correct_order_q) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (article_url, sentence, sentence_length, difficulty_score, missing_word, missing_word_pos, missing_word_definition, option1 ,option2, option3, image_file_name, missing_word_q, correct_order_q))
        
                connection.commit()
    
cursor.execute("DELETE FROM questions WHERE rowid NOT IN (SELECT min(rowid) FROM questions GROUP BY image_file_name)")
connection.commit()   

cursor.close()



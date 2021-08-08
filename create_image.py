import textwrap
import random
import Settings
import json
import time
import random

import os

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from datetime import datetime

def filename_generator(question):
    if question:
        suffix = "_question"
    else:
        suffix = "_answer"

    file_name = 'insta_post_' + \
        str(datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")) + suffix + '.jpg'
    return file_name

def random_background_generator():
    background = Image.open('background_' + str(random.randint(1, 2)) + '.jpg')
    return background

def insta_post_generator(text, text_org, sentence, option1, option2, option3, option4, missing_word, missing_word_definition, image_file_name):
    background = random_background_generator()
    background_e = random_background_generator()

    background_a = random_background_generator()
    background_b = random_background_generator()
    
    lingomoo = Image.open('lingomoo.png')
    lingomoo = lingomoo.resize((int(lingomoo.size[0]/2),int(lingomoo.size[1]/2)), 0)

    fnt_body = ImageFont.truetype('Nunito-ExtraBold.ttf', 55)
    fnt_title = ImageFont.truetype('Nunito-ExtraBold.ttf', 60)

    d = ImageDraw.Draw(background) #question for missing word
    e = ImageDraw.Draw(background_e) #question for order 
    
    a = ImageDraw.Draw(background_a) #answer for missing word question
    b = ImageDraw.Draw(background_b) #answer for order question

    #FIRST LINE QUESTION
    d.text((50, 10), "Find the Missing Word!",
           font=fnt_title, fill=(255, 140, 0))
    e.text((50, 10), "Put the Words in the Correct Order",
           font=fnt_title, fill=(255, 140, 0))
    
    #FIRST LINE ANSWER
    a.text((50, 10), "Correct Answer: " ,
           font=fnt_title, fill=(255, 140, 0))
    a.text((550, 10), missing_word,
           font=fnt_title, fill=(0, 115, 255))      
    
    b.text((50, 10), "Correct Answer: " ,
           font=fnt_title, fill=(255, 140, 0))


    #SECOND LINE QUESTION
    d.text((50, 30), "_________________________________",
           font=fnt_title, fill=(255, 140, 0))
    e.text((50, 30), "_________________________________",
           font=fnt_title, fill=(255, 140, 0))
        
    #SECOND LINE ANSWER
    a.text((50, 30), "_________________________________",
           font=fnt_title, fill=(255, 140, 0))
    b.text((50, 30), "_________________________________",
           font=fnt_title, fill=(255, 140, 0))
    
    text_keep_org = text_org
    text_org = text_org.split()
    random.shuffle(text_org)
    separator = ' '
    unordered_text = separator.join(text_org)
    print(unordered_text)

    lines = textwrap.wrap(text, width=35)
    y_text = 100
    for line in lines:
        d.text((50, y_text), line, font=fnt_body, fill=(0, 115, 255))
        a.text((50, y_text), line, font=fnt_body, fill=(0, 115, 255))
        y_text += 50

    lines = textwrap.wrap(unordered_text, width=35)
    y_text = 150
    for line in lines:
        e.text((50, y_text), line, font=fnt_title, fill=(0, 115, 255))
        y_text += 50
        
    lines = textwrap.wrap(text_keep_org, width=35)
    y_text = 150
    for line in lines:
        b.text((50, y_text), line, font=fnt_title, fill=(0, 115, 255))
        y_text += 50
        
              
    d.text((150, 300), option1, font=fnt_body, fill=(0, 115, 255))
    d.text((150, 400), option2, font=fnt_body, fill=(0, 115, 255))
    d.text((150, 500), option3, font=fnt_body, fill=(0, 115, 255))
    d.text((150, 600), option4, font=fnt_body, fill=(0, 115, 255))

    d.text((50, 300), "(A)", font=fnt_body, fill=(255, 140, 0))
    d.text((50, 400), "(B)", font=fnt_body, fill=(255, 140, 0))
    d.text((50, 500), "(C)", font=fnt_body, fill=(255, 140, 0))
    d.text((50, 600), "(D)", font=fnt_body, fill=(255, 140, 0))
    
    background.paste(lingomoo, (850, 1000), lingomoo)
    background_e.paste(lingomoo, (850, 1000), lingomoo)

    background.save('/Users/erdemisbilen/Desktop/deneme/'  + image_file_name.replace(".", "_missing_word_question."), quality=60)
    
    if len(text_org) < 10:
        background_e.save('/Users/erdemisbilen/Desktop/deneme/'  + image_file_name.replace(".", "_correct_order_question."), quality=60)
        background_b.save('/Users/erdemisbilen/Desktop/deneme/'  + image_file_name.replace(".", "_correct_order_answer."), quality=60)
   
    a.text((250, 300), option1, font=fnt_body, fill=(0, 115, 255))
    a.text((250, 400), option2, font=fnt_body, fill=(0, 115, 255))
    a.text((250, 500), option3, font=fnt_body, fill=(0, 115, 255))
    a.text((250, 600), option4, font=fnt_body, fill=(0, 115, 255))

    a.text((150, 300), "(A)", font=fnt_body, fill=(255, 140, 0))
    a.text((150, 400), "(B)", font=fnt_body, fill=(255, 140, 0))
    a.text((150, 500), "(C)", font=fnt_body, fill=(255, 140, 0))
    a.text((150, 600), "(D)", font=fnt_body, fill=(255, 140, 0))
    
    tick =Image.open('correct.png')
    if option1==missing_word:
        background_a.paste(tick, (50, 300), tick)
    if option2==missing_word:
        background_a.paste(tick, (50, 400), tick)
    if option3==missing_word:
        background_a.paste(tick, (50, 500), tick)
    if option4==missing_word:
        background_a.paste(tick, (50, 600), tick)

    a.text((50, 780), "Meaning of '" + missing_word+ "':",
           font=fnt_title, fill=(0, 115, 255))   
    
    lines = textwrap.wrap(missing_word_definition, width=35)
    y_text = 840
    for line in lines:
        a.text((50, y_text), line, font=fnt_body, fill=(255, 140, 0))
        y_text += 50

    background_a.paste(lingomoo, (850, 1000), lingomoo)
    background_a.save('/Users/erdemisbilen/Desktop/deneme/'  +  image_file_name.replace(".", "_missing_word_answer.") , quality=60)

with open(Settings.ARTICLE_SENTENCES_PROCESSED_JSON_FILE) as json_file:
    data = json.load(json_file)

    for p in data:

        text_org = p['sentence']
        sentence = p['sentence']
        missing_word = p['missing_word']
        missing_word_definition = p['missing_word_definition']
        image_file_name = p['image_file_name']
                
        print(missing_word)
        print(text_org)
        text = text_org.replace(str(missing_word), "_____")

        answers = list()
        answers.append(missing_word)
        answers.append(p['option1'])
        answers.append(p['option2'])
        answers.append(p['option3'])
        
        random.shuffle(answers)

        insta_post_generator(text, text_org, sentence, answers[0], answers[1], answers[2], answers[3], missing_word, missing_word_definition, image_file_name)
        time.sleep(1)

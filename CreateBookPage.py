import json
import Settings
from datetime import datetime
import random
import re
import glob
import os
import textwrap
import random
import time

from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def extract__(s):
    return re.findall(r'\__(.+?)\__', s)

def extract_(s):
    return re.findall(r'\--(.+?)\--', s)

def extract___(s):
    return re.findall(r'\___(.+?)\___', s)

def background_generator():
    background = Image.open('background_blue_2535_3810_verbs.jpg')           
    #lingomoo_icon = Image.open('lingomoo.png')
    #lingomoo_icon = lingomoo_icon.resize((int(lingomoo_icon.size[0]/2),int(lingomoo_icon.size[1]/2)), 0)
    #background.paste(lingomoo_icon, (850, 1000), lingomoo_icon)
    img = ImageDraw.Draw(background) 
    return img, background

tests = ["Test1","Test2","Test3","Test4","Test5","Test6","Test7","Test8","Test9","Test10","Test11","Test12","Test13","Test14","Test15","Test16","Test17","Test18","Test19","Test20"]
answer_key = dict()


for test in tests:

    count = 0
    x = 0
    y = 0
    x_add = 20
    y_add = 365
    page=1
    
    answers = list()
    
  
    img, background = background_generator()
    white_bg_img = Image.open('background_white_2535_3280.jpg')
    rect = Image.open('rect_blue.jpg')
    line = Image.open('line_blue.jpg')  
    rect_vertical = Image.open('rect_vertical_blue.jpg')  

    background.paste(white_bg_img , (0, 375))
    
    image_files = glob.glob(Settings.IMAGE_FILES_FOR_BOOK + test +"/" + "*.jpg")
    print(test)
    print(image_files)
    
    for image in image_files:   
        count += 1

        path, filename = os.path.split(image)
    
        question_cat = extract__(filename)[0]
        question_word = extract_(filename)[0]
        correct_answer = extract___(filename)[0]
        file_name = filename.split("__")[0] + ".jpg"
        
        print(correct_answer)
        
        if int(correct_answer) == 0:
            answer = "A"
        if int(correct_answer) == 1:
            answer = "B"           
        if int(correct_answer) == 2:
            answer = "C"
        if int(correct_answer) == 3:
            answer = "D"
        
        answer = str(count ) + "-" + answer         
        answers.append(answer)
    
        question_img = Image.open(image)
        
        question_img = question_img.resize((int(question_img.size[0]/1),int(question_img.size[1]/1)), 0)
        background.paste(question_img, (y, x+375))

        background.paste(rect, (y, x+380))
        background.paste(rect_vertical, (1250, 375))
        
        if count!=1 and count!=6 and count!=11 and count!=16:
            background.paste(line, (y, x+370))
        
        img.text((y+50, x+375), str(count) + '.', font=Settings.FONT_BODY, fill=(255, 140, 0))
        img.text((20, 3680), "Book 1 / " + str(test), font=Settings.FONT_FOOTER, fill=(255, 255, 255))
          
        if count!=5 or count!=15:
            x = x + 640 + x_add
        if count==5 or count==15:
            x = 0
            y = y + 1080 + y_add
    
        if count==10:
            background.save(Settings.IMAGE_FILES_FOR_BOOK+test+'-page1.jpg'  , quality=60)
            x=0
            y=0
            img, background = background_generator()
            background.paste(white_bg_img , (0, 375))

    
        if count==20:
            background.save(Settings.IMAGE_FILES_FOR_BOOK+test+'-page2.jpg'  , quality=60)
            answer_key[test] = answers


            break
    
        print(file_name)
        print(question_cat)
        print(question_word)
        print(correct_answer)

with open('answer_key.txt', 'w') as file:
     file.write(json.dumps(answer_key))
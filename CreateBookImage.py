import textwrap
import random
import Settings
import json
import time
import random
import os
import re 

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from datetime import datetime

class CreateImage:
    """ This class generates question/answer Image Sets """
    
    # Initializer / Instance Attributes
    def __init__(self, question_type, question_category, text, text_org, answer_options, missing_word, missing_word_definition, image_file_name):
        self.question_type = question_type
        self.question_category = question_category
        self.text = text
        self.text_org = text_org

        self.option1 = answer_options[0]
        self.option2 = answer_options[1]
        self.option3 = answer_options[2]
        self.option4 = answer_options[3]
        self.missing_word = missing_word
        self.missing_word_definition = missing_word_definition
        self.image_file_name = image_file_name
        self.img, self.save_image = self.random_background_generator()

    def filename_generator(self, question):
        if question:
            suffix = "_question"
        else:
            suffix = "_answer"

        file_name = 'insta_post_' + \
            str(datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")) + suffix + '.jpg'
        return file_name
    
    @staticmethod
    def random_background_generator():
        background = Image.open('background_' + str(random.randint(1, 2)) + '_1.jpg')           
        #lingomoo_icon = Image.open('lingomoo.png')
        #lingomoo_icon = lingomoo_icon.resize((int(lingomoo_icon.size[0]/2),int(lingomoo_icon.size[1]/2)), 0)
        #background.paste(lingomoo_icon, (850, 1000), lingomoo_icon)
        img = ImageDraw.Draw(background) 
        
        return img, background
    
    def option_lines(self, question_or_answer):
        if self.question_type=="missing_word":
            self.img.text((150, 250), self.option1, font=Settings.FONT_BODY, fill=(0, 115, 255))
            self.img.text((150, 350), self.option2, font=Settings.FONT_BODY, fill=(0, 115, 255))
            self.img.text((150, 450), self.option3, font=Settings.FONT_BODY, fill=(0, 115, 255))
            self.img.text((150, 550), self.option4, font=Settings.FONT_BODY, fill=(0, 115, 255))

            self.img.text((50, 250), "(A)", font=Settings.FONT_BODY, fill=(255, 140, 0))
            self.img.text((50, 350), "(B)", font=Settings.FONT_BODY, fill=(255, 140, 0))
            self.img.text((50, 450), "(C)", font=Settings.FONT_BODY, fill=(255, 140, 0))
            self.img.text((50, 550), "(D)", font=Settings.FONT_BODY, fill=(255, 140, 0))
        
        if question_or_answer=="answer":
            tick = Image.open('correct.png')     
            if self.option1==self.missing_word:
                self.save_image.paste(tick, (50, 350), tick)
            if self.option2==self.missing_word:
                self.save_image.paste(tick, (50, 450), tick)
            if self.option3==self.missing_word:
                self.save_image.paste(tick, (50, 550), tick)
            if self.option4==self.missing_word:
                 self.save_image.paste(tick, (50, 650), tick)
            
        return self.img
    
    def first_line(self, question_or_answer):
        if question_or_answer == "question":
            self.img.text((50, 10), Settings.FIRST_LINE[self.question_type], 
                font=Settings.FONT_TITLE, fill=(255, 140, 0))
            
            #rect_20 = Image.open('rect20.png')
            #self.save_image.paste(rect_20, (50, 990), rect_20)
        
            #self.img.text((90, 1000), self.question_category, 
            #    font=Settings.FONT_CAT, fill=(0, 115, 255))       
    
        if question_or_answer == "answer":
            self.img.text((50, 10), "Correct Answer: " ,
                font=Settings.FONT_TITLE, fill=(255, 140, 0))
            self.img.text((550, 10), self.missing_word,
                font=Settings.FONT_TITLE, fill=(0, 115, 255)) 
    
        self.img.text((50, 30), "_________________________________",
            font=Settings.FONT_TITLE, fill=(255, 140, 0))
                
        return self.img
    
    def question_or_answer_line(self, question_or_answer):
        text_keep_org = self.text_org
        
        self.text_org = self.text_org.split()
        random.shuffle(self.text_org)
        separator = ' '
        unordered_text = separator.join(self.text_org)
        
        if question_or_answer == "answer":
            if self.question_type == "correct_order":
                self.text = text_keep_org
            if self.question_type == "missing_word":
                self.text = text_keep_org
            
        else:
            if self.question_type == "correct_order":
                self.text = unordered_text
            
        lines = textwrap.wrap(self.text, width=30)
        y_text = 10
        for line in lines:
            self.img.text((150, y_text ), line, font = Settings.FONT_BODY, fill=(0, 115, 255))
            y_text += 50
        
        return self.img
    
    def meaning_text_line(self):
        self.img.text((50, 780), "Meaning of '" + self.missing_word + "':",
            font=Settings.FONT_TITLE, fill=(0, 115, 255)) 
        lines = textwrap.wrap(self.missing_word_definition, width=35)
        y_text = 840
        
        for line in lines:
            self.img.text((50, y_text), line, font = Settings.FONT_BODY, fill=(255, 140, 0))
            y_text += 50
        return self.img
    
    def question_generator(self, correct_answer):
        #self.img = self.first_line("question")
        self.img = self.question_or_answer_line( "question")
        self.img = self.option_lines("question")
        self.save_image.save('/Users/erdemisbilen/Desktop/deneme/'  +  self.image_file_name.replace(".", "__" + self.question_category + "__" +  "--" + self.missing_word + "--" + "___" + str(correct_answer) + "___missing_word_question.") , quality=100)
    
    def answer_generator(self, correct_answer):
        self.img = self.first_line("answer")
        self.img = self.question_or_answer_line( "answer")
        self.img = self.option_lines("answer")
        #self.img = self.meaning_text_line()
        self.save_image.save('/Users/erdemisbilen/Desktop/deneme/'  +  self.image_file_name.replace(".", "__" + self.question_category + "__" + "--" + self.missing_word + "--" + "___" + str(correct_answer) + "___missing_word_answer.")  , quality=100)
                     
if __name__ == "__main__" :
    
    with open(Settings.ARTICLE_SENTENCES_PROCESSED_JSON_FILE) as json_file:
        data = json.load(json_file)

        for p in data:

            text_org = p['sentence']
            sentence = p['sentence']
            missing_word = p['missing_word']
            missing_word_definition = p['missing_word_definition']
            image_file_name = p['image_file_name']
            words = p['linguistic_features']    

            answers = list()
            answers.append(missing_word)
            answers.append(p['option1'])
            answers.append(p['option2'])
            answers.append(p['option3'])
            
            random.shuffle(answers)
            
            #image = CreateImage("missing_word", "VOCABULARY-ADJECTIVES", text, text_org, answers, missing_word, missing_word_definition, image_file_name)
            #image.question_generator()
            
            for question_cat in Settings.QUESTION_CAT_LIST:
                question = p[question_cat]
      
                if len(question) > 1:
                    
                    for question in question[0]:
                        answers = []
                        text_adj = []
                        missing_word = question["base"]

                        for word in words:   
                         
                            word['word'] = word['word'].translate(".,!)(?")
                            
                            if word['word'] == missing_word:
                                text_adj.append("____")
                            else:
                                text_adj.append(word['word'])
                        
                        text = ' '.join(map(str, text_adj))
                          
                        #text = text_org.replace(str(missing_word), "_____")
                        
                        answers.append(question["base"])
                        answers.append(question["option1"])
                        answers.append(question["option2"])
                        answers.append(question["option3"])              
                        random.shuffle(answers)
                        
                        for i, answer in enumerate(answers):
                            if answer == missing_word:
                                correct_answer = i
                            
                        print (answers)
                        image = CreateImage("missing_word", question_cat.upper(), text, text_org, answers, missing_word, missing_word_definition, image_file_name)
                        image.question_generator(correct_answer)
                      
                        #image_a = CreateImage("missing_word", question_cat.upper(), text, text_org, answers, missing_word, missing_word_definition, image_file_name)
                        #image_a.answer_generator(correct_answer)

            time.sleep(1)
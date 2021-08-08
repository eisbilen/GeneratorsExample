
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ARTICLE_BODY_JSON_FILE = "/Users/erdemisbilen/Angular/TRTWorld/article_body.json"
ARTICLE_SENTENCES_TXT_FILE = "/Users/erdemisbilen/Angular/TRTWorld/article_body.txt"
ARTICLE_SENTENCES_FIRST_JSON_FILE = "/Users/erdemisbilen/Language/article_first_json.json"
ARTICLE_SENTENCES_PROCESSED_JSON_FILE = "/Users/erdemisbilen/Language/article_simple.json"
IMAGE_FILES_FOR_BOOK = "/Users/erdemisbilen/Desktop/Book_Images/"
IMAGE_FILES_FIREBASE = "/Users/erdemisbilen/Desktop/deneme/*.jpg"

QUESTION_CAT_LIST = ["preposition", "adverb_particle", "coordinating_conjuction", "modal", "possesive_pronoun", "predeterminer", "wh_determiner", "determiner", "adverb", "adjective", "verb" ]

FIRST_LINE = {
    "missing_word": "Find the Missing Word !",
    "correct_order": "Put the Words in the Correct Order"
}

Y_TEXT= {
    "missing_word_question": 100,
    "correct_order_question": 150
}

FONT_BODY = ImageFont.truetype('Nunito-ExtraBold.ttf', 55)
FONT_TITLE = ImageFont.truetype('Nunito-ExtraBold.ttf', 60)
FONT_CAT = ImageFont.truetype('Nunito-ExtraBoldItalic.ttf', 40) 
FONT_FOOTER = ImageFont.truetype('Roboto-Thin.ttf', 80)   
import sqlite3
import json
import Settings

import textwrap
import random
import Settings
import json
import time
import random

import os

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from datetime import datetime

import glob
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyD5b16Ejf5wxsaswc8qIaTBXJTLW7xp8Oc",
    "authDomain": "lingomoo.firebaseapp.com",
    "databaseURL": "https://lingomoo.firebaseio.com",
    "projectId": "lingomoo",
    "storageBucket": "lingomoo.appspot.com",
    "messagingSenderId": "886228262297",
    "appId": "1:886228262297:web:4f391f1d1b68d595974708"}

firebase = pyrebase.initialize_app(firebaseConfig)


image_files = glob.glob(Settings.IMAGE_FILES_FIREBASE)


for images in image_files:

    
    
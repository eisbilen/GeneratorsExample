import random
import spacy

from spacy.lang.en import English # updated
from spacy.vectors import Vectors

from word_forms.word_forms import get_word_forms
from word_forms.lemmatizer import lemmatize

BASE_DICT = {
    "ADVERB_PARTICLE": ["above", "about", "in", "out", "up", "down", "off", "before", "accros", "below", "behind" ],          
    "CONJUCTION" : ["and","as","because","but","for","just as","or","neither","either","nor","not only","so","whether","yet"],
    "PREPOSITION" : ["aboard","about","above","across","after","against","along","amid","among","anti",
                      "around","as","at","before","behind","below","beneath","beside","besides","between",
                      "beyond","but","by","despite","as","down","during","except","following","for","from",
                      "in","inside","into","like","near","of","off","on","onto","opposite","outside","over","past","per","as",
                      "regarding","round","since","than","through","to","toward","towards","under","unlike","until","up",
                      "upon","versus","via","with","within","without"],
    "MODAL": ["can", "may", "must", "shall", "will", "could", "might", "should", "would" ],
    "PERSONAL_PRONOUN": ["I", "you", "he", "she", "it", "we", "they" ],
    "POSSESIVE_PRONOUN": ["mine", "yours", "his", "hers", "its", "ours", "theirs" ], 
    "PREDETERMINER": ["rather", "quite", "such", "what", "all", "both", "twice", "half" ],
    "WH-DETERMINER": ["what", "which", "such", "where", "why", "when"],
    "DETERMINER": ["the", "an", "what", "which", "such", "where", "why", "when", "rather", "quite", "all", "both", "twice", "half"],
    "ADVERB": ["the", "an", "what", "which", "such", "where", "why", "when", "rather", "quite", "all", "both", "twice", "half"],
}

class AddOptions:
    """ This class generates answer options """
    
    # Initializer / Instance Attributes
    def __init__(self, tag, question):
        self.tag = tag
        self.question = question
 
    # Instance Method
    def add_options(self):
        question_temp = BASE_DICT[self.tag]
        question_options = []
        
        for item in self.question:
            question_option = {}
            
            #If there is any Capital letter in options, dont consider it
            print(item)
            if any(x.isupper() for x in item[self.tag]):
                break
            
            n = [x for x in question_temp if x != item[self.tag]]
       
            question_option["base"] = item[self.tag]           
            question_option["option1"] = random.choice(n)
            n.remove(question_option["option1"])          
            question_option["option2"] = random.choice(n)
            n.remove(question_option["option2"])         
            question_option["option3"] = random.choice(n)
            
            question_options.append(question_option)
            
        return question_options
    
    def add_options_vocab(self, nlp, vaa):
        
        question_options = []
        
        vaa_options = []
        vaa_options.append("")
        vaa_options.append("")
        vaa_options.append("")
        
        if vaa == "r":
            vaa_options[0]="n"
            vaa_options[1]="a"
            vaa_options[2]="v"
        if vaa == "a":
            vaa_options[0]="n"
            vaa_options[1]="r"
            vaa_options[2]="v"
        if vaa == "v":
            vaa_options[0]="n"
            vaa_options[1]="r"
            vaa_options[2]="a"
        
        for item in self.question:
            print(item)
            question_option = {}
            
            if any(x.isupper() for x in item[self.tag]):
                break
            
            w_id = nlp.vocab.strings[item[self.tag]]
            w_vector = nlp.vocab.vectors[w_id]
            most_similar = nlp.vocab.vectors.most_similar(w_vector.reshape(1,300), n=60)

            question_option["base"] = item[self.tag]        
            question_option["option1"] = nlp.vocab.strings[most_similar[0][0][random.choice(range(10,20))]].lower()
            question_option["option2"] = nlp.vocab.strings[most_similar[0][0][random.choice(range(21,30))]].lower()
            question_option["option3"] = nlp.vocab.strings[most_similar[0][0][random.choice(range(31,40))]].lower()
            
            for word in get_word_forms(lemmatize(item[self.tag]))[vaa_options[0]]:
                if word != item[self.tag]:
                    question_option["option1"] =  word 
            
            for word in get_word_forms(lemmatize(item[self.tag]))[vaa_options[1]]:
                if word != item[self.tag]:
                    question_option["option2"] =  word      
            
            for word in get_word_forms(lemmatize(item[self.tag]))[vaa_options[2]]:
                if word != item[self.tag]:
                    question_option["option3"] =  word
                     
            question_options.append(question_option)
            print(question_options)
        
        return question_options
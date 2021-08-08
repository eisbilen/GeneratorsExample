import json
import spacy
import textstat
import random

import Settings
from AddOptions import AddOptions

from spacy.tokenizer import Tokenizer
from spacy.lang.en import English  # updated
from spacy.lang.en.stop_words import STOP_WORDS

from spacy.vectors import Vectors

from spacy.matcher import Matcher
from spacy.tokens import Span

from collections import Counter
import re

import nltk
from nltk.corpus import wordnet


from datetime import datetime
import time


PARENT_DIR = "/Users/erdemisbilen/Language/"
INPUT_FILE_NAME = "sports_article_all.txt"
OUTPUT_FILE_NAME = "sports_article_simple_test.txt"

EASY_MIN_SENTENCE_LENGTH = 6
EASY_MAX_SENTENCE_LENGTH = 15

MODARATE_MIN_SENTENCE_LENGTH = 10
MODARATE_MAX_SENTENCE_LENGTH = 16

DIFFICULT_MIN_SENTENCE_LENGTH = 17
DIFFICULT_MAX_SENTENCE_LENGTH = 22

RANDOM_LIST = [0, 1]

LONG_WORDS_LIMIT = 5
POLYSYLLABIC_WORDS_LIMIT = 4

json_data = []
linguistic_features = []
named_entities = []

similar_words = []
missing_word = ""
option1 = ""
option2 = ""


def filename_generator():
    file_name = '' + \
        str(datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")) + '.jpg'
    return file_name


def calculate_sentence_length(words):
    return (len(words))


def calculate_word_character_length_mavrg(words):
    total_char = 0
    for word in words:
        total_char += len(word)
    return (round(total_char/len(words), 1))


def calculate_number_of_long_words(words):
    total_long_word = 0
    for word in words:
        if len(word) > LONG_WORDS_LIMIT:
            total_long_word += 1
    return (total_long_word)


def calculate_number_of_polysyllabic_words(words):
    total_polysyllabic_words = 0
    for word in words:
        if len(word) > POLYSYLLABIC_WORDS_LIMIT:
            total_polysyllabic_words += 1
    return (total_polysyllabic_words)


def define_question_mark(words):
    question_mark = 0
    for word in words:
        if "?" in word:
            question_mark = 1
    return (question_mark)

def simple_tokenization(line):
    sentence_length = 0
    linguistic_features = []
    tokenizer = Tokenizer(nlp.vocab)
    toks = tokenizer(line)

    for token in toks:
        print(token.text)

        if not "\n" in token.text:
            sentence_length += 1
            linguistic_features.append({'word': token.text})

    return(linguistic_features, sentence_length)

def define_missing_word(my_doc):
    missing_word = ""
    option1 = ""
    option2 = ""
    option3 = ""
    missing_word_pos = ""

    for token in my_doc:
        if token.is_punct != True and token.is_alpha == True:

            if (token.pos_ == "VERB" or token.pos_ == "ADJ" or token.pos_ == "ADV") and (random.choice(RANDOM_LIST) == 1 or missing_word == ""):
                w_id = nlp.vocab.strings[token.text]
                w_vector = nlp.vocab.vectors[w_id]
                most_similar = nlp.vocab.vectors.most_similar(
                    w_vector.reshape(1, 300), n=25)
                missing_word = token.text
                missing_word_pos = token.pos_
                option1 = nlp.vocab.strings[most_similar[0][0][9]].lower()
                option2 = nlp.vocab.strings[most_similar[0][0][18]].lower()
                option3 = nlp.vocab.strings[most_similar[0][0][24]].lower()

    return(missing_word, missing_word_pos, option1, option2, option3)

def define_named_entities(my_doc):
    named_entities = []
    for ent in my_doc.ents:
        named_entities.append({
            'entity': ent.text,
            'entity_label': ent.label_})
    return(named_entities)

def write_linguistic_features(matches_single):
    lf_dict = {}
    lf_list = []
    for match_id, start, end in matches_single:
        lf_dict = {}
        # Get the string representation
        string_id = nlp.vocab.strings[match_id]
        span = my_doc[start:end]  # The matched span
        lf_dict[string_id] = span.text
        lf_list.append(lf_dict)
        print(match_id, string_id, start, end, span.text)
    return lf_list

# Loads the spaCy small English language model
nlp = spacy.load('en_core_web_lg')

matcher_wh_determiner = Matcher(nlp.vocab)
matcher_determiner = Matcher(nlp.vocab)
matcher_predeterminer = Matcher(nlp.vocab)

matcher_verb = Matcher(nlp.vocab)
matcher_adverb = Matcher(nlp.vocab)
matcher_adjective = Matcher(nlp.vocab)

matcher_passive = Matcher(nlp.vocab)
matcher_conjuction = Matcher(nlp.vocab)
matcher_subject = Matcher(nlp.vocab)
matcher_object = Matcher(nlp.vocab)

matcher_future_tense = Matcher(nlp.vocab)

matcher_present_continuous_tense = Matcher(nlp.vocab)
matcher_present_perfect_tense = Matcher(nlp.vocab)
matcher_present_perfect_continuous_tense = Matcher(nlp.vocab)

matcher_simple_past_tense = Matcher(nlp.vocab)
matcher_simple_present_tense = Matcher(nlp.vocab)

matcher_possesive_ending = Matcher(nlp.vocab)
matcher_possesive_pronoun = Matcher(nlp.vocab)

matcher_prepositions_sub_conj = Matcher(nlp.vocab)
matcher_adverb_particle = Matcher(nlp.vocab)

matcher_comparative_adjective = Matcher(nlp.vocab)
matcher_superlative_adjective = Matcher(nlp.vocab)

matcher_comparative_adverb = Matcher(nlp.vocab)
matcher_superlative_adverb = Matcher(nlp.vocab)

matcher_modals = Matcher(nlp.vocab)
matcher_there_is_are = Matcher(nlp.vocab)
matcher_to_infinitive = Matcher(nlp.vocab)
matcher_gerunds = Matcher(nlp.vocab)

# Coordinating Conjunctions
determiner_rule_1 = [{'POS': 'DET'}]
wh_determiner_rule_1 = [{'TAG': 'WDT'}]
predeterminer_rule_1 = [{'TAG': 'PDT'}]

verb_rule_1 = [{'TAG': 'VBN'}]
verb_rule_2 = [{'TAG': 'VB'}]
verb_rule_3 = [{'TAG': 'VBZ'}]
verb_rule_4 = [{'TAG': 'VBP'}]

adverb_rule_1 = [{'POS': 'ADV'}]
adjective_rule_1 = [{'POS': 'ADJ'}]

conjuction_rule_1 = [{'TAG': 'CC'}]
prepositions_sub_conj_rule_1 = [{'TAG': 'IN'}]
adverb_particle_rule_1 = [{'TAG': 'RP'}]

comparative_adjective_rule_1 = [{'TAG': 'JJR'}]
superlative_adjective_rule_1 = [{'TAG': 'JJS'}]

comparative_adverb_rule_1 = [{'TAG': 'RBR'}]
superlative_adverb_rule_1 = [{'TAG': 'RBS'}]

there_is_are_rule_1 = [
    {'TEXT': 'There', 'TEXT': 'there'}, {'TEXT': 'is', 'TEXT': 'are'}]
modals_rule_1 = [{'TAG': 'MD'}]
to_infinitive_rule_1 = [{'TAG': 'TO'}, {'TAG': 'VB'}]
gerunds_rule_1 = [{'TAG': 'VB'}, {'TAG': 'VBG'}]

passive_rule_1 = [{'DEP': 'auxpass'}, {'TAG': 'VBN'}]
subject_rule_1 = [{'DEP': 'csubj'}]
subject_rule_2 = [{'DEP': 'nsubj'}]
object_rule_1 = [{'DEP': 'dobj'}]

# Future Tenses With Auxiliaries
future_tense_rule_1 = [{'TEXT': 'will'}, {'TAG': 'VB'}]
future_tense_rule_2 = [{'TEXT': 'shall'}, {'TAG': 'VB'}]

# Morphological Present Tenses
simple_present_rule_1 = [{'POS': 'PRON'}, {'TAG': 'VBP', 'TAG': 'VBZ'}, {
    'TAG': 'VB', 'TAG': 'VBG', 'TAG': 'VBN', 'OP': '!'}]
present_continuous_rule_1 = [
    {'TAG': 'VBZ', 'DEP': 'aux'}, {'TAG': 'VBG', 'DEP': 'ROOT'}]
present_perfect_rule_1 = [
    {'TAG': 'VBZ', 'DEP': 'aux'}, {'TAG': 'VBN', 'DEP': 'ROOT'}]
present_perfect_continuous_rule_1 = [{'TAG': 'VBZ', 'DEP': 'aux'}, {
    'TAG': 'VBN'}, {'TAG': 'VBN', 'DEP': 'ROOT'}]

# Morphological Past Tenses
simple_past_rule_1 = [{'POS': 'PRON'}, {'TAG': 'VBD'}, {
    'TAG': 'VB', 'TAG': 'VBG', 'TAG': 'VBN', 'OP': '!'}]

# Possessive Endings the boy's ball
possesive_ending_rule_1 = [{'TAG': 'POS'}]

# Possessive Pronoun
possesive_pronoun_rule_1 = [{'TAG': 'PRP$'}]

matcher_determiner.add('DETERMINER', None, determiner_rule_1)
matcher_predeterminer.add('PREDETERMINER', None, predeterminer_rule_1)
matcher_wh_determiner.add('WH-DETERMINER', None, wh_determiner_rule_1)

matcher_verb.add('VERB', None, verb_rule_1)
matcher_verb.add('VERB', None, verb_rule_2)
matcher_verb.add('VERB', None, verb_rule_3)
matcher_verb.add('VERB', None, verb_rule_4)
matcher_adverb.add('ADVERB', None, adverb_rule_1)
matcher_adjective.add('ADJECTIVE', None, adjective_rule_1)

matcher_passive.add('Passive', None, passive_rule_1)
matcher_subject.add('Subject', None, subject_rule_1)
matcher_subject.add('Subject', None, subject_rule_2)
matcher_object.add('Object', None, object_rule_1)
matcher_conjuction.add('CONJUCTION', None, conjuction_rule_1)

matcher_future_tense.add('Future Tense (will)', None, future_tense_rule_1)
matcher_future_tense.add('Future Tense (shall)', None, future_tense_rule_2)

matcher_present_continuous_tense.add(
    'Present Continuous Tense', None, present_continuous_rule_1)
matcher_present_perfect_tense.add(
    'Present Perfect Tense', None, present_perfect_rule_1)
matcher_present_perfect_continuous_tense.add(
    'Present Perfect Continuous Tense', None, present_perfect_continuous_rule_1)

matcher_simple_past_tense.add('Simple Past Tense', None, simple_past_rule_1)

matcher_simple_present_tense.add(
    'Simple Present Tense', None, simple_present_rule_1)
matcher_possesive_ending.add('Possesive Ending', None, possesive_ending_rule_1)
matcher_possesive_pronoun.add(
    'POSSESIVE_PRONOUN', None, possesive_pronoun_rule_1)

matcher_prepositions_sub_conj.add(
    'PREPOSITION', None, prepositions_sub_conj_rule_1)
matcher_adverb_particle.add('ADVERB_PARTICLE', None, adverb_particle_rule_1)

matcher_comparative_adjective.add(
    'Comparative Adjective', None, comparative_adjective_rule_1)
matcher_superlative_adjective.add(
    'Superlative Adjective', None, superlative_adjective_rule_1)

matcher_comparative_adverb.add(
    'Comparative Adverb', None, comparative_adverb_rule_1)
matcher_superlative_adverb.add(
    'Superlative Adverb', None, superlative_adverb_rule_1)

matcher_modals.add('MODAL', None, modals_rule_1)
matcher_there_is_are.add('There is/are', None, there_is_are_rule_1)
matcher_to_infinitive.add('To+Infinitive', None, to_infinitive_rule_1)
matcher_gerunds.add('Gerunds', None, gerunds_rule_1)

# Using readlines()
file = open(Settings.ARTICLE_SENTENCES_TXT_FILE, 'r')
lines = file.readlines()


with open(Settings.ARTICLE_SENTENCES_PROCESSED_JSON_FILE, "w") as text_file:

    with open(Settings.ARTICLE_SENTENCES_FIRST_JSON_FILE) as json_file:
      data = json.load(json_file)

    # Strips the newline character
      for data_line in data:
        line = data_line['sentence']
        linguistic_features = []
        named_entities = []
        my_doc = nlp(line)

        words = [token.text for token in my_doc if token.is_punct !=
                 True and token.is_alpha == True]
        words_all = [token.text for token in my_doc]

        sentence_length = calculate_sentence_length(words)
        matches_subject = matcher_subject(my_doc)

        matches_comparative_adverb = matcher_comparative_adverb(my_doc)
        matches_there_is_are = matcher_there_is_are(my_doc)
        matches_to_infinitive = matcher_to_infinitive(my_doc)
        matches_gerunds = matcher_gerunds(my_doc)

        if sentence_length < EASY_MAX_SENTENCE_LENGTH and sentence_length > EASY_MIN_SENTENCE_LENGTH:
            word_character_length_mavrg = calculate_word_character_length_mavrg(
                words)
            number_of_long_words = calculate_number_of_long_words(words)
            linguistic_features, sentence_length = simple_tokenization(line)

            number_of_polysyllabic_words = calculate_number_of_polysyllabic_words(
                words)
            missing_word, missing_word_pos, option1, option2, option3 = define_missing_word(
                my_doc)
            named_entities = define_named_entities(my_doc)
            question_mark = define_question_mark(words_all)

            matches_passive = matcher_passive(my_doc)

            matches_determiner = matcher_determiner(my_doc)
            matches_wh_determiner = matcher_wh_determiner(my_doc)
            matches_predeterminer = matcher_predeterminer(my_doc)

            matches_verb = matcher_verb(my_doc)
            matches_adverb = matcher_adverb(my_doc)
            matches_adjective = matcher_adjective(my_doc)

            matches_conjuction = matcher_conjuction(my_doc)
            matches_subject = matcher_subject(my_doc)
            matches_object = matcher_object(my_doc)
            matches_simple_past_tense = matcher_simple_past_tense(my_doc)
            matches_future_tense = matcher_future_tense(my_doc)
            matches_present_continuous_tense = matcher_present_continuous_tense(
                my_doc)
            matches_present_perfect_tense = matcher_present_perfect_tense(
                my_doc)
            matches_present_perfect_continuous_tense = matcher_present_perfect_continuous_tense(
                my_doc)
            matches_simple_present_tense = matcher_simple_present_tense(my_doc)
            matches_possesive_ending = matcher_possesive_ending(my_doc)
            matches_possesive_pronoun = matcher_possesive_pronoun(my_doc)

            matches_prepositions_sub_conj = matcher_prepositions_sub_conj(
                my_doc)
            matches_adverb_particle = matcher_adverb_particle(my_doc)

            matches_comparative_adjective = matcher_comparative_adjective(
                my_doc)
            matches_superlative_adjective = matcher_superlative_adjective(
                my_doc)

            matches_comparative_adverb = matcher_comparative_adverb(my_doc)
            matches_superlative_adverb = matcher_superlative_adverb(my_doc)

            matches_modals = matcher_modals(my_doc)
            matches_there_is_are = matcher_there_is_are(my_doc)
            matches_to_infinitive = matcher_to_infinitive(my_doc)
            matches_gerunds = matcher_gerunds(my_doc)

            write_linguistic_features(matches_passive)

            coor_conjuction = write_linguistic_features(matches_conjuction)
            c_conj = AddOptions("CONJUCTION", coor_conjuction)
            coor_conjuction.insert(0, c_conj.add_options())

            write_linguistic_features(matches_subject)
            write_linguistic_features(matches_object)
            write_linguistic_features(matches_simple_past_tense)
            write_linguistic_features(matches_future_tense)
            write_linguistic_features(matches_present_continuous_tense)
            write_linguistic_features(matches_present_perfect_tense)
            write_linguistic_features(matches_present_perfect_continuous_tense)
            write_linguistic_features(matches_simple_present_tense)
            write_linguistic_features(matches_possesive_ending)

            verb = write_linguistic_features(matches_verb)
            vb = AddOptions("VERB", verb)
            verb.insert(0, vb.add_options_vocab(nlp, "v"))

            adverb = write_linguistic_features(matches_adverb)
            advb = AddOptions("ADVERB", adverb)
            adverb.insert(0, advb.add_options_vocab(nlp, "r"))

            adjective = write_linguistic_features(matches_adjective)
            adj = AddOptions("ADJECTIVE", adjective)
            adjective.insert(0, adj.add_options_vocab(nlp, "a"))

            determiner = write_linguistic_features(matches_determiner)
            det = AddOptions("DETERMINER", determiner)
            determiner.insert(0, det.add_options())

            wh_determiner = write_linguistic_features(matches_wh_determiner)
            wh_det = AddOptions("WH-DETERMINER", wh_determiner)
            wh_determiner.insert(0, wh_det.add_options())

            predeterminer = write_linguistic_features(matches_predeterminer)
            predet = AddOptions("PREDETERMINER", predeterminer)
            predeterminer.insert(0, predet.add_options())

            possesive_pronoun = write_linguistic_features(
                matches_possesive_pronoun)
            pos_pro = AddOptions("POSSESIVE_PRONOUN", possesive_pronoun)
            possesive_pronoun.insert(0, pos_pro.add_options())

            preposition = write_linguistic_features(
                matches_prepositions_sub_conj)
            pp = AddOptions("PREPOSITION", preposition)
            preposition.insert(0, pp.add_options())

            adverb_particle = write_linguistic_features(
                matches_adverb_particle)
            ap = AddOptions("ADVERB_PARTICLE", adverb_particle)
            adverb_particle.insert(0, ap.add_options())

            write_linguistic_features(matches_comparative_adjective)
            write_linguistic_features(matches_superlative_adjective)
            write_linguistic_features(matches_comparative_adverb)
            write_linguistic_features(matches_superlative_adverb)

            modal = write_linguistic_features(matches_modals)
            md = AddOptions("MODAL", modal)
            modal.insert(0, md.add_options())

            write_linguistic_features(matches_there_is_are)
            write_linguistic_features(matches_to_infinitive)
            write_linguistic_features(matches_gerunds)

            difficulty_score = (sentence_length + word_character_length_mavrg)

            print(
                "-----------------------------------------------------------------------")
            print(words)
            print(f"Sentece Length: {sentence_length}")
            print(f"Mean Average Word Length: {word_character_length_mavrg}")
            print(f"Number of Long Words: {number_of_long_words}")
            print(
                f"Number of Polysyllabic Words: {number_of_polysyllabic_words}")

            print(f"Question Sentence: {question_mark}")
            print(
                "-----------------------------------------------------------------------")

            pos_item = 'v'

            if missing_word_pos == "VERB":
                pos_item = 'v'
            if missing_word_pos == "ADJ":
                pos_item = 'a'
            if missing_word_pos == "ADV":
                pos_item = 'r'

            #synset = wordnet.synsets(missing_word, pos=pos_item)

            missing_word_definition = ''
            #if synset:
            #    missing_word_definition = synset[0].definition()
            #    print('Missing word definition:', missing_word_definition)

            image_file_name = filename_generator()

            json_data.append({
                'sentence': line,
                'sentence_length': sentence_length,
                'difficulty_score': difficulty_score,
                'missing_word': missing_word,
                'missing_word_pos': missing_word_pos,
                'missing_word_definition': missing_word_definition,
                'option1': option1,
                'option2': option2,
                'option3': option3,
                'word_character_length_mavrg': word_character_length_mavrg,
                'number_of_long_words': number_of_long_words,
                'named_entities': named_entities,
                'linguistic_features': linguistic_features,
                'image_file_name': image_file_name,
                'preposition': preposition,
                'adverb_particle': adverb_particle,
                'coordinating_conjuction': coor_conjuction,
                'modal': modal,
                "possesive_pronoun": possesive_pronoun,
                "predeterminer": predeterminer,
                "wh_determiner": wh_determiner,
                "determiner": determiner,
                "adverb": adverb,
                "adjective": adjective,
                "verb": verb,
                "article_url" : data_line['articel_url']
            },
            )

            time.sleep(1)

            with open(Settings.ARTICLE_SENTENCES_PROCESSED_JSON_FILE, 'w') as outfile:
                json.dump(json_data, outfile)

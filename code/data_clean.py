"""
    Remove english sentences, ensure only one sentence per line,
    remove sentences which contain only special characters.
"""
import re

def detect_english(sentence):
    return True


def sentence_per_line(sentence):
    sub_sentences = sentence.split('।')
    return sub_sentences


def remove_small_sentence(sentence):
    return True if len(sentence) <= 5 else False


cleaned_file = open('../data/hindi_cleaned.txt', 'w')

with open('../data/hindi.txt', 'r') as hindi_file:
    for sentence in hindi_file:
        english_sentence = detect_english(sentence)
        sub_sentences = sentence_per_line(sentence)
        small_sent = remove_small_sentence(sentence)
        if not english_sentence and not small_sent:  # If not english sentence and neither small sentence
            for sent in sub_sentences:
                cleaned_file.write(sent + '\n')

cleaned_file.close()

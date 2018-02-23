"""
    Remove english sentences, ensure only one sentence per line,
    remove sentences which contain only special characters.
"""
import re

def detect_english(sentence):
    sentence = re.sub(r'[A-Za-z0-9]*|.''','',sentence)
    return sentence


def sentence_per_line(sentence):
    sub_sentences = sentence.split('।')
    return sub_sentences


def remove_small_sentence(sentence):
    return True if len(sentence) <= 5 else False


cleaned_file = open('hindi_cleaned.txt', 'w')
#
# with open('hindi.txt', 'r') as hindi_file:
#     for sentence in hindi_file:
#         english_sentence = detect_english(sentence)
#         sub_sentences = sentence_per_line(sentence)
#         small_sent = remove_small_sentence(sentence)
#         if not english_sentence and not small_sent:  # If not english sentence and neither small sentence
#             for sent in sub_sentences:
#                 cleaned_file.write(sent + '\n')

with open('hindi.txt', 'r') as hindi_file:
    for sentence in hindi_file:
        sub_sentences = sentence_per_line(sentence)
        small_sent = remove_small_sentence(sentence)
        if not small_sent:  # If not english sentence and neither small sentence
            for sent in sub_sentences:
                english_sentence_remove = detect_english(sent)
                cleaned_file.write(english_sentence_remove)

cleaned_file.close()

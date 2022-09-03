from ast import pattern
from lib2to3.pgen2.tokenize import tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
#Read TXT file
f = open("scene_one.txt", "r")
scene_one = f.read()
sentences = sent_tokenize(scene_one)

tokenize_sent = word_tokenize(sentences[0])
#print(tokenize_sent)
unique_tokens = set(word_tokenize(scene_one))
#print(len(unique_tokens))
match = re.search("coconuts",scene_one)
#print(match.start(),match.end()) # หาตำแหน่ง
pattern1 = r"\[.*\]" #หาอะไรก้ได้ใน []
#print(re.search(pattern1,scene_one))
pattern2 = r"[\w\s]+:"
#print(re.match(pattern2,sentences[3]))

match_digits_and_words = ('(\d+|\w+)')
print(re.findall(match_digits_and_words, 'He has 11 cats'))
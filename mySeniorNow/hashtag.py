from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re
tweets = ['This is the #nlp exercise! #python', '#NLP is super fun! <3 #learning', 'Thanks @fitmkmutnb :) #nlp #python']
pattern1 = r"#\w+"
hashtags = regexp_tokenize(tweets[0], pattern1)
#print(hashtags)
pattern2 = r"([@#]\w+)"
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
#print(mentions_hashtags)
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)
from nltk.tokenize import word_tokenize
from collections import Counter
#counter = Counter(word_tokenize("""The cat is in the box.
#The cat likes the box. The box is over the cat."""))
#print(counter)
#print('******************************')
f = open("wiki_article.txt", "r")
article = f.read()
tokens = word_tokenize(article)
lower_tokens = [t.lower() for t in tokens]
bow_simple = Counter(lower_tokens)
print(bow_simple.most_common())

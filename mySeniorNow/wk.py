import itertools
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from collections import defaultdict
articles = []
for i in range(10) :
    #Read TXT file
    f = open(f".\wiki\wiki_article_{i}.txt", "r")
    article = f.read()
    # Tokenize the article: tokens
    tokens = word_tokenize(article)
    # Convert the tokens into lowercase: lower_tokens
    lower_tokens = [t.lower() for t in tokens]
    # Retain alphabetic words: alpha_only
    alpha_only = [t for t in lower_tokens if t.isalpha()]
    # Remove all stop words: no_stops
    no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
    # Instantiate the WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    # Lemmatize all tokens into a new list: lemmatized
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    #list_article
    articles.append(lemmatized)

dictionary = Dictionary(articles)
computer_id = dictionary.token2id.get("computer")
#print(dictionary.get(computer_id))
corpus = [dictionary.doc2bow(a) for a in articles]
# Save the second document: doc
doc = corpus[0]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)
# Print the top 5 words of the document alongside the count
#for word_id, word_count in bow_doc[:5]:
    #print(dictionary.get(word_id), word_count)

total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id] += word_count
# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1],reverse=True)
# Print the top 5 words across all documents alongside the count
for word_id, word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id), word_count)


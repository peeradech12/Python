#tfidf
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel

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

# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)
# Create a Corpus: corpus
corpus = [dictionary.doc2bow(a) for a in articles]
# Save the second document: doc
for n in range (10):
    print("---------"+str(n)+"----------")
    doc = corpus[n]

    # Create a new TfidfModel using the corpus: tfidf
    tfidf = TfidfModel(corpus)
    # Calculate the tfidf weights of doc: tfidf_weights
    tfidf_weights = tfidf[doc]
    # Print the first five weights
    #print(tfidf_weights[:5])

    sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)
    # Print the top 5 weighted words
    for term_id, weight in sorted_tfidf_weights[:5]:
        print(dictionary.get(term_id), weight)
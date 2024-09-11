import re
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Load English tokenizer, POS tagger, etc. from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Natural language processing (NLP) is a sub-field of artificial intelligence (AI) focused on the interaction between humans and computers using natural language. NLP is used in applications such as speech recognition, machine translation, and sentiment analysis.
"""

# 1. Clean Text using Regex
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

cleaned_text = clean_text(text)
print("Cleaned Text:", cleaned_text)

# 2. Tokenization
def tokenize_text(text):
    return word_tokenize(text)

tokens = tokenize_text(cleaned_text)
print("Tokens:", tokens)

# 3. Remove Stop Words
stop_words = set(stopwords.words('english'))

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

filtered_tokens = remove_stopwords(tokens)
print("Filtered Tokens:", filtered_tokens)

# 4. Lemmatization using spaCy
def lemmatize_text(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

lemmatized_tokens = lemmatize_text(filtered_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)

# 5. Convert Text to TF-IDF Representation
corpus = ["Natural language processing is a field of AI.", "Machine learning and deep learning are subsets of AI."]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

print("TF-IDF Matrix:")
print(X.toarray())

# 6. Named Entity Recognition (NER) using spaCy
def extract_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

entities = extract_entities(text)
print("Named Entities:", entities)









'''
Explanation of the Pipeline Steps:
Clean Text using Regex:

Convert the text to lowercase.
Remove URLs, numbers, and punctuation using regex.
Tokenization:

Tokenize the text using NLTK’s word_tokenize(). Tokenization breaks text into individual words or tokens.
Remove Stop Words:

Remove common stop words like "the", "is", "in", etc., using the NLTK stop words list.
Lemmatization:

Use spaCy’s lemmatizer to convert words to their base or dictionary form (e.g., "processing" becomes "process").
TF-IDF (Term Frequency-Inverse Document Frequency):

Transform text into a numerical representation using the TfidfVectorizer, which converts a collection of documents into a matrix of TF-IDF features.
Named Entity Recognition (NER):

Use spaCy to extract entities from the text such as names, dates, and locations, and classify them into predefined categories (e.g., "ORG" for organizations, "DATE" for dates).
Customization Tips:
Regex Customization: Adjust regex patterns in clean_text() for specific text cleaning needs. You can add more patterns to remove emails, hashtags, or custom symbols.
Stop Words: Use a custom stop word list if you want to keep some words that are otherwise classified as stop words.
Lemmatization vs. Stemming: If you prefer stemming instead of lemmatization, you can replace spaCy's lemmatizer with NLTK’s PorterStemmer().
'''

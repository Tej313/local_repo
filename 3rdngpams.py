from sklearn.feature_extraction.text import CountVectorizer

# Initialize CountVectorizer with ngram_range=(2, 2) for bigrams
v = CountVectorizer(ngram_range=(2, 2))

# Fit the vectorizer to the text data
v.fit(["Thor Hathodawala is looking for a job"])

# Get the vocabulary (mapping of terms to feature indices)
vocabulary = v.vocabulary_

# Example usage
corpus = [
    "Thor ate pizza",
    "Loki is tall",
    "Loki is eating pizza"
]
print(v.transform(["Thor ate pizza"]).toarray())

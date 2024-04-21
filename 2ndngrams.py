# Example usage
corpus = [
    "Thor ate pizza",
    "Loki is tall",
    "Loki is eating pizza"
]
import spacy

# Load English language model and create nlp object from it
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    return " ".join(filtered_tokens)

preprocessed_corpus = [preprocess(text) for text in corpus]
print(preprocessed_corpus)
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Example text
text = "Natural Language Processing is an exciting field. It helps machines understand human language."

# Process the text
doc = nlp(text)

# 1. Sentence Tokenization
print("Sentence Tokenization:")
for sent in doc.sents:
    print("-", sent.text)

# 2. Word Tokenization
print("\nWord Tokenization:")
for token in doc:
    print(token.text, end=' ')

# 3. Remove Stopwords
print("\n\nWords without Stopwords:")
filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
print(filtered_tokens)

# 4. Lemmatization
print("\nLemmatized Words:")
lemmas = [token.lemma_ for token in doc if not token.is_punct]
print(lemmas)

# 5. Named Entity Recognition
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)

# 6. POS Tagging
print("\nPart-of-Speech Tags:")
for token in doc:
    print(f"{token.text} → {token.pos_}")

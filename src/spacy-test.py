import spacy

nlp = spacy.load("en_core_web_sm")
text = "I love this product, but the quality could be better."
doc = nlp(text)

# Extract noun phrases
for np in doc.noun_chunks:
    print(np.text)

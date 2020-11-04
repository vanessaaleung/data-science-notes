# Feature Extraction from Text and Images
## Text
1. Bag of Words
2. Embeddings (~word2vec)

### Bag of Words
- Preprocessing -> use bag of words -> ngrams -> TFiDF
- Each row represents a text, each column represents a unique word
- Count the number of occurences via `CountVectorizer`
- Ngrams: each column is a gorup of several consecutive words/chars
- TFiDF: make the values more comparable, `TfidfVectorizer`

#### Preprocessing
- Lowercase
- Lemmatization: more careful, using knowledge/vocabulary
  - e.g. democracy, democratic, and democratization -> democracy
  - e.g. saw -> s
- Stemming: chops off ending of words
  - e.g. democracy, democratic, and democratization -> democr
  - e.g. saw -> see
- Stopwords: articles/prepositions, very common words

### Embeddings

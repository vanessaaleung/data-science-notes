# Feature Extraction from Text and Images
- [Text](#text)
  - [Bag of Words](#bag-of-words)
  - [Word2Vec](#word2vec)
  - [BoW vs w2v](#bow-vs-w2v)
- [Images](#images)
## Text
1. Bag of Words
2. Embeddings (~word2vec)

### Bag of Words
- Preprocessing -> use bag of words -> ngrams -> TFiDF
- Each row represents a text, each column represents a unique word
- Count the number of occurences via `CountVectorizer`
- Ngrams: each column is a group of several consecutive words/chars, can include interaction between words
  - are typically sparse
- TFiDF: make the values more comparable, `TfidfVectorizer`
  - IDF: decrease importance of most frequent words

#### Preprocessing
- Lowercase
- Lemmatization: more careful, using knowledge/vocabulary
  - e.g. democracy, democratic, and democratization -> democracy
  - e.g. saw -> s
- Stemming: chops off ending of words
  - e.g. democracy, democratic, and democratization -> democr
  - e.g. saw -> see
- Stopwords: articles/prepositions, very common words

### Word2vec
_Get vector representation for text_
- Words often used in the same context will be close in the vector representation
- Uses a **neural network model** to learn word associations from a large corpus of text

### BoW vs w2v
- Bag of Words
  1. very large vectors
  2. meaning of each value in vector is known
  3. Ngrams can help to use local context
- Word2vec
  1. relatively small vectors
  2. values in vector can be interpreted only in some cases
  3. words with  similar meaning often have similar embeddings

## Images
- use pre-trained neural networks to extract features
- finetune pre-trained models

1. Descriptors
  - Output of inner layers
  - Descriptors from early layers have more text independent information
2. Trainn network from scratch
3. Finetuning: refine pretrained models: VGG, ResNet, etc.


### Augmentation
_Increase the amount of trained data_
- rotation
- add noise

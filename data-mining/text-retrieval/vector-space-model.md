# Vector Space Model

## Guiding Questions
### What are some different ways to place a document as a vector in the vector space?
- Term Frequency Vector
- Adding Inverse Document Frequency (IDF)

  <img src="images/idf-vector.png" height="250px">

### What is term frequency (TF)?
- Count of a term in a document

### What is TF transformation?

### What is document frequency (DF)?
- Count of documents that contain a particular term

### What is inverse document frequency (IDF)?
- Reward a word that doesn't occur in any documents, penalize common words

### What is TF-IDF weighting?
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;IDF(W)=log[\frac{M&plus;1}{k}]" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;IDF(W)=log[\frac{M&plus;1}{k}]" title="IDF(W)=log[\frac{M+1}{k}]" /></a>
- M: total number of docs in collection
- k: total number of docs containing

<img src="images/idf-weighting.png" height="250px">

### Why do we need to penalize long documents in text retrieval?

### What is pivoted document length normalization?

### What are the main ideas behind the retrieval function BM25?

### What is the typical architecture of a text retrieval system?

### What is an inverted index?

### Why is it desirable to compress an inverted index?

### How can we create an inverted index when the collection of documents does not fit into the memory?

### How can we leverage an inverted index to score documents quickly?

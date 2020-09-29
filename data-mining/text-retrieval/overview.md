# Overview

## Guiding Questions
### What does a computer have to do in order to understand a natural language sentence?

  <img src="images/nlp-example.png" height="300px">
  
  1. Lexical analysis (part-of-speech tagging): tag Noun, Verb, Prep, etc.
  2. Syntactic analysis (parsing): some words go together first, and then go with other wordsantic analysis  - know the structure of the sentence
  3. Semantic analysis: use symbols to denote objects and relationship - know the meaning of the sentence
  4. Inference
  5. Pragmatic analysis (speech act): the goal of the sentence
  
### What is ambiguity?
  - Word-level ambiguity: design can be a noun or a verb
  - Syntactic ambiguity
    - Modification: "natural language processing"
    - Prepositional phrase (PP) attachment: "A man saw a boy *with a telescope*"
  - Anaphora resolution: "John persuaded Bill to buy a TV for *himself*"
  - Presupposition: "He has quit smoking" implies he smoked before
  
### Why is natural language processing (NLP) difficult for computers?
  - Natural language is designed for human, we omit a lot of "common sense" knowledge, keep a lot of ambiguities
  
### What is bag-of-words representation? Why do modern search engines use this simple representation of text?
  - Keep individual words, but ignore the orders of words
  - When searching, related words often appear together which helps understand, e.g. "Java applet" and "Java coffee"
  
### What are the two modes of text information access? Which mode does a web search engine such as Google support?
  - Pull (search engines): users take initiative, ad hoc information
    - Querying: user enters a query, system returns relevant document
    - Browsing: user navigates into relevant information by following a path enabled by the structures on the documents
    - Want to combine the two way
  - Push (recommender systems): systems take initiative, stable information need
  - Combine the two in sophisticated information system
  
### When is browsing more useful than querying to help a user find relevant information?
  - Querying: works well when the user knows what keywords to use
  - Browsing: works well when user wants to explore information
  
### Why is a text retrieval task defined as a ranking task?
  - The problem of Selection
    - Over-constrained (no relevant) / Under-constrained (over delivery), hard to find the position between two extremes
    - All relevant documents are not equally relevant, prioritization is needed
    
### What is a retrieval model?
  - Formalization of relevance (give a computational definition  of relevance)

### What are the two assumptions made by the Probability Ranking Principle?
  1. The utility of a document (to a user) is independent of the utility of any other document
    - Not really true when a user has already seen a similar/duplicated document before, or multiple documents are only userful to users when they are put together
  2. A user would browse the results sequentially
    - Evidence shows that users don't always just go strictly sequentially through the entire list

### What is the Vector Space Retrieval Model? How does it work?
  - Assumes relevance is roughly similarity between the document and the query
  - In a high dimensional space, each dimension corresponds to a term (word/phrase), N terms define an N-dimensional space
  - Represent a doc/query by a term vector
  <img src="images/vector-space-model.png" height="250px">
  - Term weight in query indicates the importance of term
  - Term weight in doc indicates how well the term characterizes the doc
  - How to place docs and query in the space? How to assign term weights?
  - How to define the similarity measure?
  
### How do we define the dimensions of the Vector Space Model? What does “bag of words” representation mean?
  - Each dimension corresponds to a term/word, N terms define an N-dimensional space
  - Bag of words: keep individual words, but ignore the orders of words

### What does the retrieval function intuitively capture when we instantiate a vector space model with bag of words representation and bit representation for documents and queries?
  - Bit representation
    <img src="images/bit-vector.png" height="200px"> 
  - Similarity Instantiation: Dot Product
    <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Sim(q,d)=q.d=x_1y_1&plus;...&plus;x_Ny_N=\sum_{i=1}^{N}x_iy_i" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Sim(q,d)=q.d=x_1y_1&plus;...&plus;x_Ny_N=\sum_{i=1}^{N}x_iy_i" title="Sim(q,d)=q.d=x_1y_1+...+x_Ny_N=\sum_{i=1}^{N}x_iy_i" /></a>
  - VSM = Bit-Vector + Dot-Product + BOW
    - Simplest VSM
      - Dimension = word
      - Vector = 0-1 bit vector (Word presence/absence)
      - Similarity: dot-product
      - f(q,d): number of unique query terms matched in each document
    
## Text Retrieval Problem
_The system would respond to a user's query with relevant documents_
- Implement the pull mode of information access
- An empirically defined problem: which algorithm is better must be judged by users

### Formal Formulation of TR
- Vocabulary: a set of words in a language, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;V={w_1,&space;w_2,&space;...,&space;w_N}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;V={w_1,&space;w_2,&space;...,&space;w_N}" title="V={w_1, w_2, ..., w_N}" /></a>
- Query: a sequence of words, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;q&space;=&space;q_1,&space;...,&space;q_m" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;q&space;=&space;q_1,&space;...,&space;q_m" title="q = q_1, ..., q_m" /></a>, where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;q_i&space;\in&space;V" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;q_i&space;\in&space;V" title="q_i \in V" /></a>
- Document: <img src="images/documents.svg">, where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;d_{ij}&space;\in&space;V" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;d_{ij}&space;\in&space;V" title="d_{ij} \in V" /></a>
- Collection: a collection of documents, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;C={d_1,&space;...,&space;d_M}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;C={d_1,&space;...,&space;d_M}" title="C={d_1, ..., d_M}" /></a>
- Set of relevant documents: goal of retrieval, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;R(q)&space;\subseteq&space;C" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;R(q)&space;\subseteq&space;C" title="R(q) \subseteq C" /></a>
  - Generally unknown and user-dependent
  - Query is a "hint" on which doc is in R(q)
- Task: compute <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;{R}'(q)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;{R}'(q)" title="{R}'(q)" /></a>, an approximation of R(q)

### How to Compute R'(q)
<img src="images/selection-ranking.png" height="300px">

1. Document selection
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;{R}'(q)=\left&space;\{d\in&space;C|f(d,q)=1&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;{R}'(q)=\left&space;\{d\in&space;C|f(d,q)=1&space;\right&space;\}" title="{R}'(q)=\left \{d\in C|f(d,q)=1 \right \}" /></a>
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;f(d,q)&space;\in&space;\left&space;\{&space;0,&space;1&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;f(d,q)&space;\in&space;\left&space;\{&space;0,&space;1&space;\right&space;\}" title="f(d,q) \in \left \{ 0, 1 \right \}" /></a>: a binary classifier, whether the document is relevant to the query or not
  - Abosolute relevance: system must decide if a doc is relevant or not
  - Problems
    - Over-constrained (no relevant) / Under-constrained (over delivery), hard to find the position between two extremes
    - All relevant documents are not equally relevant, prioritization is needed
  
2. Document ranking
  - <img src="images/document-ranking.svg">
  - <img src="images/relevance-measure.svg"> is a relevance measure function, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\theta" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\theta" title="\theta" /></a> is a cutoff determined by the user
  - Relative relevance: sytem only needs to decide is one doc is more likely relevant than another
  - Easier to determine

### Probability Ranking Principle
Returning a ranked list of documents in descending order of probability that a document is relevant to the query is the optimal strategy under the two assumptions:
1. The utility of a document (to a user) is independent of the utility of any other document
2. A user would browse the results sequentially

## Text Retrieval Methods
- Similarity-based models: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;f(q,d)=similarity(q,d)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;f(q,d)=similarity(q,d)" title="f(q,d)=similarity(q,d)" /></a>
  - Vector space model
- Probabilistic models: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;f(d,q)=p(R=1|d,q),&space;where&space;R&space;\in&space;\left\{0,1\right\}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;f(d,q)=p(R=1|d,q),&space;where&space;R&space;\in&space;\left\{0,1\right\}" title="f(d,q)=p(R=1|d,q), where R \in \left\{0,1\right\}" /></a>
  - Assumes that queries and documents are all observations from random variables, R indicates whether the document is relevant to the query
  - The probability of random variable R is 1, given a particular document query
  - Classic probabilistic model
  - Language model
  - Divergence-from-randomness model
- Probabilistic inference model: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;f(q,d)=p(d\rightarrow&space;q)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;f(q,d)=p(d\rightarrow&space;q)" title="f(q,d)=p(d\rightarrow q)" /></a>
  - Associate uncertainty to inference rules
- Axiomatic model: f(q,d) must satisfy a set of constraints
- Models tend to result in similar ranking functions

### State of Art Ranking Functions
- tend to rely on
  - Bag of words representation
  - Term Frequency (TF): how many times a word occur in a document, the higher the frequency, the higher the score
  - Document Length: how long is the document, the longer document, the lower the score
  - Document Frequency: how often the word appears in a collection of documents, matching a rare word will get a higher score

## Vector Space Model
- Bit representation

  <img src="images/bit-vector.png" height="200px"> 
- Similarity Instantiation: Dot Product
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Sim(q,d)=q.d=x_1y_1&plus;...&plus;x_Ny_N=\sum_{i=1}^{N}x_iy_i" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Sim(q,d)=q.d=x_1y_1&plus;...&plus;x_Ny_N=\sum_{i=1}^{N}x_iy_i" title="Sim(q,d)=q.d=x_1y_1+...+x_Ny_N=\sum_{i=1}^{N}x_iy_i" /></a>
- VSM = Bit-Vector + Dot-Product + BOW

# Overview

# Guiding Questions
- **What does a computer have to do in order to understand a natural language sentence?**
  1. Lexical analysis (part-of-speech tagging): tag Noun, Verb, Prep, etc.
  2. Syntactic analysis (parsing): some words go together first, and then go with other wordsantic analysis  - know the structure of the sentence
  3. Semantic analysis: use symbols to denote objects and relationship - know the meaning of the sentence
  4. Inference
  5. Pragmatic analysis (speech act): the goal of the sentence
  
- **What is ambiguity?**
  - Word-level ambiguity: design can be a noun or a verb
  - Syntactic ambiguity
    - Modification: "natural language processing"
    - Prepositional phrase (PP) attachment: "A man saw a boy *with a telescope*"
  - Anaphora resolution: "John persuaded Bill to buy a TV for *himself*"
  - Presupposition: "He has quit smoking" implies he smoked before
  
- **Why is natural language processing (NLP) difficult for computers?**
  - Natural language is designed for human, we omit a lot of "common sense" knowledge, keep a lot of ambiguities
  
- **What is bag-of-words representation? Why do modern search engines use this simple representation of text?**
  - Keep individual words, but ignore the orders of words
  - When searching, related words often appear together which helps understand, e.g. "Java applet" and "Java coffee"
  
- **What are the two modes of text information access? Which mode does a web search engine such as Google support?**
  - Pull (search engines): users take initiative, ad hoc information
  - Push (recommender systems): systems take initiative, stable information need
  
- When is browsing more useful than querying to help a user find relevant information?
- Why is a text retrieval task defined as a ranking task?
- What is a retrieval model?
- What are the two assumptions made by the Probability Ranking Principle?
- What is the Vector Space Retrieval Model? How does it work?
- How do we define the dimensions of the Vector Space Model? What does “bag of words” representation mean?
- What does the retrieval function intuitively capture when we instantiate a vector space model with bag of words representation and bit representation for documents and queries?

# Key Phrases and Concepts
1. Part of speech tagging, syntactic analysis, semantic analysis, and ambiguity
2. “Bag of words” representation
3. Push, pull, querying, browsing
4. Probability ranking principle
5. Relevance
6. Vector space model
7. Dot product
8. Bag of words representation
9. Bit vector representation

## Natural Language Content Analysis

## Text Access

## Text Retrieval Problem

## Text Retrieval Methods

## Vector Space Model

## Vector Space Retrieval Model


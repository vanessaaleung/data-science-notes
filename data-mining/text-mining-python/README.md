# Text Mining in Python
- Regex
- Non-ASCII Characters
- Spelling Recommender
- [Naive Bayes Classifiers](#naive-bayes-classifiers)
- [Naive Bayes Variants](#naive-bayes-variants)
- [Support Vector Machines](#support-vector-machines)

## Regex
### Character matches
  - `.`: wildcard, matches a single character
  - `^`: start of a string
  - `$`: end of a string
  - `[]`: matches one of the set of characters within []
  - `[^abc]`: matches a character that is not a, b, or, c
  - `a|b`: matches either a or b
  - `()`: scoping for operators
  - `\`: escape characters (\t, \n, \b)
  
### Character symbols
- `\b`: matches word boundary
- `\d`: any digit
- `\D`: any non-digit
- `\s`: any whitespaces
- `\S`: any non-whitespace
- `w`: alphanumeric
- `\W`: non-alphanumeric

### Repetitions
- `*`: matches 0+ times
- `+`: matches 1+ times
- `?`: matches 0 or 1 times
- `{n}`: exactly n times
- `{n,}: at least n repetitions
- `{,n}: at most n repetitions
- `{m, n}`: at least m and at most n

### Regex in Python
```python
import re
[w for w in text if re.search('@\w+', w)]
re.findall(r'[aeiou]', text)
```

## Non-ASCII Characters
### ASCII
_American Standard Code for Information Interchange_
- 7-bit long, 128 valid codes
- Range: 0x00 - 0x7F
- Includes alphabets(upper & lower), digits, punctuations, control characters, common symbols

### Unicode
_Industry standard for encoding and representing text_
- UTF-8: 1-4 bytes
  - Unicode Transformational Format - 8-bits
- UTF-16: one or two 16-bit code units
- UTF-32: one 32-bit code unit

## Basic NLP tasks with NLTK
- Frequency of words
```python
dist = FreqDist(text)
```
- Stemming
- Lemmatization: stemming, but resulting stems are all valid words
- Tokenization: built-in tokenizer
```python
nltk.word_tokenize(text)
```
- Sentence Splitting
```python
nltk.sent_tokenize(text)
```
- Part-of-speech (POS) Tagging
```python
nltk.help.upenn_tagset('MD')
nltk.pos_tag(text)
```
- Parsing Sentence Structure
```python
grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP
  NP -> 'Alice' | 'Bob'
"""
grammar = nltk.data.load('grammar.cfg')
)
```
```python
parser = nltk.ChartParser(grammar)
trees = parser.parse_all(text)
for tree in trees:
  print(tree)
```
- Parse Tree Collection
```python
from nltk.corpus import treebank
text = treebank.parsed_sent('wsj.mrg')[0]
```

## Spelling Recommender
- Jaccard distance: comparing set-similarity
- edit distance: the number of characters that need to be substituted, inserted, or deleted, to transform s1 into s2

## Naive Bayes Classifiers
_Probabilistic model_
- Assumption: (why called naive) features are assumed to be independent of each other, given the class label
- Provides baseline for text classification problems
- Update the likelihood of the class given new information
- Parameters:
  - Prior probability: P(y) for all y in Y, e.g. P(Zoology)
  - Likelihood: probability of seeing a particular feature in y, e.g. P(Python|Zoology)
    - Count how many times feature xi appears in class y
- Posterior probability: P(Entertainment|Python)
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(x|y)=\frac{P(x)\times&space;P(y|x)}{P(y)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(x|y)=\frac{P(x)\times&space;P(y|x)}{P(y)}" title="P(x|y)=\frac{P(x)\times P(y|x)}{P(y)}" /></a>
- Smoothing: if feature xi never occurs in class y, P(xi|y) = 0
  - Laplace/Additive smoothing: add a dummy count, e.g. add count of one to every word in every class
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(x_i|y)=(k&plus;1)/(p&plus;n),&space;n=&space;\text{number&space;of&space;features}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(x_i|y)=(k&plus;1)/(p&plus;n),&space;n=&space;\text{number&space;of&space;features}" title="P(x_i|y)=(k+1)/(p+n), n= \text{number of features}" /></a>
  
## Naive Bayes Variants
- Multinomial Naive Bayes
  - Data follows multinomial distribution
  - Number of times a word occurs is important
  - Each feature value is a count
  - Very common
- Bernoulli Naive Bayes
  - Data follows a multivariate Bernoulli distribution
  - Each feature is binary (word present/absent), count doesn't matter

## Support Vector Machines
_Linear classifiers sthat find a hyperplane to separate two classes of data_
- Pros
  - Tend to be most accurate in high-dimensional data
- Cons
  - Handles only numeric features, need normalization
  - Hyperplane is hard to interpret
- Decision Boundaries
  - Linear: easy to find/evaluate, more generalizable
    - perceptron
    - linear discriminative analysis
    - linear least squares
  - A resonable boundary: maximize margin, find the thickest band that seperates the positive and negative points
- SVM is a Maximum-margin Classifiers, work only for binary classification problems
- Multi-class
  - One vs Rest, n classfiers learn n class
  - One vs One, C(n, 2) classifiers
- Parameters
  - Regularization: how much importance should give individual data points
    - More regularization: more tolerant to errors on individual data points, more generalized
  - Regularization parameter c: the larger c, less regularization
  - **Linear kernels work best for text data**
  - multi_class: ovr (one-vs-rest)
  - class_weight: different classes can get different weights

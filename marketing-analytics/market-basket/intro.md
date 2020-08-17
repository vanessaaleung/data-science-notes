# Introduction to Market Basket Analysis
- Association Rules
- Metrics
  - Support
  - Confidence
  - Lift

## Steps
1. Construct Association Rules - Identify products frequently purchased together
2. Construct recommendations based on these findings

## Usage
  - Recommendations engine
  - In-store recommendation
  - Cross-sell products
  - Improve inventory
  - Upsell products
  
## Association Rules
- Association rule
  - {health} -> {cooking}
- Multi-antecedent rule
  - {humor, travel} -> {language}
- Multi-consequent rule
  - {biography} -> {history, language}

### Generating rules with itertools
```python
from itertools import permutations
# Extract unique items
flattened = [item for transaction in transactions for item in transaction]
items = list(set(flattened))
```
```python
# Compute and print rules
rules = list(permutations(items, 2))
print(rules)
```

## Metrics
_A measure of performance for rules_

- **Pruning**: the use of metrics to discard rules

### Support
_Measures the share of transactions that contain an itemset_

<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{\text{number&space;of&space;transactions&space;with&space;items(s))}}{\text{number&space;of&space;transactions}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{\text{number&space;of&space;transactions&space;with&space;items(s))}}{\text{number&space;of&space;transactions}}" title="\frac{\text{number of transactions with items(s))}}{\text{number of transactions}}" /></a>
</p>

#### Preparing the data
```python
from mlxtend.preprocessing import TransactionEncoder
# Instantiate transaction encode
encoder = TransactionEncoder().fit(transactions)
```
```python
# One-hot encode itemsets
onehot = encoder.transform(transactions)
# Convert one-hot encoded data to DataFrame
onehot = pd.DataFrame(onehob, columns=encoder.columns_)
```
#### Conputing support for single items
```python
onehot.mean()
```
#### Conputing support for multiple items
```python
import numpy as np
# Define itemset
onehot['fiction+poetry'] = np.logical_and(onehot['fiction'], onehot['poetry'])
onehot.mean()
```
### Confidence
_Probability that we'll purchase Y, given that we have purchased X_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{Support(X\&Y)}{Support(X)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{Support(X\&Y)}{Support(X)}" title="\frac{Support(X\&Y)}{Support(X)}" /></a>
</p>

### Lift
_If > 1: two items occur in transactions together more often than their individual support values, the relationship is unlikely to be explained by random chance_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{Support(X\&Y)}{Support(X)Support(Y)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{Support(X\&Y)}{Support(X)Support(Y)}" title="\frac{Support(X\&Y)}{Support(X)Support(Y)}" /></a>
</p>

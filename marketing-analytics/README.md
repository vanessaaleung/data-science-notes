# Market Basket Analysis

<p align="center">
  <img src="https://miro.medium.com/max/5760/1*DHfQvlMVBaJCHpYmj1kmCw.png" height="300px">
</p>

1. Construct Association Rules - Identify products frequently purchased together
2. Construct recommendations based on these findings

- Usage
  - Recommendations engine
  - In-store recommendation
  - Cross-sell products
  - Improve inventory
  - Upsell products
  
## Association Ruless
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



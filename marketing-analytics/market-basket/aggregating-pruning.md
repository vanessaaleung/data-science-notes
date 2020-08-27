# Aggregating and Pruning
<img src="pruning-and-aggregating.png" height="300px">

## Aggregation
_Groups items together into categories_

1. Select the columnn names for bags
```python
bag_headers = [i for i in onehot.columns if i.lower().find('bag') >= 0]
```

2. Identify column headers
```python
bags = onehot[bag_headers]
```

3. Sum over columns to check whether at least one item in the transaction is a bag
```python
bags = (bags.sum(axis=1) > 0.0).values
```

## Pruning
_Remove items and rules  with low support or poor performance_


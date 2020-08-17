# Association Rules

## Confidence
_Probability that we'll purchase Y, given that we have purchased X_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{Support(X\&Y)}{Support(X)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{Support(X\&Y)}{Support(X)}" title="\frac{Support(X\&Y)}{Support(X)}" /></a>
</p>

## Lift
_If > 1: two items occur in transactions together more often than their individual support values, the relationship is unlikely to be explained by random chance_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{Support(X\&Y)}{Support(X)Support(Y)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{Support(X\&Y)}{Support(X)Support(Y)}" title="\frac{Support(X\&Y)}{Support(X)Support(Y)}" /></a>
</p>

```python
# Compute support for Potter and Twilight
supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()
# Compute support for Potter
supportP = books['Potter'].mean()
# Compute support for Twilight
supportT = books['Twilight'].mean()
# Compute lift
lift = supportPT / (supportP * supportT)
```

## Leverage and Conviction

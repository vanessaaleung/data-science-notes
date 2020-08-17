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

- lies in [0, infinity]

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

## Leverage
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Leverage(X\rightarrow&space;Y)=Support(X\&Y)-Support(X)Support(Y)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Leverage(X\rightarrow&space;Y)=Support(X\&Y)-Support(X)Support(Y)" title="Leverage(X\rightarrow Y)=Support(X\&Y)-Support(X)Support(Y)" /></a>
</p>
- lies in [-1, +1]

```python
leverage = supportTP - supportP * supportT
```

## Conviction
_If > 1: two items occur in transactions together less frequently than their individual support values_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Conviction(X\rightarrow&space;Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Conviction(X\rightarrow&space;Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" title="Conviction(X\rightarrow Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" /></a>
</p>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\bar{Y}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\bar{Y}" title="\bar{Y}" /></a>: transactions that do not include Y

```python
# Compute support for NOT Harry Potter
supportnP  = 1.0 - books['Potter'].mean()
# Compute support for Twilight and NOT Harry Potter
supportTnP = supportT - supportPT
# Compute conviction
conviction = supportT * supportnP / supportTnP
```

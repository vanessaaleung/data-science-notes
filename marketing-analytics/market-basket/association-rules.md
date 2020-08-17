# Association Rules
- [Confidence and Lift](#confidence-and-lift)
- [Leverage and Conviction](#leverage-and-conviction)
- [Association and Dissociation](#association-and-dissociation)

## Confidence and Lift
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

## Leverage and Conviction
### Leverage
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Leverage(X\rightarrow&space;Y)=Support(X\&Y)-Support(X)Support(Y)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Leverage(X\rightarrow&space;Y)=Support(X\&Y)-Support(X)Support(Y)" title="Leverage(X\rightarrow Y)=Support(X\&Y)-Support(X)Support(Y)" /></a>
</p>

- based on support
- similar to lift, advantage: bound by [-1, +1]
- threshold: 0

```python
leverage = supportTP - supportP * supportT
```

### Conviction
_If > 1: two items occur in transactions together less frequently than their individual support values_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Conviction(X\rightarrow&space;Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Conviction(X\rightarrow&space;Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" title="Conviction(X\rightarrow Y)=\frac{Support(X)Support(\bar{Y})}{Support(X\&\bar{Y})}" /></a>
</p>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\bar{Y}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\bar{Y}" title="\bar{Y}" /></a>: transactions that do not include Y
- based on support

```python
# Compute support for NOT Harry Potter
supportnP  = 1.0 - books['Potter'].mean()
# Compute support for Twilight and NOT Harry Potter
supportTnP = supportT - supportPT
# Compute conviction
conviction = supportT * supportnP / supportTnP
```

## Association and Dissociation
### Zhang's metric
- takes values between [-1, +1]
- +1: perfect association
- -1: perfect dissociation

<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Zhang(A&space;\rightarrow&space;B)&space;=&space;\frac{Confidence(A&space;\rightarrow&space;B)-Confidence(\bar{A}\rightarrow&space;B)}&space;{Max(Confidence(A&space;\rightarrow&space;B),&space;Confidence(\bar{A}\rightarrow&space;B))}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Zhang(A&space;\rightarrow&space;B)&space;=&space;\frac{Confidence(A&space;\rightarrow&space;B)-Confidence(\bar{A}\rightarrow&space;B)}&space;{Max(Confidence(A&space;\rightarrow&space;B),&space;Confidence(\bar{A}\rightarrow&space;B))}" title="Zhang(A \rightarrow B) = \frac{Confidence(A \rightarrow B)-Confidence(\bar{A}\rightarrow B)} {Max(Confidence(A \rightarrow B), Confidence(\bar{A}\rightarrow B))}" /></a>
</p>
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Confidence=\frac{Support(A\&B)}{Support(A)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Confidence=\frac{Support(A\&B)}{Support(A)}" title="Confidence=\frac{Support(A\&B)}{Support(A)}" /></a>
</p>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Confidence(A&space;\rightarrow&space;B)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Confidence(A&space;\rightarrow&space;B)" title="Confidence(A \rightarrow B)" /></a>: degree of association
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Confidence(\bar{A}\rightarrow&space;B)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Confidence(\bar{A}\rightarrow&space;B)" title="Confidence(\bar{A}\rightarrow B)" /></a>: degree of dissociation

#### Constructing using support
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Zhang(A&space;\rightarrow&space;B)&space;=&space;\frac{Support(A\&B)-Support(A)Support(B)}&space;{Max[Support(AB)(1-Support(A)),&space;Support(A)Support(B)-Support(AB)]}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Zhang(A&space;\rightarrow&space;B)&space;=&space;\frac{Support(A\&B)-Support(A)Support(B)}&space;{Max[Support(AB)(1-Support(A)),&space;Support(A)Support(B)-Support(AB)]}" title="Zhang(A \rightarrow B) = \frac{Support(A\&B)-Support(A)Support(B)} {Max[Support(AB)(1-Support(A)), Support(A)Support(B)-Support(AB)]}" /></a>
</p>

#### Computing
```python
# Compute the numerator
num = supportHP - supportH * support P
```
```python
# Compute the numerator
denom = max(supportHP * (1-supportH), supportH * (supportP - support(HP))
```
```python
# Compute Zhang's metric
zhang = num / denom
```



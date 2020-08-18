# Statistics

1. [Resampling Methods]()
2. [Linear Regression](#linear-regression)
3. [Central Limit Theorem (CLT)](#central-limit-theorem)
4. [Law of Large Numbers](#law-of-large-numbers)

## Linear Regression
### Assumptions


## Central Limit Theorem (CLT)
_With a **large** enough collection of **samples** from the same population, the **sample means** will be **normally distributed**_
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/IllustrationCentralTheorem.png/400px-IllustrationCentralTheorem.png">
</p>

- Don't make any assumptions about the underlying distribution of the data
- With a large sample of 30+, the theorem will always ring true
- Usage: perform hypothesis test

## Law of Large Numbers
_As the **size of a sample is increased**, the **estimate of the sample mean** will **more accurately** reflect the population mean_

<img src="images/law-of-large-numbers.png" height="200px">

### Sampling
- A sample is a collection of data from a certain population that is meant to represent the whole

### Confidence Intervals
_A range of values that we are fairly sure includes the true value of an unknown population parameter_
- Has an associated confidence level that represents the frequency in which the interval will contain this value
- Mean: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\bar{X}\pm&space;Z_{\frac{\alpha}{2}}\frac{\sigma&space;}{\sqrt{n}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\bar{X}\pm&space;Z_{\frac{\alpha}{2}}\frac{\sigma&space;}{\sqrt{n}}" title="\bar{X}\pm Z_{\frac{\alpha}{2}}\frac{\sigma }{\sqrt{n}}" /></a>
- Proportions: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\hat{p}&space;\pm&space;Z_{\frac{\alpha}{2}}&space;\sqrt{&space;\frac{\hat{p}(1-\hat{p})}&space;{n}&space;}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\hat{p}&space;\pm&space;Z_{\frac{\alpha}{2}}&space;\sqrt{&space;\frac{\hat{p}(1-\hat{p})}&space;{n}&space;}" title="\hat{p} \pm Z_{\frac{\alpha}{2}} \sqrt{ \frac{\hat{p}(1-\hat{p})} {n} }" /></a>
- Margin of error: the part after the <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\pm" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\pm" title="\pm" /></a> sign, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;=\text{Standard&space;Error}\times&space;\text{z-score}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;=\text{Standard&space;Error}\times&space;\text{z-score}" title="=\text{Standard Error}\times \text{z-score}" /></a>

```python
from scipy.stats import sem, t
data = [1, 2, 3, 4, 5]
confidence = 0.95

# Compute the standard error and margin of error
std_err = sem(data)
margin_error = std_err * z_score

# Compute and print the lower threshold
lower = sample_mean - margin_error
print(lower)

# Compute and print the upper threshold
upper = sample_mean + margin_error
print(upper)
```



# Statistics

1. [Resampling Methods]()
2. [Linear Regression Assumptions](#linear-regression-assumptions)
3. [Central Limit Theorem (CLT)](#central-limit-theorem)
4. [Law of Large Numbers](#law-of-large-numbers)

## Linear Regression Assumptions
### 1. Linearity
_Linear relationship between the independent and dependent variables_
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Y=\beta_{0}&plus;\beta{1}X&plus;\epsilon\text{(Error&space;term)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Y=\beta_{0}&plus;\beta{1}X&plus;\epsilon\text{(Error&space;term)}" title="Y=\beta_{0}+\beta{1}X+\epsilon\text{(Error term)}" /></a>
</p>

#### Detection
Residual plots  (against X), nicely and event spread

### 2. No or little Multicollinearity
_Independent variables are not highly correlated with each other_

#### Why 
- Undermines the statistical significance of an independent variable
- Regression coefficient represents the mean change in  the dependent variable for each 1 unit change in an independent variable when all of the other independent variables constant
- The coefficients become very sensitive to small changes in the model
- Reduces the precision of the estimate coefficients

#### Detection
- VIF (Variance Inflation Factor), VIF > 5/10 = multicollinearity
- Correlation matrix, heatmap, pairplots

#### Solution
Remove independent variables with high VIF values

### The Error Term Assumptions
_Investigated with plots of the observed individuals against X/y_ 

<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;e_{i}\text{(Residual)}=Y_{i}(Observed)-&space;\hat{Y}_i&space;\text{(Predicted&space;Value)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;e_{i}\text{(Residual)}=Y_{i}(Observed)-&space;\hat{Y}_i&space;\text{(Predicted&space;Value)}" title="e_{i}\text{(Residual)}=Y_{i}(Observed)- \hat{Y}_i \text{(Predicted Value)}" /></a>
</p>

#### 3. Normally distributed
- When size is large, doesn't matter, apply central limit theorem

#### Detection
- Normality test: e.g. Shapiro-Wilk
- Histogram/QQ plot of residuals
- Scatter plot of residuals against X, should get vertical cross sections of each X value, most of the data should be centered around the 0 line

<img src="images/Normality.png" height="150px">

#### Solution
Change functional form, e.g. log

#### Detection
- Normality test
- QQ plot of residuals

### 4. Homoscedastic 
_Has constant variance at every value of X_

- `/hoʊmoʊsɪdæsˈtɪk/`

**Example**

When income is small, the variance of spending is small. When income increases, the variance increases as some may spend little while others may spend a lot.

<img src="images/Homoscedastic.png" height="150px">

#### Detection
- Scatter plot: residuals are equal across the regression line

#### Solution
- Log things

### 5. Independent - No Autocorrelation
_When there's a natural order of X_

**Example**

Stock price is not independent from the previous price

<img src="images/Autocorrelation.png" height="150px">

#### Detection
- Scatterplot
- Durbin-Watson’s d tests
  - the statistic will always be between 0 and 4
  - closer to 0, more positive serial correlation
  - closer to 4, more negative serial correlation

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



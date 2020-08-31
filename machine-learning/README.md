# Machine Learning
_Giving computers the ability to learn, to make decisions from data without being explicitly programmed_

- [Machine Learning Types](#)
- [Classfication](#classfication)
    - [k-Nearest Neighbors (kNN)](#k-nearest-neighbors-knn)
- [Regression Models](#regression-models)
    - [Assumptions](#assumptions)
    - [Logistic Regression](#logistic-regression)
- [Interpreting Models](#interpreting-models)
    - [Coefficients](#coefficients)
    - [Significance Testing](#significance-testing)
    - [Confidence Interval](#confidence-interval)
- [Evaluating Models](#evaluating-models)
    - [Recall](#recall)
    - [Precision](#precision)
    - [Confusion Matrix](#confusion-matrix)
- [Comparing Models](#comparing-models)
- [Handling Missing Data and Outliers](#handling-missing-data-and-outliers)
- [Bias-Variance Tradeoff](#bias-variance-tradeoff)

## Machine Learning Types
### Supervised
_Use labeld data_

### Unsupervised
_Uncovering hidden patterns from unlabeled data_

### Reinforcement Learning
_Learn how to optimize behavior given a system of rewards and punishments_
- Application: AlphaGo

## Classification
### k-Nearest Neighbors (kNN)
_Predict the label of data by looking at the K closest labeled data points and getting them vote the majority_
```python
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbor=6)
knn.fit(y, x)
prediction = knn.predict(X_new)
```

## GLM
_A generalization of linear models, a unified framework for different data distributions_

### Linear Model
```python
from statsmodels.formula.api import ols
model = ols(formula='y ~ X',  data=my_data).fit()
```
### GLM
```python
import statsmodels.api as sm
from statsmodels.formula.api import glm
```
- `family`: the probability distribution of the response variable
- Binomial GLM: for binary data
```python
model=glm(formula='y~X',  data=my_data, family=sm.families.___).fit()
```
### Assumptions
- Linear in parameters
- Errors are independent and normally distributed
- The variance around the regression line is constant  for all values of x

## Regression Models
_How much the response variable y changes on average for a unit increase in x_

### Linear Regression
<img src="https://miro.medium.com/max/2872/1*k2bLmeYIG7z7dCyxADedhQ.png" height="200px">

```python
from sklearn.linear_model import LinearRegression 
X_train = np.array(weather['Humidity9am']).reshape(-1,1)
y_train = weather['Humidity3pm']

# Create and fit your linear regression model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Assign and print predictions
preds = lm.predict(X_train)
```

### Logistic Regression
_Compute the probabilities that each observation belong to a class using the sigmoid function_

```python
from sklearn.linear_model import LogisticRegression

# Create and fit your model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Compute and print the accuracy
acc = clf.score(X_test, y_test)
```
#### Sigmoid/Logistic Function
_S-shaped curve that takes any real number and maps it between 0 and 1_
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;f(x)=\frac{1}{1&plus;e^{-x}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;f(x)=\frac{1}{1&plus;e^{-x}}" title="f(x)=\frac{1}{1+e^{-x}}" /></a>

#### Multicollinearity
_Varibles are correlated with others_
- Increase in standard errors of coefficients
    - Coefficients may not be statistically significant
- Check
    - Coefficient is not significant, but variable is highly correlated with y
    - Adding/removing a variable significantly changes coefficients
    - High pairwise correlation
- Variance Inflation Factor (VIF)
    - How inflated the variance of the coefficient is compared to what it would be if the variables were not correlated with any other variable in the model
    - Thresohold VIF > 2.5

#### Interaction Terms
_The effect of x1 on the response depends on the level of x2_


## Interpreting Models
### Maximum Likelihood Estimation (MLE)
_Obtain the values of betas, the parameters, which maximize the log-likelihood function (the probability of the observed data)_

### Coefficients
- Regression coefficients are obtained by the maximum likelihood estimation
- Linear
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mu=-0.114&plus;0.32\times&space;weight" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mu=-0.114&plus;0.32\times&space;weight" title="\mu=-0.114+0.32\times weight" /></a>

- Logistic
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;log(odds)=-3.69&plus;1.8\times&space;weight" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;log(odds)=-3.69&plus;1.8\times&space;weight" title="log(odds)=-3.69+1.8\times weight" /></a>
  
### Significance Testing
_Whether constraining the parameter values to zero would reduce the model fit_
- z-statistic
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;z=\hat{\beta}/SE" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;z=\hat{\beta}/SE" title="z=\hat{\beta}/SE" /></a>
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\hat{\beta}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\hat{\beta}" title="\hat{\beta}" /></a>: estimated coefficient
  - rule of thumb: if > 2 is statistically significant
  - z large -> coefficient <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\neq" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\neq" title="\neq" /></a> 0 -> variable significant

### Confidence Intervals
_Uncertainty of the estimates_
- 95% confidence intervals
    - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;[\hat{\beta}-1.96\times&space;SE,&space;\hat{\beta}&plus;1.96&space;\times&space;SE]" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;[\hat{\beta}-1.96\times&space;SE,&space;\hat{\beta}&plus;1.96&space;\times&space;SE]" title="[\hat{\beta}-1.96\times SE, \hat{\beta}+1.96 \times SE]" /></a>
    - If we repeat the experiment over and over again, we would expect the interval to cover the true value in the population 95% of the time. 95% of intervals constructed contain the true mean.

- e.g. The change in the log off can be as small as ___ (lower) or as much as ___ (upper)
- Extracting the confidence interval
  ```python
  model_GLM.conf_int())
  ```

## Evaluating Models
### Regression Technique
- R-squared
- Mean absolute error (MAE)
- Mean squared error (MSE)

#### R-squared
_Proportionn of variance of the dependent variable that is explained by the regression model_

<img src="https://miro.medium.com/max/930/1*1e3R1SFu1kU9GdWXEKPPjg.png" height="200px">

```python
r2 = lm.score(X, y)
```

#### Mean squared error (MSE)
_Sum of the residuals squared over the number of points_
- scaling exponentially

```python
mse = mean_squared_error(y, preds)
```

#### Mean absolute error (MAE)
_Sum of the absolute residuals over the number of points_
- scaling linearly

<img src="https://miro.medium.com/max/2100/1*JTC4ReFwSeAt3kvTLq1YoA.png" height="200px">

```python
mae = mean_absolute_error(y, preds)
```

#### MAE vs. MSE
- MSE: if the dataset has outliers / worried about individual observations, since by squaring the errors, they are weighted more heavily
- MAE: aren't concerned the above, suppress those errors a bit more

### Classification Technique
- Precision
- Recall
- Confusion Matrices

#### Precision
_Percentage of observation you correctly guessed, linked to Type I error_
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" title="\text{Precision}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Positive}}" /></a>

```python
precision = precision_score(y_test, preds)
```

#### Recall
_Linked to Type II error_

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" title="\text{Recall}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Negative}}" /></a>

```python
recall = recall_score(y_test, preds)
```

#### Confusion Matrix
_How many observations the model classfied correctly and incorrectly_
<img src="https://miro.medium.com/max/2692/1*I7KT0RgsHaWf0KZETJf56g.png" height="150px">

```python
pd.crosstab(y_actual,  y_predicted, rownames=['Actual'], colnames=['Predicted'], margins=True)
```

```python
matrix = confusion_matrix(y_test, preds)
```

## Comparing Models
### Goodness of Fit
_Whether the model is correctly specified and if we add more complexity would it be better_
- complexity: adding more variables, non-linear or interaction terms

### Deviance
- Formula: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;D=-2Log&space;Likelihood(\beta)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;D=-2Log&space;Likelihood(\beta)" title="D=-2Log Likelihood(\beta)" /></a>
- Measure of error
- Lower deviance: better model fit
- Benchmark: null deviance -> intercept-only model
```python
model.null_deviance
model.deviance
```
- Evaluate
    - Adding p predictors to the model, deviance should decrease by more than p

## Complexity
_The number of parameters_
- A lower deviance does not necessarily mean a better fit, may be overfitting and has worse fit on new data


## Handling Missing Data and Outliers
### Missing Data
- Dropping row: could lose a significant portion of information 
  ```python
  df.dropna(inplace=True)
  ```
- Impute missing values
  - constant value
  - randomly selected record
  - mean, median, or mode
  - use another model to predict the value

### Outliers
- Standard deviations/z-score
  - Falls outside of 3 standard deviations of the mean is deemed an outlier
- Interquartile range (IQR)
  - Subtracting the first quartile from the third quartile
  <img src="https://naysan.ca/wp-content/uploads/2020/06/box_plot_ref_needed.png" height="200px">

## Bias-Variance Tradeoff
### Types of error
- Bias error
- Variance error
- Irreducible error

### Bias
_Simplifying assumptions made by a model to make the target function easier to learn_
- High bias makes algorithm faster to learn and easier to understand but less flexible
- Too much bias could lead to under-fitting
- Example: Linear Regression, LDA, Logistic Regression

### Variance
_The amount that the estimate of the target function would change if different training data was used_
- Too much variance will lead to overfitting, too flexible, not generalizable
- Example: Decision Trees, k-Nearest Neighbors, and Support Vector Machines

### Bias-variance tradeoff
<img src="https://lh3.googleusercontent.com/proxy/dImKqPBtSGfgp7VYrRm3GfgDaYB1FF11sLKDjpu7KH1CRENchNK8cnPlw3LDzZyT7HKrIbI8ApZdIXpSFu3-hxSVTKhJg8UjbY7NxvZ_5qbaZ3mo0HouBxS-CrqW" height="300px">

- Increase the bias will decrease the variance


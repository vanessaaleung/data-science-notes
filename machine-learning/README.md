# Machine Learning
1. [Regression Models](#regression-models)
2. [Evaluating Models](#evaluating-models)
3. [Handling Missing Data and Outliers](#handling-missing-data-and-outliers)
4. [Bias-Variance Tradeoff](#bias-variance-tradeoff)

## Linear Regression
_A generalization of linear models_

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

#### Confusion Matrices
<img src="https://miro.medium.com/max/2692/1*I7KT0RgsHaWf0KZETJf56g.png" height="150px">

```python
matrix = confusion_matrix(y_test, preds)
```

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


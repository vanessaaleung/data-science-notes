# Machine Learning
1. [Regression Models](#regression-models)
2. [Evaluating Models](#evaluating-models)

## Regression Models
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

#### Mean squared error (MSE)
_Sum of the residuals squared over the number of points_
- scaling exponentially

#### Mean absolute error (MAE)
_Sum of the absolute residuals over the number of points_
- scaling linearly

<img src="https://miro.medium.com/max/2100/1*JTC4ReFwSeAt3kvTLq1YoA.png" height="300px">

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

#### Recall
_Linked to Type II error_

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" title="\text{Recall}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Negative}}" /></a>

#### Confusion Matrices
<img src="https://miro.medium.com/max/2692/1*I7KT0RgsHaWf0KZETJf56g.png" height="300px">






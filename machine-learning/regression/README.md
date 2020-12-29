# Regression Models
_How much the response variable y changes on average for a unit increase in x_

- [Linear Regression](#linear-regression)
- [Logistic Regression](#logistic-regression)

## GLM
_A generalization of linear models, a unified framework for different data distributions_
```python
import statsmodels.api as sm
from statsmodels.formula.api import glm
```
- `family`: the probability distribution of the response variable
- Binomial GLM: for binary data
```python
model=glm(formula='y~X',  data=my_data, family=sm.families.___).fit()
```

## Linear Model
```python
from statsmodels.formula.api import ols
model = ols(formula='y ~ X',  data=my_data).fit()
```

## Linear Regression
_Fits a linear model with coefficients to minimize the residual sum of squares between the targets and the predicted values by linear approximation_
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
### Assumptions

https://github.com/vanessaaleung/DS-notes/tree/master/statistics#linear-regression-assumptions

- How to fit
    - Define an error functions for any given line, choose the line that minimizes the error/loss/cost function
    - Minimize the vertical distance between the fit and the data - residual
    - Minimize the sum  of the squares of the residuals - OLS (Ordinary Least Square)


## Logistic Regression
_Compute the **probabilities** that each observation belong to a class using the sigmoid function_

```python
from sklearn.linear_model import LogisticRegression

# Create and fit your model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Compute and print the accuracy
acc = clf.score(X_test, y_test)
```

### Assumptions
1. The outcome is binary
2. Linear relationship between the logit of the outcome and the predictors. Logit function: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;logit(p)=log(\frac{p}{1-p})" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;logit(p)=log(\frac{p}{1-p})" title="logit(p)=log(\frac{p}{1-p})" /></a>
    - p: probability of the outcome
3. No outliers/extreme  values in the continuous predictors
4. No multicollinearity among the predictors

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

### Receiver Operating Characteristics Curve (ROC Curve)
_The set of points when trying all possible thresholds_

<img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2018/08/ROC-Curve-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model.png" height="300px">

### Area Under the ROC Curve (AUC)
- The larger, the better

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(logreg, X, y, cv=5, scoring='roc_auc'
```

## Interaction Terms
_The effect of x1 on the response depends on the level of x2_

##  Cross-validation
- Why: the R-squared is dependent on the way splitting up the data, the test data may not be representative of the model's ability to generalize the unseen data
- more folds, more computationally  expensive
- split data into training and hold-out set, perform grid search cross-validation on training set

## Regularized Regression
_Penalizing large coefficients_
- Why: large coefficients can lead overfitting

### Ridge Regression
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\alpha_i^2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\alpha_i^2" title="\text{Loss function}=\text{OLS loss function} + \alpha \times \sum_{i=1}^{n}\alpha_i^2" /></a>
- Alpha: Parameter we need to choose, controls model complexity
    - Alpha = 0: get back OLS
    - High alpha: lead to underfitting

### Lasso Regression
-  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\mid&space;\alpha_i\mid" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\mid&space;\alpha_i\mid" title="\text{Loss function}=\text{OLS loss function} + \alpha \times \sum_{i=1}^{n}\mid \alpha_i\mid" /></a>
- Usage: select important features of a dataset, shrinks the coefficients of less important  features to exactly 0

```python
from sklearn.linear_model import Lasso
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X, y).coef_
```

# Machine Learning
_Giving computers the ability to learn, to make decisions from data without being explicitly programmed_

- [Machine Learning Types](#machine-learning-types)
- [Families of ML algorithms](#families-of-ml-algorithms)
    - [Linear](#linear)
    - [Tree-based Models](https://github.com/vanessaaleung/DS-notes/tree/master/machine-learning/tree-models)
    - [k-Nearest Neighbors (kNN)](#k-nearest-neighbors-knn)
    - Neural Networks
    
- [Regression Models](#regression-models)
    - [Linear Regression](#linear-regression)
    - [Logistic Regression](#logistic-regression)
        - [Receiver Operating Characteristics Curve (ROC Curve)](#receiver-operating-characteristics-curve-roc-curve)
    - [Cross Validation](#cross-validation)
    - [Regularized Regression](#regularized-regression)
    - [Interaction Terms](#interaction-terms)
    
- [Interpreting Models](#interpreting-models)
    - [Coefficients](#coefficients)
    - [Significance Testing](#significance-testing)
    - [Confidence Intervals](#confidence-intervals)
    
- [Evaluating Models](#evaluating-models)
    - [Recall](#recall)
    - [Precision](#precision)
    - [Confusion Matrix](#confusion-matrix)
    
- [Comparing Models](#comparing-models)
    - [Goodness of Fit](#goodness-of-fit)
    - [Deviance](#deviance)
    
- [Preprocessing](#preprocessing)
    - [Missing Data](#handling-missing-data)
    - [Numeric Features](#numeric-features)
        - Outliers
        - Centering and Scaling
    - [Categorical and Ordinal Features](#categorial-and-ordinal-features)
        - Label Encoding
        - Frequency Encoding
        - One-hot Encoding
        - Interactions of Categorical Features
    - [Datetime and Coordinates](#datetime-and-coordinates)
        
- [Bias-Variance Tradeoff](#bias-variance-tradeoff)

## Machine Learning Types
### Supervised
_Use labeld data_

### Unsupervised
_Uncovering hidden patterns from unlabeled data_

### Reinforcement Learning
_Learn how to optimize behavior given a system of rewards and punishments_
- Application: AlphaGo

## Families of ML algorithms
- the most powerful methods are Gradient Boosted Decision Trees and Neural Networks
### Linear
_Separate objects with a plane which divides space into two parts_
- Good for sparse, high-dimensional data
- Examples
    - Logistic Regression
    - Support Vector Machines

### Tree-based
- [Link](https://github.com/vanessaaleung/DS-notes/blob/master/machine-learning/tree-models/tree-models.md)
- Good for tabular data, hard to capture linear dependencies
- Examples
    - Decision Tree: Use divide-and-conquer approach to recur sub-split spaces into sub-spaces
    - Random Forest
    - GBDT
- ExtraTrees: randomized trees, always tests random splits over fraction of features (Random forest tests all possible splits over fraction of features)

### k-Nearest Neighbors (kNN)
_Find k-nearest objects and select the label by majority vote_
- classification method
- Assume points close to each other are likely to have similar labels
- Heavily rely on how to measure "closeness"
```python
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbor=6)
knn.fit(y, x)
prediction = knn.predict(X_new)
```

- Larger k: smoother decision boundary, less complex
- Smaller k: more complex model, may be overfitting

## Regression Models
_How much the response variable y changes on average for a unit increase in x_

### GLM
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

### Linear Model
```python
from statsmodels.formula.api import ols
model = ols(formula='y ~ X',  data=my_data).fit()
```

#### Assumptions
- Linear in parameters
- Errors are independent and normally distributed
- The variance around the regression line is constant  for all values of x

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

- How to fit
    - Define an error functions for any given line, choose the line that minimizes the error/loss/cost function
    - Minimize the vertical distance between the fit and the data - residual
    - Minimize the sum  of the squares of the residuals - OLS (Ordinary Least Square)


### Logistic Regression
_Compute the **probabilities** that each observation belong to a class using the sigmoid function_

```python
from sklearn.linear_model import LogisticRegression

# Create and fit your model
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Compute and print the accuracy
acc = clf.score(X_test, y_test)
```

#### Assumptions
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

#### Receiver Operating Characteristics Curve (ROC Curve)
_The set of points when trying all possible thresholds_

<img src="https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2018/08/ROC-Curve-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model.png" height="300px">

#### Area Under the ROC Curve (AUC)
- The larger, the better

```python
from sklearn.model_selection import cross_val_score
cv_scores = cross_val_score(logreg, X, y, cv=5, scoring='roc_auc'
```

### Interaction Terms
_The effect of x1 on the response depends on the level of x2_

###  Cross-validation
- Why: the R-squared is dependent on the way splitting up the data, the test data may not be representative of the model's ability to generalize the unseen data
- more folds, more computationally  expensive
- split data into training and hold-out set, perform grid search cross-validation on training set

### Regularized Regression
_Penalizing large coefficients_
- Why: large coefficients can lead overfitting

#### Ridge Regression
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\alpha_i^2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\alpha_i^2" title="\text{Loss function}=\text{OLS loss function} + \alpha \times \sum_{i=1}^{n}\alpha_i^2" /></a>
- Alpha: Parameter we need to choose, controls model complexity
    - Alpha = 0: get back OLS
    - High alpha: lead to underfitting

#### Lasso Regression
-  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\mid&space;\alpha_i\mid" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Loss&space;function}=\text{OLS&space;loss&space;function}&space;&plus;&space;\alpha&space;\times&space;\sum_{i=1}^{n}\mid&space;\alpha_i\mid" title="\text{Loss function}=\text{OLS loss function} + \alpha \times \sum_{i=1}^{n}\mid \alpha_i\mid" /></a>
- Usage: select important features of a dataset, shrinks the coefficients of less important  features to exactly 0

```python
from sklearn.linear_model import Lasso
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X, y).coef_
```

## Interpreting Models
### Maximum Likelihood Estimation (MLE)
_Obtain the values of betas, the parameters, which maximize the log-likelihood function (the probability of the observed data)_

### Coefficients
- Regression coefficients are obtained by the maximum likelihood estimation
- Linear
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\mu&space;=&space;-0.114&space;&plus;&space;0.32&space;\times&space;weight" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\mu&space;=&space;-0.114&space;&plus;&space;0.32&space;\times&space;weight" title="\mu = -0.114 + 0.32 \times weight" /></a>

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
- penalize more when the prediction is way off
```python
mse = mean_squared_error(y, preds)
```
- Root mean squared error (RMSE): <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{\sum_{i=1}^{n}(y_i&space;-&space;x_i)^2}{n}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{\sum_{i=1}^{n}(y_i&space;-&space;x_i)^2}{n}" title="\frac{\sum_{i=1}^{n}(y_i - x_i)^2}{n}" /></a>

#### Mean absolute error (MAE)
_Sum of the absolute residuals over the number of points_
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{\sum_{i=1}^{n}\left&space;|&space;y_i&space;-&space;x_i&space;\right&space;|}{n}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{\sum_{i=1}^{n}\left&space;|&space;y_i&space;-&space;x_i&space;\right&space;|}{n}" title="\frac{\sum_{i=1}^{n}\left | y_i - x_i \right |}{n}" /></a>
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

#### Accuracy
- Friction of correct predictions

#### Precision
_Percentage of observation you correctly guessed, linked to Type I error_
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" title="\text{Precision}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Positive}}" /></a>

```python
precision = precision_score(y_test, preds)
```
- e.g. high precision: not many real emails predicted as spam

#### Recall
_Linked to Type II error_

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" title="\text{Recall}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Negative}}" /></a>

```python
recall = recall_score(y_test, preds)
```
- predicted most spam emails correctly

#### F1 Score
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;2\times\frac{precision\times&space;recall}{precision&space;&plus;&space;recall}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;2\times\frac{precision\times&space;recall}{precision&space;&plus;&space;recall}" title="2\times\frac{precision\times recall}{precision + recall}" /></a>

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

### Complexity
_The number of parameters_
- A lower deviance does not necessarily mean a better fit, may be overfitting and has worse fit on new data

## Preprocessing
- Tree-based models don't depend on scaling

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

### Numeric features
#### Outliers
- Standard deviations/z-score
  - Falls outside of 3 standard deviations of the mean is deemed an outlier
- Interquartile range (IQR)
  - Subtracting the first quartile from the third quartile
  <img src="https://naysan.ca/wp-content/uploads/2020/06/box_plot_ref_needed.png" height="200px">
  
#### Centering and Scaling
- Scaling = Normalizing = Centering
- Why scaling
    - Features on larger scales can influence the model
    - e.g. kNN uses distance when making predictions
- Ways
    - Standardization: subtract the mean and divide by variance - center around 0 with variance 1
    - Min-Max: subtract the minimum and divide by the range - range will be [0, 1], distribution won't change
    - Normalize:  [-1, 1]
    - Rank: better with outliers situation, will move outliers closer, set space between sorted values to be equal
    - Log transformation: np.log(1+x)
    - Raising to the power < 1: np.sqrt(x + 2/3)

### Categorical and Ordinal Features
#### Label Encoding
_Works fine with tree-methods_
- Alphabetical (sorted): [S,C,Q] -> [2,1,3],  ```python sklearn.preprocessing.LabelEncoder```
- Order of Appearance: [S,C,Q] -> [1,2,3], ```python pandas.factorize```

#### Frequency Encoding
- can help for non-tree based models, will reserve information about values distribution
- [S,C,Q] -> [0.5, 0.3, 0.2]
```python
encoding = titanic.groupby('Embarked').size()
encoding = encoding/len(titanic)
titanic['enc'] = titanic.Embarked.map(encoding)
```

#### One-hot Encoding
- often used for non-tree-based models, tree-models will slow down
    - if the categorical features have too many unique values, will add too many new columns with a few non-zero values
- ```python sklearn.preprocessing.OneHotEncoder```
- ```python pandas.get_dummies```
- **Sparse Matrices**: useful when work with categorical features/text data, only store non-zero values

#### Interactions of Categorical Features
- can help linear models and KNN

### Datetime and Coordinates
#### Datetime Feature Generation
- Periodicity: day number in week, month, season, year, etc.
- Time since: number of days left until next holidays/ time passed after last holiday
- Difference between dates

#### Coordinates Feature Generation
- interesting places and add distance to the places
- center of clusters
- aggregated statistics: mean realty prices
- high/low price district

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


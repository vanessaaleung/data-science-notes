# Machine Learning
_Giving computers the ability to learn, to make decisions from data without being explicitly programmed_

- [Machine Learning Types](#machine-learning-types)
    - [Parametric vs Nonparametric](#parametric-vs-nonparametric)
- [Families of ML algorithms](#families-of-ml-algorithms)
    - [Linear](#linear)
    - [Tree-based Models](https://github.com/vanessaaleung/DS-notes/tree/master/machine-learning/tree-models)
    - [k-Nearest Neighbors (kNN)](#k-nearest-neighbors-knn)
    - Neural Networks
    - [Clustering](https://github.com/vanessaaleung/DS-notes/tree/master/machine-learning/clustering)
    - [Regression Models](https://github.com/vanessaaleung/DS-notes/tree/master/machine-learning/regression)

- [Interpreting Models](#interpreting-models)
    - [Coefficients](#coefficients)
    - [Significance Testing](#significance-testing)
    - [Confidence Intervals](#confidence-intervals)
    
- [Evaluating Models](#evaluating-models)
    - [R-squared](#r-squared)
    - [Adjusted R-squared](#adjusted-r-squared)
    - [Recall](#recall)
    - [Precision](#precision)
    - [Confusion Matrix](#confusion-matrix)
    
- [Comparing Models](#comparing-models)
    - [Goodness of Fit](#goodness-of-fit)
    - [Deviance](#deviance)
    
- [Feature Preprocessing and Generation](https://github.com/vanessaaleung/DS-notes/blob/master/machine-learning/preprocessing.md)
        
- [Bias-Variance Tradeoff](#bias-variance-tradeoff)

## Machine Learning Types
### Supervised
_Use labeled data_

### Unsupervised
_Uncovering hidden patterns from unlabeled data_

### Reinforcement Learning
_Learn how to optimize behavior given a system of rewards and punishments_
- Application: AlphaGo

### Parametric vs Nonparametric
- Parametric: a model that summarizes data with a set of parametrers of fixed size (independent of # of training examples)
    - simpler, faster, less data
- Nonparametric: do not make strong assumptions about the form of the mapping function
    - good when have a lot of data, no prior knowledge
    - e.g. K-nearest neighbors, Decision trees, Support Vector Machines

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
  - <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;z&space;=&space;\frac{\hat{\beta}}{SE}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;z&space;=&space;\frac{\hat{\beta}}{SE}" title="z = \frac{\hat{\beta}}{SE}" /></a>
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
_Proportion of variance of the dependent variable that is explained by the regression model_

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;1-\frac{\text{residual&space;sum&space;of&space;squares}}{\text{total&space;sum&space;of&space;squares}}&space;=&space;1-\frac{((y_{true}-&space;y_{pred})^2).sum()}{((y_{true}-y_{true}.mean())^2).sum()}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;1-\frac{\text{residual&space;sum&space;of&space;squares}}{\text{total&space;sum&space;of&space;squares}}&space;=&space;1-\frac{((y_{true}-&space;y_{pred})^2).sum()}{((y_{true}-y_{true}.mean())^2).sum()}" title="1-\frac{\text{residual sum of squares}}{\text{total sum of squares}} = 1-\frac{((y_{true}- y_{pred})^2).sum()}{((y_{true}-y_{true}.mean())^2).sum()}" /></a>

<img src="https://www.riskprep.com/images/stories/miscimages/regressiongraph.png" height="300px">

```python
r2 = lm.score(X, y)
```

#### Adjusted R-squared
- Why: every additional independent variable added to a model always increases the R-squared value
- Adjusted R-squared only increases if each given variable improves the model above what is possible by probability

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
_Proportion of positive identifications was actually correct_
- linked to Type I error

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Precision}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Positive}}" title="\text{Precision}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Positive}}" /></a>

```python
precision = precision_score(y_test, preds)
```
- e.g. high precision: not many real emails predicted as spam

#### Recall
_Proportion of actual positives identified correctly_

- Linked to Type II error

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Recall}=\frac{\text{True&space;Positive}}{\text{True&space;Positive}&plus;\text{False&space;Negative}}" title="\text{Recall}=\frac{\text{True Positive}}{\text{True Positive}+\text{False Negative}}" /></a>

```python
recall = recall_score(y_test, preds)
```
- predicted most spam emails correctly

<img src="https://miro.medium.com/max/942/0*MvoEw2m0KTIQlYmD.png">

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


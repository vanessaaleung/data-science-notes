#  Tree-Based Models
_Infer class labels, Capture non-linear relationships between features and labels_
- Don't require feature scaling

1. [Decision Tree](#decision-tree)
2. [The Bias-Variance Tradeoff](#the-bias-variance-tradeoff)
    - [Ensemble Learning](#ensemble-learning)
3. [Bagging and Random Forest](#bagging-and-random-forest)
    - [Bagging](#bagging)
    - [Random Forest](#random-forest)
4. [Boosting](#boosting)
    - [AdaBoost](#adaboost)
    - [Gradient Boosting](#gradient-boosting-gb)
    - [Stochastic Gradient Boosting](#stochastic-gradient-boosting)
5. [Model Tuning](#model-tuning)

## Decision Tree
_Data structure consisting of a hierarchy of nodes_
- [scikit-learn documentation](https://scikit-learn.org/stable/modules/tree.html)

<img src="https://scalar.usc.edu/works/c2c-digital-magazine-fall-2017--winter-2018/media/GolfDecisionTree.jpg" height="300px">

- Decision Region: region in the feature space where all instances are assigned to one class label
- Decision Boundary: surface separating different decision regions

<img src="https://slideplayer.com/slide/14454418/90/images/16/Decision+Boundaries+Decision+Boundary+Decision+Region+1+Decision.jpg" height="300px">

- Nodes: questions or predictions
  - Root: no parent node
  - Internal node: one parent node
  - Leaf: one parent node, no children nodes  -> prediction
- Maximum depth: the number of branches separating from the top to the extreme end

### Advantages
- easy to interpret and visualize
- the cost is logarithmicc in the number of data points used in training
- requires little data preparation
- **does not support missing values**

### Disadvantages
- overfitting
    - setting the minimum number of samples required at a leaf node
    - pruning
    - setting the maximum depth of the tree
- unstable: small variations in the data might result in a different tree being generated
- create biased trees if some classes dominate
    - balance the dataset before fitting the tree

### Logistic regression vs classification tree
- A classification tree divides the feature space into rectangular regions. 
- A linear model such as logistic regression produces only a single linear decision boundary dividing the feature space into two decision regions

<img src="logreg_tree.svg" height="300px">

### Information Gain
- Every node contains information and aims at maximizing Information Gain obtained after each split
- At each node, split data based on feature f and split-point sp to maximize IG(node)
- Meaure impurity of a node I
  - gini index
  - entropy
  
```python
dt = DecisionTreeClassfier(criterion='gini', random_state=1)
```

### Decision Tree for Regression
_Capture the non-linear relationship_

- min_samples_leaf: each leaf has to contain at least 10% of the training data

```python
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.1, random_state=1)
```

- The impurity is measured using  the mean-squared error of the targets
  - Find the splits that produce leats where in each leaf the target value on average, the closest possible to the mean-value of the labels in that leaf
- Prediction: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\hat{y}_{pred}(leaf)=\frac{1}{N_{leaf}}\sum_{i&space;\epsilon&space;leaf}^{}&space;y^{(i)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\hat{y}_{pred}(leaf)=\frac{1}{N_{leaf}}\sum_{i&space;\epsilon&space;leaf}^{}&space;y^{(i)}" title="\hat{y}_{pred}(leaf)=\frac{1}{N_{leaf}}\sum_{i \epsilon leaf}^{} y^{(i)}" /></a>


## The Bias-Variance Tradeoff
### Generalization Error
_How much the model generalizes on unseen data_

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Generalization&space;Error}&space;=&space;bias^2&space;&plus;&space;variance&space;&plus;&space;\text{irreducible&space;error}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Generalization&space;Error}&space;=&space;bias^2&space;&plus;&space;variance&space;&plus;&space;\text{irreducible&space;error}" title="\text{Generalization Error} = bias^2 + variance + \text{irreducible error}" /></a>

- Irreducible error: error contribution of noise
- Bias
  - How much the predicted value (fhat) and the true value (f) are **different**
  - High bias lead to underfitting
- Variance
  - How much the predicted value (fhat) is **inconsistent** over different training sets
  - High variance lead to overfitting
- Model Completxity
  - Sets the flexibility of the model function
  - e.g. Maximum tree depth, minimum samples per leaf

### The Bias-Variance Tradeoff
- find the model complexity with the lowest generalization error

<img src="https://lh3.googleusercontent.com/proxy/oYwXEIwKUmsBBs89hqL5XitQ5TrFQbwvk7Y7B6FO6L6z_uUzQbSYwzcfaqgc3b9K4Qve83-HBOJoH-ayYKZSuysPaZiZQVQD-c70MFrm8OaJiMDsjQpwwlS9ovd1" height="200px">

<img src="https://miro.medium.com/max/978/1*CgIdnlB6JK8orFKPXpc7Rg.png" height="300px">

### Estimating the Generalization error
1. Split the data
2. Fit the model
3. Evaluatethe error of  the model on test set
4. Generalization error is approximately equals to the test set error

### Model Evaluation with Cross-Validation
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{10-fold&space;CV&space;Error}&space;=&space;\frac{E_1&space;&plus;&space;...&plus;E_{10}}{10}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{10-fold&space;CV&space;Error}&space;=&space;\frac{E_1&space;&plus;&space;...&plus;E_{10}}{10}" title="\text{10-fold CV Error} = \frac{E_1 + ...+E_{10}}{10}" /></a>

```python
#  Set n-jobs to -1 in order to exploit all CPU cores in computation
# Multiplied by negative one since cross_val_score has only the option of evaluating the negative MSEs
MSE_CV = -cross_val_score(dt,  X_train, y_train, cv=10, scoring='neg_mean_squared_error', n_jobs=-1

print('CV MSE:', MSE_CV.mean())
print('Train MSE:', MSE(y_train, y_predict_train))
print('Test MSE:', MSE(y_test, y_predict_test))
```

- Diagnose Variance problems: CV error > training set error
  - Remedy: decrease model complexity  - decrease max depth, increase min samples per leaf, gather more data
- Diagnose Bias problems: CV error is approximately equals to training set error, but much greater than the desired error
  - Remedy: increase complexity - gather more features data

### Ensemble Learning
_Train different classfiers on the same training set, aggregate the predictions_

- Advantages of CARTs (Classification and Regression Trees) : simple to understand and interpret
- Limitations of CARTs
  - sensitive to small variations in the training set
  - Classification: only produce orthogonal decision boundaries
  - High variance: may overfit
  
#### Voting Classifier
- Train different models/classifiers on the same dataset, let each model make its predictions
- Meta-model: Aggregates predictions of individual models
- More robust, less prone to errors: if some models make predictions that are way off, the other models should compensate these errors

<img src="ensemble-learning.png" height="300px">

```python
from sklearn.ensemble import VotingClassifier
# Define a list that contains (classifier_name, classifier)
classifiers = [('Logistic Regression', lr),
                ('K Nearest Neighbours', knn)]
# Instantiate a Voting Classifier 'vc'
vc = VotingClassifier(estimators=classfiers)
vc.fit(X_train, y_train)
y_pred = vc.predict(X_test)
```

## Bagging and Random Forest
### Ensemble Methods
- Voting Classifier: different algorithms on the same training data
- Bagging: one algorithm on different subsets of training data

### Bagging
_One algorithm trained on different subset of the training set, Bootstrap Aggregation_
- Bootstrap: Draw sample from the set with replacement
- Classification problem: aggregates predictions by majority voting, `BaggingClassifier`
- Regression problem: aggregates predictions through averaging, `BaggingRegressor`

- n_estimators: number of classification trees
```python
from sklearn.ensemble import BaggingClassifier
bc = BaggingClassifier(base_estimator=dt, n_estimators=300, n_jobs=-1)
```

### Out Of Bag Evaluation
_Obtain the performance of a bagged-ensemble on unseen data without performing cross-validation_

- OOB instsances: training instances that are not sampled, used to estimate the performance
- Each model is trained on bootstrap samples and evaluated on the OOB instances

<img src="oob-evaluation.png" height="300px">

- Corresponds to accuracy score for classifiers, and r-squared score for regressors

```python
bc = BaggingClassifier(base_estimator=dt, n_estimators=300, oob_score=True, n_jobs=-1)
oob_accuracy = bc.oob_score_
```

### Random Forests
- Base estimator: Decision Tree
- Each estimator is trained on a different bootstrap sample
- further randomization in the training of individual trees
- At each node, d features are sampled without replacement (d < total number of features)
    - in scikit-learn, d defaults = the square-root of the number of features
- The node is split using the sampled feature that maximized information gain
- Final prediction
    - Majority voting for classification, `RandomForestClassifier`
    - Averaging for regression, `RandomForestRegressor`

<img src="random-forest.png" height="300px">

```python
rf = RandomeForestRegressor(n_estimator=...)
```

#### Feature Importance
- in `sklearn`: how much the tree nodes use a particular feature (weighted average) to reduce impurity
- Is expressed as a percentage indicating the weight of that feature in training and prediction

```python
importances_rf = pd.Series(rf.feature_importances_, index=X.columns)
sorted_importance_rf = importance_rf.sort_values()

# Make a horizontal bar plot
sorted_importances_rf.plot(kind='barh', color='lightgreen')
plt.show()
```

## Boosting
_An ensemble method in which many predictors are trained and each predictor learns from the **errors** of its predecessor_

- Train an ensemble of predictors sequentially
- Each predictor tries to correct its predecessor
- Combine several weak learners to form a strong learner
- Weak learner: model doing slightly better than random guessing
- Most popular boosting methods
    - AdaBoost
    - Gradient Boosting

### AdaBoost
- Adaptive Boosting
- Each predictors **pays more attention to the instances wrongly predicted by its predecessor** by **changing the weights of training instances**
- Each predictor is assigned to a coefficient alpha, which depends on the predictor's training error

<img src="adaboost.png" height="300px">

- alpha 1 is used to determine the weight 2 for predictor 2
- Incorrectly predicted instasnces acquire higher weights, shown in green
- Prediction: `AdaBoostClassifier` for classification, `AdaBoostRegressor` for regression
- Predictors need NOT to be CARTs, but CARTs are used most of the time

```python
from sklearn.ensemble imiport AdaBoostClassifier
adb_clf = AdaBoostClassifier(base_estimator=dt, n_estimators=100)

# Predict the test set probabilities of positive class
y_pred_proba = adb_clf.predict_proba(X_test)[:, 1]

adb_clf_roc_auc_score = roc_auc_score(y_test, y_pred_proba)
```

#### Learning Rate
_Shrink the coefficient alpha of a trained predictor_

- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;0&space;<&space;\eta&space;\leq&space;1" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;0&space;<&space;\eta&space;\leq&space;1" title="0 < \eta \leq 1" /></a>

<img src="learning-rate.png" height="300px">

- Tradeoff between the learning rate and the number of estimators
    - A small learning rate should be compensated by a greater number of estimators

### Gradient Boosting (GB)
- **Does not tweak the weights** of training instances
- Each predictor is trained using the residual errors of its predecessor as labels
- Base learner: CART

<img src="gradient-boosted.png" height="300px">

#### Shrinkage
_Prediction of each tree in the ensemble is shirnked after it is multiplied by a learning rate_

|GB|AdaBoost|
|---|---|
|<img src="shrinkage.png" height="300px">|<img src="learning-rate.png" height="300px">|

- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;y_{pred}=y_1&plus;\eta&space;r_1&plus;...&plus;\eta&space;r_N" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;y_{pred}=y_1&plus;\eta&space;r_1&plus;...&plus;\eta&space;r_N" title="y_{pred}=y_1+\eta r_1+...+\eta r_N" /></a>

- `GradientBoostingRegressor`, `GraidentBoostingClassifier`

### Stochastic Gradient Boosting (SGB)
- GB involves an exhaustive search procedure
- Each tree is trained on a random subset **(sampled without replacement)** of rows of the training data
- Features are sampled without replacement

|SGB|Random Forest|
|---|---|
|<img src="sgb.png" height="300px">|<img src="random-forest.png" height="300px">|

- `subsample=0.8`: each tree to sample 80% of the data for training
- `max_features=0.2`: each tree uses 20% of available features to perform the best-split
```python
sgb = GradientBoostingRegressor(max_depth=1,
                                subsample=0.8,
                                max_features=0.2,
                                n_estimators=300,
                                random_state=SEED)
```

## Model Tuning
_Find a set of optimal hyperparameters that results in an optimal model_

- Parameters: learned from data, e.g. split-point of a node
- Hyperparameters: not learned from data, set prior to training
- Approaches
    - Grid Search
    - Random Search
    - Bayesian Optimization
    - Genetic Algorithms
- For each set of hyperparameters, evaluate each model's CV score
- Computationally expensive

### Grid Search Cross Validation
_Manually set a grid of discrete hyperparameter values_

```python
from sklearn.model_selection import GridSearchCV
# Define the grid of hyperparameters
params_dt = {
            'max_depth': [3, 4, 5, 6],
            'min_samples_leaf': [0.04, 0.06, 0.08],
            'max_features': [0.2, 0.4, 0.6, 0.8]
            }
```
```python
# Instantiate a 10-fold CV grid search object
grid_dt = GridSearchCV(estimator=dt,
                        param_grid=params_dt,
                        scoring='accuracy',
                        cv=10,
                        n_jobs=-1)
```
```python
# Extract best params
grid_dt.best_params_
```

- Tuning a RF's hyperparameters
    - `verbose`: the higher its value, the more messages are printed during fitting
    - 
    ```python
    grid_rf = GridSearchCV(estimator=rf,
                            param_grid=params_rf,
                            verbose=1
                            )
    ```


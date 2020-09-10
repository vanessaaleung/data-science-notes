#  Tree-Based Models
_Infer class labels, Capture non-linear relationships between features and labels_
- Don't require feature scaling

## Decision Tree
_Data structure consisting of a hierarchy of nodes_

<img src="https://scalar.usc.edu/works/c2c-digital-magazine-fall-2017--winter-2018/media/GolfDecisionTree.jpg" height="300px">

- Decision Region: region in the feature space where all instances are assigned to one class label
- Decision Boundary: surface separating different decision regions

<img src="https://slideplayer.com/slide/14454418/90/images/16/Decision+Boundaries+Decision+Boundary+Decision+Region+1+Decision.jpg" height="300px">

- Nodes: questions or predictions
  - Root: no parent node
  - Internal node: one parent node
  - Leaf: one parent node, no children nodes  -> prediction
- Maximum depth: the number of branches separating from the top to the extreme end

```python
from sklearn.tree import DecisionTreeClassfier

dt = DecisionTreeClassfier(max_depth=2, random_state=1)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
```

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



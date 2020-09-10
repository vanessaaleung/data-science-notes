#  Tree-Based Models
_Infer class labels, Capture non-linear relationships between features and labels_
- Don't require feature scaling

## Decision Tree
<img src="https://scalar.usc.edu/works/c2c-digital-magazine-fall-2017--winter-2018/media/GolfDecisionTree.jpg" height="300px">

- Decision Region: region in the feature space where all instances are assigned to one class label
- Decision Boundary: surface separating different decision regions

<img src="https://slideplayer.com/slide/14454418/90/images/16/Decision+Boundaries+Decision+Boundary+Decision+Region+1+Decision.jpg" height="300px">

- Maximum depth: the number of branches separating from the top to the extreme  end

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

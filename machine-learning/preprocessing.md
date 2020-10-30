# Feature Preprocessing and Generation 
- [Missing Data](#handling-missing-data)
- [Numeric Features](#numeric-features)
    - Outliers
    - Centering and Scaling
- [Categorical and Ordinal Features](#categorical-and-ordinal-features)
    - Label Encoding
    - Frequency Encoding
    - One-hot Encoding
    - Interactions of Categorical Features
- [Datetime and Coordinates](#datetime-and-coordinates)

## Missing Data
- Dropping row: could lose a significant portion of information 
  ```python
  df.dropna(inplace=True)
  ```
- Impute missing values
  - constant value: -99, -1, etc.
  - randomly selected record
  - mean, median, or mode
  - use another model to predict the value
- XGBoost can handle NaN
- Avoid filling nans before feature generation

## Numeric features
### Outliers
- Standard deviations/z-score
  - Falls outside of 3 standard deviations of the mean is deemed an outlier
- Interquartile range (IQR)
  - Subtracting the first quartile from the third quartile
  <img src="https://naysan.ca/wp-content/uploads/2020/06/box_plot_ref_needed.png" height="200px">
  
### Centering and Scaling
- Tree-based models don't depend on scaling
- Scaling = Normalizing = Centering
- Why scaling
    - Features on larger scales can influence the model
    - e.g. kNN uses distance when making predictions
- Ways
    - Standardization: subtract the mean and divide by variance - center around 0 mean with variance 1
    ```python 
    from sklearn import preprocessing
    preprocessing.scale(X_train)
    ```
    - Min-Max: subtract the minimum and divide by the range - range will be [0, 1], distribution won't change
    - Normalize:  [-1, 1]
    - Rank: better with outliers situation, will move outliers closer, set space between sorted values to be equal
    - Log transformation: np.log(1+x)
    - Raising to the power < 1: np.sqrt(x + 2/3)

## Categorical and Ordinal Features
### Label Encoding
_Works fine with tree-methods_
- Alphabetical (sorted): [S,C,Q] -> [2,1,3],  
```python 
sklearn.preprocessing.LabelEncoder
```
- Order of Appearance: [S,C,Q] -> [1,2,3], 
```python 
pandas.factorize
```

### Frequency Encoding
- can help for non-tree based models, will reserve information about values distribution
- [S,C,Q] -> [0.5, 0.3, 0.2]
```python
encoding = titanic.groupby('Embarked').size()
encoding = encoding/len(titanic)
titanic['enc'] = titanic.Embarked.map(encoding)
```

### One-hot Encoding
- often used for non-tree-based models, tree-models will slow down
    - if the categorical features have too many unique values, will add too many new columns with a few non-zero values
- ```python 
    sklearn.preprocessing.OneHotEncoder
    ```
- ```python 
    pandas.get_dummies
    ```
- **Sparse Matrices**: useful when work with categorical features/text data, only store non-zero values

### Interactions of Categorical Features
- can help linear models and KNN

## Datetime and Coordinates
### Datetime Feature Generation
- Periodicity: day number in week, month, season, year, etc.
- Time since: number of days left until next holidays/ time passed after last holiday
- Difference between dates

### Coordinates Feature Generation
- interesting places and add distance to the places
- center of clusters
- aggregated statistics: mean realty prices
- high/low price district

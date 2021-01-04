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
- Methods
    - Standardization: subtract the mean and divide by variance - center around 0 mean with variance 1
    ```python 
    from sklearn import preprocessing
    preprocessing.scale(X_train)
    ```
    - Min-Max: subtract the minimum and divide by the range - range will be [0, 1], distribution won't change
    - Normalize:  [-1, 1]
    - Rank transform: better with outliers situation, will move outliers closer, set space between sorted values to be equal
    - Log transformation: np.log(1+x), move outliers relatively closer to each other
    - np.sqrt(x): move outliers relatively closer to each other
    - Raising to the power < 1: np.sqrt(x + 2/3)
    - Winsorization: remove outliers by setting all outliers to a specified percentile of the data
        - Example:
        
        Consider the data set consisting of:

        {92, 19, 101, 58, 1053, 91, 26, 78, 10, 13, −40, 101, 86, 85, 15, 89, 89, 28, −5, 41}       (N = 20, mean = 101.5)
        The data below the 5th percentile lies between −40 and −5, while the data above the 95th percentile lies between 101 and 1053. (Values shown in bold.) Then a 90% winsorization would result in the following:

        {92, 19, 101, 58, 101, 91, 26, 78, 10, 13, −5, 101, 86, 85, 15, 89, 89, 28, −5, 41}       (N = 20, mean = 55.65)
        
        ```python
        from scipy.stats.mstats import winsorize
        winsorize([92, 19, 101, 58, 1053, 91, 26, 78, 10, 13, -40, 101, 86, 85, 15, 89, 89, 28, -5, 41], limits=[0.05, 0.05])
        ```
- Decrease outliers' influence on non-tree models: Rank transform, np.log(1+x), np.sqrt(x), winsorization

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

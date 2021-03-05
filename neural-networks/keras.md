# Keras
_For quick prototyping, easy to use API_

## Model Classes
- Sequantial model
- Model class used with the functional API

## Regression Models
```python
import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
n_cols = concreate_data.shape[1]

model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(predictors, target)

predictions = model.predict(test_data)
```

### Adam Optimizer
- Don't need to specify the learnign rate

## Classification Models
```python
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

model = Sequential()
n_cols = car_data.shape[1]
target = to_categorical(target)

model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer='adam', , loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target, epochs=10)

predictions = model.predict(test_data) # output for each data point is an array of probabilities the outcome belongs to each class
```

## Save Models
```python
model.save('classification_model.h5')

from keras.model import load_model
pretrained_model = load_model('classification_model.h5')
```


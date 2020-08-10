# Resampling Methods
_Simulate multiple instances of the dataset by resamplinng it_

## Introduction
- Usage
    - Model Validationn
    - Uncertainty Estimation
    - Significance Testing
- Computationally expensive
- No strict assumptions regarding the distribution
- Methods
  - Bootstrapping
    - Most common
    - Samplingg with replacement
  - Jackknife
    - No random sampling
    - One or more observations from the original dataset are systematically exlucded in creating new datasets
    - Estimating the bias and variance of estimators
    - Linear approximation of bootstrapping
  - Permutation Testing
    - Label Switching

## Bootstrapping

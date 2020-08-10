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
- Assumption: the original sample being a reasonable representation of the population
- Bootstrapped statistics that concerning the dispersion of the data like standard deviation tend to be inherently biased
- Bias correction: e.g. balanced bootstrap
- Running a simple bootstrap
    ```python
    # Draw some random sample with replacement and append mean to mean_lengths.
    mean_lengths, sims = [], 1000
    for i in range(sims):
        temp_sample = np.random.choice(wrench_lengths, replace=True, size=len(wrench_lengths))
        sample_mean = np.mean(temp_sample)
        mean_lengths.append(sample_mean)

    # Calculate bootstrapped mean and 95% confidence interval.
    boot_mean = np.mean(mean_lengths)
    boot_95_ci = np.percentile(mean_lengths, [2.5, 97.5])
    print("Bootstrapped Mean Length = {}, 95% CI = {}".format(boot_mean, boot_95_ci))
    ```

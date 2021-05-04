# Descriptive Statistics
- [Mean](#mean)
- [Median](#median)
- [Variance + STD DEV](#variance-+-std-dev)
## Mean

## Median
_Middle number of the series when ordered_

### Mean vs Median
- Symmetric distributions: Mean =  Median
  - Uniform distribution
  - Bell curve
  - Bimodal distribution
- Asymmetric distributions
  - median is more robust/reflective of the central tendency when there're extreme values/heavily skewed
- When median is preferred
  - house prices
  - car prices
  - salaries

## Mode
## Quantiles
## Range + IQR

## Variance + STD DEV
_Describe the spread of the data_
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Variance&space;=&space;s^2&space;=&space;\frac{\sum(x-\bar{x})^2}{n-1}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Variance&space;=&space;s^2&space;=&space;\frac{\sum(x-\bar{x})^2}{n-1}" title="Variance = s^2 = \frac{\sum(x-\bar{x})^2}{n-1}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Std&space;dev&space;=&space;s&space;=&space;\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Std&space;dev&space;=&space;s&space;=&space;\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" title="Std dev = s = \sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" /></a>
- Variance: the average **squared deviation** from the **population** mean
- Why divide by n-1
  - sample mean is only one possible position for the true population mean
  - at any other position, the sum of squares would be larger
  - using n-1 instead of n would adjust the variance estimate upwards
- Degree of Freedom
  - Population variance - Three degrees of freedom (three pieces of independent information): <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sigma^2=\frac{\sum(X-\mu)^2}{N}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\sigma^2=\frac{\sum(X-\mu)^2}{N}" title="\sigma^2=\frac{\sum(X-\mu)^2}{N}" /></a>
  - Sample Variance - Two degrees of freedom: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;s^2=\frac{\sum(X-\bar{X})^2}{n-1}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;s^2=\frac{\sum(X-\bar{X})^2}{n-1}" title="s^2=\frac{\sum(X-\bar{X})^2}{n-1}" /></a>

## Coefficient of Variation

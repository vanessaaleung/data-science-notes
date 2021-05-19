# Descriptive Statistics
<p align="center">
  <img src="https://luminousmen.com/media/descriptive-and-inferential-statistics.jpeg" width="500px">
</p>

- [Median](#Median)
- [Variance](#Variance)
- [Skewness](#Skewness)

## Median
_Middle number of the series when ordered_

### Mean vs Median
- Symmetric distributions: Mean =  Median
  - Uniform distribution
  - Bell curve
  - Bimodal distribution
- Asymmetric distributions
  - median is more robust/reflective of the central tendency when there're **extreme values**/heavily skewed
- When median is preferred
  - house prices
  - car prices
  - salaries

## Variance
_Describe the **spread** of the data_
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Variance&space;=&space;s^2&space;=&space;\frac{\sum(x-\bar{x})^2}{n-1}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Variance&space;=&space;s^2&space;=&space;\frac{\sum(x-\bar{x})^2}{n-1}" title="Variance = s^2 = \frac{\sum(x-\bar{x})^2}{n-1}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Std&space;dev&space;=&space;s&space;=&space;\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Std&space;dev&space;=&space;s&space;=&space;\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" title="Std dev = s = \sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}" /></a>
- Variance: the average **squared deviation** from the **population** mean
- Why divide by n-1
  - sample mean is only one possible position for the true population mean
  - at any other position, the sum of squares would be larger
  - using n-1 instead of n would adjust the variance estimate upwards
- Degree of Freedom
  - <img src="images/degree_of_freedom.png">
  - Population variance - Three degrees of freedom (three pieces of independent information): <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sigma^2=\frac{\sum(X-\mu)^2}{N}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\sigma^2=\frac{\sum(X-\mu)^2}{N}" title="\sigma^2=\frac{\sum(X-\mu)^2}{N}" /></a>
  - Sample Variance - Two degrees of freedom: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;s^2=\frac{\sum(X-\bar{X})^2}{n-1}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;s^2=\frac{\sum(X-\bar{X})^2}{n-1}" title="s^2=\frac{\sum(X-\bar{X})^2}{n-1}" /></a>

## [Skewness](https://www.youtube.com/watch?v=_vDRKlTz7yo)
<p align="center">
  <img src="images/skew_types.png" height="100px">
</p>

- Symmetric/no skew: mean = median = mode
- Positively/Right skewed: Mode < Median < Mean (pulled by the extreme values on the right)
- Negatively/Left skewed: Mean < Median < Mode
  - e.g. relatively easy test that most students score a high mark, distribution of age of death in a developed country
- The greater the skew, the greater the distance between mode, median, and mean

### Pearsons' Method
_Calculate skewness_
1. Mode Skewness
  - May not hold in small samples as the mode can be all over the place

<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Skew=\frac{mean-mode}{std&space;dev}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Skew=\frac{mean-mode}{std&space;dev}" title="Skew=\frac{mean-mode}{std dev}" /></a>
</p>

2. Median Skewness
  - More robust in smaller samples

<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Skew=\frac{3(mean-median)}{std&space;dev}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Skew=\frac{3(mean-median)}{std&space;dev}" title="Skew=\frac{3(mean-median)}{std dev}" /></a>
</p>

- In appreciably small data, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;mode=3(median)-2(mean)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;mode=3(median)-2(mean)" title="mode=3(median)-2(mean)" /></a>

### Moment based calculation
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{First&space;moment}:&space;\frac{\sum{x}}{n}&space;\rightarrow&space;mean" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{First&space;moment}:&space;\frac{\sum{x}}{n}&space;\rightarrow&space;mean" title="\text{First moment}: \frac{\sum{x}}{n} \rightarrow mean" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Second&space;(centralised)&space;moment}:&space;\frac{\sum{(x-\mu)^2}}{n}&space;\rightarrow&space;\text{population&space;variance}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Second&space;(centralised)&space;moment}:&space;\frac{\sum{(x-\mu)^2}}{n}&space;\rightarrow&space;\text{population&space;variance}" title="\text{Second (centralised) moment}: \frac{\sum{(x-\mu)^2}}{n} \rightarrow \text{population variance}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Second&space;(centralised)&space;moment}:&space;\frac{\sum{(x-\bar{x})^2}}{n-1}&space;\rightarrow&space;\text{sample&space;variance}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Second&space;(centralised)&space;moment}:&space;\frac{\sum{(x-\bar{x})^2}}{n-1}&space;\rightarrow&space;\text{sample&space;variance}" title="\text{Second (centralised) moment}: \frac{\sum{(x-\bar{x})^2}}{n-1} \rightarrow \text{sample variance}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Third&space;(centralised)&space;moment}:&space;\frac{1}{n}\frac{\sum{(x-\mu)^3}}{\sigma^3}&space;\rightarrow&space;\text{population&space;skew}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Third&space;(centralised)&space;moment}:&space;\frac{1}{n}\frac{\sum{(x-\mu)^3}}{\sigma^3}&space;\rightarrow&space;\text{population&space;skew}" title="\text{Third (centralised) moment}: \frac{1}{n}\frac{\sum{(x-\mu)^3}}{\sigma^3} \rightarrow \text{population skew}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Third&space;(centralised)&space;moment}:&space;\frac{n}{(n-1)(n-2)}\frac{\sum{(x-\bar{x})^3}}{s^3}&space;\rightarrow&space;\text{sample&space;skew}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Third&space;(centralised)&space;moment}:&space;\frac{n}{(n-1)(n-2)}\frac{\sum{(x-\bar{x})^3}}{s^3}&space;\rightarrow&space;\text{sample&space;skew}" title="\text{Third (centralised) moment}: \frac{n}{(n-1)(n-2)}\frac{\sum{(x-\bar{x})^3}}{s^3} \rightarrow \text{sample skew}" /></a>

### Visualization
<p align="center">
  <img src="images/skewness_viz.png" height="300px">
</p>

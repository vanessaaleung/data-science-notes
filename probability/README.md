# Probability
1. [Probability Basics](#probability-basics)
    1. Sample Space
    2. Probability
    3. Mutually Exclusive Events
    4. Using Simulation for Probability Estimation
2. [More Probability Concepts](#more-probability-concepts)
    1. [Conditional Probability](#conditional-probability)
    2. [Bayes Rule](#bayes-rule)
    3. [Independent Events](#independent-events)
    4. [Bernoulli Distribution](#bernoulli-distribution)
    5. [Binomial Distribution](#binomial-distribution)
    6. [Normal Distribution](#normal-distribution)
    7. [Poisson Distribution](#poisson-distribution)
    8. [Exponential Distribution](#exponential-distribution)
    9. [Probability Density Function (PDF)](#probability-density-function-pdf)
    10. [Overdispersion](#overdispersion)
3. [Data Generating Process](#data-generating-process)

## Probability Basics
### Frequentist vs Bayesian
- Frequentist: the rate at which an event will occur if we repeat the experiment
- Bayesian: the degree of belief that something is true

### Sample Space
_S: Set of all possible outcomes_
<p align="center">
  <img src="https://www.mathsisfun.com/data/images/probability-sample-space.svg">
</p>

### Probability
_P(A):  Likelihood of event A within the sample space_
- <img src="https://render.githubusercontent.com/render/math?math=0 \leq P(A) \leq 1">
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(A&space;\cup&space;B)=P(A)&plus;P(B)-P(A&space;\cap&space;B)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(A&space;\cup&space;B)=P(A)&plus;P(B)-P(A&space;\cap&space;B)" title="P(A \cup B)=P(A)+P(B)-P(A \cap B)" /></a>

### Mutually Exclusive Events
_A and B cannot occur at the same time_
- <img src="https://render.githubusercontent.com/render/math?math=P(A \cap B) = 0">
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(A&space;\cup&space;B)=P(A)&plus;P(B)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(A&space;\cup&space;B)=P(A)&plus;P(B)" title="P(A \cup B)=P(A)+P(B)" /></a>

### Using Simulation for Probability Estimation
1. Construct sample space / population
2. Determine how to simulate one outcome
3. Determine rule for success
4. Sample repeatedly and count successes
5. Calculate frequency of sucesses and estimate of probability

## More Probability Concepts
### Conditional Probability
_Probability of A occuring given B has already occured_
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(A&space;|&space;B)=&space;\frac&space;{P(A&space;\cap&space;B)}{P(B)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(A&space;|&space;B)=&space;\frac&space;{P(A&space;\cap&space;B)}{P(B)}" title="P(A | B)= \frac {P(A \cap B)}{P(B)}" /></a>
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(B&space;|&space;A)=&space;\frac&space;{P(B&space;\cap&space;A)}{P(A)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(B&space;|&space;A)=&space;\frac&space;{P(B&space;\cap&space;A)}{P(A)}" title="P(B | A)= \frac {P(B \cap A)}{P(A)}" /></a>

### Bayes Rule
_Probability of an event using prior knowledge about facotrs that might have influenced that event_
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(A&space;|&space;B)=&space;\frac&space;{P(B|A)P(A)}{P(B)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(A&space;|&space;B)=&space;\frac&space;{P(B|A)P(A)}{P(B)}" title="P(A | B)= \frac {P(B|A)P(A)}{P(B)}" /></a>

### Independent Events
_Probability of one occuring is independent of the probability of the other_
- <img src="https://render.githubusercontent.com/render/math?math=P(A \cap B) = P(A)P(B)">
- Conditional Probability <img src="https://render.githubusercontent.com/render/math?math=P(A|B) = P(A)">

### Bernoulli Distribution
_Discrete, models the probability of two outcomes_

<p align="center">
    <img src="https://probabilitycourse.com/images/chapter3/bernoulli(p)%20color.png" height="200px">
</p>

```python
from scipy.stats import bernoulli
data = bernoulli.rvs(p=0.5, size=10)
```

### Binomial Distribution
_Sum of the outcomes of multiple Bernoulli trails_

<p align="center">
    <img src="https://i1.wp.com/www.real-statistics.com/wp-content/uploads/2012/11/binomial-distribution-chart.png?resize=483%2C291" height="200px">
</p>

- Model the number of successful outcomes in trials where there is some consistent probability of success
- k: number of success
- n: number of trials
- p: probability of success

```python
# Given 10 shots and have an 80% chance of making a given shot
# The probability of 8 or less successes is
prob = binom.pmf(k=8, n=10, p=0.8)
```

### Normal Distribution
- bell-curve shaped
- Gaussian distribution
- 68-95-99.7
    - <img src="https://image3.slideserve.com/6601976/the-68-95-99-7-rule-l.jpg"  height="200px">

### Poisson Distribution
_Probability an event occurs in a given unit of time does not change through time_

<p align="center">
    <img src="https://brilliant-staff-media.s3-us-west-2.amazonaws.com/tiffany-wang/673kAjHJ5d.png" height="200px">
</p>

- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;P(y)=\frac{\lambda^y&space;e^{-\lambda}}{y!}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;P(y)=\frac{\lambda^y&space;e^{-\lambda}}{y!}" title="P(y)=\frac{\lambda^y e^{-\lambda}}{y!}" /></a>
- lambda: the average/mean number of arrivals in a given length of time
    - when increase lambda, the distribution spreads and becomes more symmetric
- y: the event
    - Always positive
    - Discrete (not continuous)
    - Lower bound at zero

#### Poisson process
- The timing of the next event is completely independent of when the previous event happened
- The number of  arrivals of a Poisson process in a given amount of time is Poisson distributed
- Examples
    - Natural  births in a given hospital
    - Hit on a website during a given hour

#### Poisson Regression
- <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;y\sim&space;Poisson(\lambda)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;y\sim&space;Poisson(\lambda)" title="y\sim Poisson(\lambda)" /></a>
- Mean of the response: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;E(y)=\lambda" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;E(y)=\lambda" title="E(y)=\lambda" /></a>
- Poisson regression model: <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;log(\lambda)=\beta_0&plus;\beta_1x_1" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;log(\lambda)=\beta_0&plus;\beta_1x_1" title="log(\lambda)=\beta_0+\beta_1x_1" /></a>
- GLM with Poisson in Python: 
```python 
family=sm.families.Poisson())
```
- Assumption: mean should be the same as the variance

### Exponential Distribution
- The waiting time between arrivals of a Poisson process is exponentially distributed

### Probability Density Function (PDF)
_Relative likelihood of observing a value of a continuous variable_

- probability is given by the area under the *PDF, not the value of the PDF

- Example: x is more likely to be less than 10 than to be greater than 10
<img src="pdf.svg" height="300px">

### Overdispersion
- Overdispersion: variance > mean
- Underdispersion: variance < mean, rare
- Compute estimated overdispersion
    - ratio = pearson chi-squared / degree of freedom of rediduals
    - ratio = 1 -> approximately Poisson
    - ratio < 1 -> underdispersion
    - ratio > 1 -> overdispersion

## Data Generating Process (DGP)
1. Define Possible Outcomes for Random Variables
2. Assign Probabilities
3. Define Relationships between Random Variables


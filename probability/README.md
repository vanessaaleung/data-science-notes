# Probability
1. [Probability Basics](#probability-basics)
    1. Sample Space
    2. Probability
    3. Mutually Exclusive Events
    4. Using Simulation for Probability Estimation
2. [More Probability Concepts](#more-probability-concepts)
    1. Conditional Probability
    2. Bayes Rule
    3. Independent Events
3. [Data Generating Process](#data-generating-process)

## Probability Basics
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
_Discrete distribution that models the probability of two outcomes_

<p align="center">
    <img src="https://probabilitycourse.com/images/chapter3/bernoulli(p)%20color.png" height="200px">
</p>

### Binomial Distribution
_Sum of the outcomes of multiple Bernoulli trails_

<p align="center">
    <img src="https://i1.wp.com/www.real-statistics.com/wp-content/uploads/2012/11/binomial-distribution-chart.png?resize=483%2C291" height="200px">
</p>

- Model the number of successful outcomes in trials where there is some consistent probability of success
- k: number of success
- n: number of trials
- p: probability of success

### Normal Distribution
- bell-curve shaped
- 68-95-99.7
    - <img src="https://image3.slideserve.com/6601976/the-68-95-99-7-rule-l.jpg"  height="200px">

### Poisson Distribution
_Count/Number of times something happened_

<p align="center">
    <img src="https://brilliant-staff-media.s3-us-west-2.amazonaws.com/tiffany-wang/673kAjHJ5d.png" height="200px">
</p>

- lambda: average rate

## Data Generating Process (DGP)
1. Define Possible Outcomes for Random Variables
2. Assign Probabilities
3. Define Relationships between Random Variables


# The conditional urn
We have an urn that contains 7 white and 6 black balls. Four balls are drawn at random. We'd like to know the probability that the first and third balls are white, while the second and the fourth balls are black.

Upon completion, you will learn to manipulate simulations to calculate simple conditional probabilities.


```python
# Initialize success, sims and urn
success, sims = 0, 5000
urn = ['w'] * 7 + ['b'] * 6

for _ in range(sims):
    # Draw 4 balls without replacement
    draw = np.random.choice(urn, replace=False, size=4)
    # Count the number of successes
    if (draw == ['w', 'b', 'w', 'b']).all(): 
        success +=1

print("Probability of success = {}".format(success/sims)) 
# Probability of success = 0.0722
```

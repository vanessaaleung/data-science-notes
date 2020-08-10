# Driving Test

Suppose that you are about to take a driving test tomorrow. Based on your own practice and based on data you have gathered, you know that the probability of you passing the test is 90% when it's sunny and only 30% when it's raining. Your local weather station forecasts that there's a 40% chance of rain tomorrow. Based on this information, you want to know what is the probability of you passing the driving test tomorrow.

```python
sims, outcomes, p_rain, p_pass = 1000, [], 0.40, {'sun':0.9, 'rain':0.3}

def test_outcome(p_rain):  
    # Simulate whether it will rain or not
    weather = np.random.choice(['rain', 'sun'], p=[p_rain, 1-p_rain])
    # Simulate and return whether you will pass or fail
    test_result = np.random.choice(['pass', 'fail'], p=[p_pass[weather], 1-p_pass[weather]])
    return test_result
```

```python
for _ in range(sims):
    outcomes.append(test_outcome(p_rain))
    
# Calculate fraction of outcomes where you pass
pass_outcomes_frac = outcomes.count('pass')/len(outcomes)
print("Probability of Passing the driving test = {}".format(pass_outcomes_frac))
```

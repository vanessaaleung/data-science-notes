# National elections
Consider national elections in a country with two political parties - Red and Blue. This country has 50 states and the party that wins the most states wins the elections. You have the probability p of Red winning in each individual state and want to know the probability of Red winning nationally.

Let's model the DGP to understand the distribution. Suppose the election outcome in each state follows a binomial distribution with probability p such that 0 indicates a loss for Red and 1 indicates a win. We then simulate a number of election outcomes. Finally, we can ask rich questions like what is the probability of Red winning less than 45% of the states?

```python
outcomes, sims, probs = [], 1000, p

for _ in range(sims):
    # Simulate elections in the 50 states
    election = np.random.binomial(p=probs, n=1, size=50)
    # Get average of Red wins and add to `outcomes`
    outcomes.append(np.mean(election))

# Calculate probability of Red winning in less than 45% of the states
prob_red_wins = sum(i < 0.45 for i in outcomes)/sims
print("Probability of Red winning in less than 45% of the states = {}".format(prob_red_wins))

# Probability of Red winning in less than 45% of the states = 0.196
```

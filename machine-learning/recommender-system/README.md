# Recommender System
## Collaborative Filtering
- User-based
  - Getting a user rating matrix
  - Learning the similarity weights: e.g. calculate the similarity between users
  - Creating the weighted ratings matrix
- Item-based
- Memory-based: uses the entire dataset to generate recommendation
- Model-based: develops a model to learn users preference

### Challenges
- Data Sparsity: large dataset of user rate only a limited number of items
- Cold Start
- Scalability: performance drops when increase in users or items

## Evaluating of Top-N Recommenders Offline
- Hit Rate: Hits/Users
  - A hit: one of the recommendations in a user's list is something they actually rated
- Average Reciprocal Hit Rate (ARHR): <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{\sum_{i=1}^{n}\frac{1}{rank_i}}{Users}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\frac{\sum_{i=1}^{n}\frac{1}{rank_i}}{Users}" title="\frac{\sum_{i=1}^{n}\frac{1}{rank_i}}{Users}" /></a>
  - Give more credit for succesfully recommending an item in the top slot than a bottom slot
  - Makes sense when users have to scroll to find the bottom items in the list
- Cumulative hit rate (cHR): throws away predicted rating under a threshold, shouldn't get credit for recommending movies that users won't actually enjoy
- Rating Hit Rate (rHR): break down the hit rate by rating
- Recommender systems can be good with poor RMSE scores
- Coverage: % of <user, item> pairs that can be predicted
- Diversity
  - (1-S): S = avg similarity between recommendation pairs
  - How various the items recommended by the system
- Novelty: mean popularity rank of recommended items
- Churn: how often do recommendations change
- Responsiveness: how quickly does new user behavior influence your recommendations
- Perceived quality: let users rate the recommendation

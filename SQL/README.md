# SQL
## Window Functions
- Performs calculation across a set of rows that are somehow related to the current row
- Does not cause rows to become grouped

```sql
SELECT duration_seconds,
     SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
FROM tutorial.dc_bikeshare_q1_2012
```

## Optimization
### Indexing
_Makes columns faster to query by creating pointers to where data is stored within a database_

- stored and searched as **B-trees**, creates a tree-like structure that sorts data for quick searching in logarithmic time
- use an optimal search method known as binary search
- All queries would start at the top node and work their way down the tree. If the target entry is less than the current node, the left path is followed, if greater, the right path is followed

#### Type of Indexing
- Clustered
  - Ensures the **primary key** is stored in **increasing** order
  - Will be **automatically created** when the primary key is defined

- Non-clustered
  - Sorted references for a specific field, from the main table, that hold pointers back to the memory addresses of the table
  - Non-clustered indexes are **not new tables**
  - Slower to query than clustered indexes
  - Can create many non-clustered indexes
  
### Join with INNER JOIN instead of WHERE
- In some databases, WHERE creates a Cartesian Join
- Example
  ```sql
  SELECT Customers.CustomerID, Customers.Name, Sales.LastSaleDate
  FROM Customers, Sales
  WHERE Customers.CustomerID = Sales.CustomerID
  ```
  - If we had 1,000 customers with 1,000 total sales, the query would first generate 1,000,000 results, then filter for the 1,000 records where CustomerID is correctly joined

### Filter Early

### Use EXPLAIN
To get a sens of how long the query will take

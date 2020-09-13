# SQL
- [Window Functions](#window-functions)
- [Optimization](#optimization)
- [Other Functions](#other-functions)

## Window Functions
- Performs calculation across a set of rows that are somehow related to the current row
- Does not cause rows to become grouped
- `PARTITION BY`: narrow the window from the entire dataset to individual groups
```sql
SELECT start_terminal,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_total
  FROM tutorial.dc_bikeshare_q1_2012
```

### RANK() and ROW_NUMBER()
- some rows have indentical value
- `ROW_NUMBER()` gives different numbers
- `RANK()` gives the same rank

### DENSE_RANK()
- `RANK()` would give the identical rows a rank of 2, then skip ranks 3 and 4, so the next result would be 5
- `DENSE_RANK()` would still give all the identical rows a rank of 2, but the following row would be 3 — no ranks would be skipped.

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

## Other Functions
### DATE_TRUNC
_Returns the first day of the date nearest to the date part_
- `DATE_TRUNC(date_part, date)`
- Example: 
       - `DATE_TRUNC('week', '2018-06-12')` returns `'2018-06-11'`
       - `DATE_TRUNC('month', '2018-06-12')` returns `'2018-06-01'`

### EXTRACT
- `EXTRACT (MONTH FROM DATE)`

### COALESCE
_Return the first non-null value in a list_

- Example: `COALESCE(NULL, 'test1', NULL, 'test2')` will return 'test1'

### LAG
_Fetch the data of a preceding row from the present row_
- `LAG(column, number of rows back) OVER (PARTITION BY ... ORDER BY ...)`
- Default number of rows back = 1
- Example: `LAG(mau) OVER (ORDER BY month)`: will return the previous month's mau

### Running Total
- `SUM(mau) OVER (ORDER BY month)`

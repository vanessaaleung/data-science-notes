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
- [Indexing](#indexing)
- [JOINs](#joins)
- [Partitioning](#partitioning)

### Indexing
_Makes columns faster to query by creating pointers to where data is stored within a database_
- Reduce full table scan
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
  
- B-tree: 
       - for equality and range queries, most commonly used
       - High cardinality: a large number of possible values in a column
       - Time to access depends on the depth of the tree
- Hash indexed: 
       - for equality only, no range values
       - look up values in a key, value form
       - mapping arbitrary length data to a fixed-size string
       - No ordering preserving
       - Smaller size than B-tree
- Bitmap: 
       - for inclusion
       - Low cardinality: for columns with few distinct values
       - fast with bitwise operations, e.g. AND, OR, NOT
       - Time to access based on the execution time of the bitwise operation
       - Read-intensive use cases, few writes like data warehouses
       - Create by postgres on the fly when it thinks it's helpful
- Specialized indexes: geo-spatial/user-defined indexing strategies
       - GIST: Generalized Search Tree, framework for implementing custom indexes
       - SP-GIST: Space-partitioned GIST
       - GIN: for text indexign, lookups are faster, builds are slower
       - BRIN: block range indexing, keeps min and max values

### JOINS
#### Sort Merge Joins
- Sort both tables, compare rows like loop join
- Stop when it is not possible to find a match later because of the order
- Use when equality only

#### Join with INNER JOIN instead of WHERE
- In some databases, WHERE creates a Cartesian Join
- Example
  ```sql
  SELECT Customers.CustomerID, Customers.Name, Sales.LastSaleDate
  FROM Customers, Sales
  WHERE Customers.CustomerID = Sales.CustomerID
  ```
  - If we had 1,000 customers with 1,000 total sales, the query would first generate 1,000,000 results, then filter for the 1,000 records where CustomerID is correctly joined
  
### Partitioning
- Break big table into partitions
- Vertical Partitioning
       - Global indexes for each partition
- Horizontal Partitioning
       - Local indexes for each partition
       - Range Partioning: Use a partition key, e.g. based on time
              - query latest data
              - report within range, comparative queries
              - drop data after a period of time
       ```sql
       CREATE TABLE iot_measurement
       ( ... )
       PARTITION BY RANGE(measure_date);
       ```
       ```sql
       CREATE TABLE iot_measurement_wk1_2019
       PARTITION OF iot_measurement
       FOR VALUES FROM ('2019-01-01') TO ('2019-01-08');
       ```
       - Partition by List: data logicalaly groups into subgroups, often query within subgroups
       ```sql
       CREATE TABLE products
       ( ... )
       PARTITION BY LIST(prod_category);
       ```
       ```sql
       CREATE TABLE product_clothing
       PARTITION OF products
       FOR VALUES IN ('casual_clothing', 'business_attire', 'formal_clothing');
       ```
       - Hash Partitioning: data not logically group into subgroups
              - want even distributions of data across partitions
              - no need for subgroup-specifi operations such as drop a partition
              - Modulus: number of partitions

### Filter Early

## Other Functions
### DEALING WITH DATES
#### DATEDIFF
- `DATEDIFF(DATE1, DATE2)`, returns Date1 - Date2

#### DATE_TRUNC
_Returns the first day of the date nearest to the date part_
- `DATE_TRUNC(date_part, date)`
- Example: 
       - `DATE_TRUNC('week', '2018-06-12')` returns `'2018-06-11'`
       - `DATE_TRUNC('month', '2018-06-12')` returns `'2018-06-01'`

#### STR_TO_DATE
- `STR_TO_DATE(str,fmt)`

#### EXTRACT
- `EXTRACT (MONTH FROM DATE)`

#### TO_CHAR
-  `TO_CHAR(DATE, FORMAT DATE STRING)`
- Example: `TO_CHAR('2018-08-13', 'FMDay DD, FMMonth YYYY')` returns `'Friday 13, August 2018'`
- `Dy`: Abbreviated, e.g. Mon, Tues, etc.
- `DD`: Day number 01-31
- `FMDay`: Full day name, Monday, Tuesday, etc

#### INTERVAL
_Calculate date_
- Example: `date - INTERVAL '1 month'`

- Example: Calculating retention rate
```sql
SELECT
  previous.delivr_month,
  ROUND(
    COUNT(DISTINCT current.user_id) :: NUMERIC /
    GREATEST(COUNT(DISTINCT previous.user_id), 1),
  2) AS retention_rate
FROM user_monthly_activity AS previous
LEFT JOIN user_monthly_activity AS current
ON previous.user_id = current.user_id
AND previous.delivr_month = current.delivr_month - INTERVAL '1 month'
```

### COALESCE
_Return the first non-null value in a list_
- Example: `COALESCE(NULL, 'test1', NULL, 'test2')` will return 'test1'

### LAG
_Fetch the data of a preceding row from the present row_
- `LAG(column, number of rows back) OVER (PARTITION BY ... ORDER BY ...)`
- Default number of rows back = 1
- Example: `LAG(mau) OVER (ORDER BY month)`: will return the previous month's mau

### RANK
- Assigns a rank to each row based on that row's position in a sorted order

### Running Total
- `SUM(mau) OVER (ORDER BY month)`

### Greatest
_Used to avoid dividing by zero_
- Example: `GREATEST(value, 1)`

### CASE
```sql
CASE
       WHEN price < 5 THEN '...'
       WHEN price < 10 THEN '...'
       ELSE '...'
END AS price_category
```
              

### CROSSTAB() - POSTGRE SQL
- import like in Python
`CREATE  EXTENSION IF NOT EXISTS tablefunc;`
-  
```SQL
SELECT * FROM CROSSTAB($$
       SELECT QUERY
$$)
AS ct(column 1 INT,
       column 2 INT);
```
       

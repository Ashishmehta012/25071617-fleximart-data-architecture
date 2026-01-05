# NoSQL Analysis

## Limitations of RDBMS
Relational databases struggle with **schema rigidity**. If we want to add "Battery Life" to Electronics but not to Clothing, we need complex NULL columns. RDBMS also struggles with **horizontal scaling** for massive data.

## MongoDB Benefits
MongoDB allows **flexible schemas** (documents). We can store detailed specs for Laptops and simple sizes for Shirts in the same collection without altering the table structure.

## Trade-offs
1. **Data Duplication:** Categories are repeated in every document.
2. **No Joins:** Complex queries requiring data from multiple collections are harder than SQL Joins.
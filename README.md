### **Solution**

1. Solution Design and Reasoning
   In my solution, I implemented all steps of the ETL process completely.

   - Starting with Extraction, I wrote a function that extracts data from a CSV file, and another to extract data from a Database. I called both functions in the ETL file that implements the entire cycle.
   - Then, I implemented a dataframe cleaning function to create a merged, clean dataframe that's fully set up for loading into the database. I used left joins using `pandas` to match each transaction that holds `customer_id` with its respective customer details. The same has been done to match the product name with the product information. This function also drops all rows that are missing any information.
   - Finally, the `load()` function that loads the full dataframe into the destination database called `customer_transactions`. The database was first created using this SQL schema:

   ```SQL
   create table customer_transactions(
   	transaction_id SERIAL primary key,
   	customer_id INT,
   	transaction_date DATE,
   	amount INT,
   	product VARCHAR(100),
   	name VARCHAR(100),
   	email VARCHAR(100),
   	location VARCHAR(100),
   	category VARCHAR(100)
   );
   ```

2. I assumed the correctness of the data since it is recorded automatically from a website. For that purpose, I didn't check for discrepancies in the data. So, if any fields were missing from the data, I just dropped the entire row. While this approach may not be the best, but with further improvement in data cleaning, better strategies will be implemented.

3. Example SQL queries to get information from the `customer_transactions` table:

- Return information about transactions with category `Accessories`:

```sql
  select * from customer_transactions
  where category = 'Accessories';
```

- Return all transactions with category `Electronics` that amount to more than 200.

```sql
  select * from customer_transactions
  where category = 'Electronics' and amount > 200;
```

- Return the sum of amounts from purchases in California:

```sql
  select sum(amount) from customer_transactions
  where location like '%, CA';
```

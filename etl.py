import psycopg2
from extract.extract import extract_csv, extract_db
from transform.transform import clean
from load.load import load

# Connect to the database
db_conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="postgres"
    )
# Creating up the cursor
db_cursor = db_conn.cursor()

# Extract data from products and transactions CSVs
products = extract_csv('data/products.csv')
transactions = extract_csv('data/transactions.csv')

# Extract data from customers Database
customers = extract_db(db_cursor)

# Transform the data to join tables and drop duplicates
transformed = clean(transactions, products, customers)

# Load the ready data to the new Database table
load(transformed, db_conn)

print("Loaded successfully.")
import pandas as pd
import psycopg2


def extract_db(cursor):
    # Extract the customers table
    try: 
        cursor.execute("SELECT * FROM customers")
        db_data = cursor.fetchall()
        db_df = pd.DataFrame(db_data, columns=['customer_id', 'name', 'email', 'join_date', 'location'])
        
        return db_df
    except Exception as exp:
        return(f"An error occurred: {exp}")
    
def extract_csv(path):
    # Extract data from CSV with path
    try:
        df = pd.read_csv(path)
        return df
    except Exception as exp:
        return(f"An error occurred: {exp}")
    
    
if __name__ == "__main__":
    # Test 
    db_conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="postgres"
    )
    db_cursor = db_conn.cursor()
    print(extract_csv("data/products.csv"))
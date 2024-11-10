from sqlalchemy import create_engine

def load(df, db_conn):
    try:
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/postgres')
        df.to_sql('customer_transactions', engine, if_exists='append', index=False)

    except Exception as exp:
        print(f"Error occurred in load batches: {exp}")
        return False

    finally:
        db_conn.commit()
        db_conn.close()
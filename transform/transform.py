import pandas as pd

def clean(transactions, products, customers):
    transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])
    transactions = transactions.dropna()
    
    joint = pd.merge(transactions, customers, 'left', on='customer_id')
    joint = joint[[*list(transactions.columns), 'name', 'email', 'location']].dropna()
    
    full = pd.merge(joint, products, 'left', left_on='product', right_on='product_name')
    full = full[[*joint.columns, 'category']]
    
    return full
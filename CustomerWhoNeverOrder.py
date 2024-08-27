import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    DF = customers[~customers['id'].isin(orders['customerId'])]
    
    return DF[["name"]].rename(columns = {'name': 'customers'})
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    DF = products[(products['recyclable'] == 'Y') &  (products['low_fats'] == 'Y')]
    return DF[["product_id"]]
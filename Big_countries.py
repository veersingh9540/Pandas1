import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    DF = world[(world['population'] >= 25000000 ) | (world['area'] >= 3000000)]
    return  DF[['name', 'population', 'area']]
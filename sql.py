import pandas as pd
from pandas import DataFrame
import gzip
def parse(path):
    g = gzip.open(path,'rb')
    for l in g:
        yield eval(l)
def get_df(path)->DataFrame:
    df = [d for d in parse(path)]
    return DataFrame.from_dict(df)
df = get_df('reviews_Amazon_Instant_Video_5.json.gz')

df.head()
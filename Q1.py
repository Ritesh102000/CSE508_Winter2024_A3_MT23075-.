import pandas as pd
import gzip
import json

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df_review = getDF('Electronics_5.json.gz')
df_metadata = getDF('meta_Electronics.json.gz')

df_review.to_csv('reviews.csv', index=True)
df_metadata.to_csv('metadata.csv', index=True)
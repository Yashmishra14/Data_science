import pandas as pd
df = pd.read_json('house.json', lines=True)
print(df.head(6))

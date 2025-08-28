import pandas as pd


df=pd.read_csv('amazon.csv')

new_df=df.dropna()

new_df.to_csv('amazon.csv_droped_na',index=False)

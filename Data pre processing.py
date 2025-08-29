import pandas as pd


df=pd.read_csv('amazon.csv')

new_df=df.dropna()

new_df.to_csv('amazon.csv_droped_na',index=False)


rate=new_df['rating']


for i in rate:
    if i=="|":
        new_df_fixed=new_df.drop(new_df[new_df['rating']==i].index)
    elif float(i)<0.0 and float(i)>5.0 :
        new_df_fixed=new_df.drop(new_df[new_df['rating']==i].index)
    else:
        print("ok")



new_df_fixed.to_csv('amazon.csv_fixed_ratings',index=False)
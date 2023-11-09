import pandas as pd
import dataframe_image as dfi

df = pd.read_csv('historic_200_values.csv')
df = df[178:200]
df_sorted = df.sort_index(ascending=False)

dfi.export(df_sorted, 'test_images/table_data.png', dpi=300)
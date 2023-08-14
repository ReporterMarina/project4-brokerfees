import os
import glob
import pandas as pd

csv_files = glob.glob("/Users/marin/Dropbox/My Mac (MacBook-Air.local)/Desktop/ApartmentUrls/HotPads_Descs/*.csv")

combined_data = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_data.append(df)

merged_df = pd.concat(combined_data, ignore_index=True)

merged_csv_path = "/Users/marin/Dropbox/My Mac (MacBook-Air.local)/Desktop/ApartmentUrls/HotPads_Descs/merged.csv"
merged_df.to_csv(merged_csv_path, index=False)

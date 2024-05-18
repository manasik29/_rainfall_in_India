import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

os.chdir(r"C:\Users\manas\OneDrive\Documents\Github\_rainfall_in_India\src\dataset")
df = pd.read_excel("rainfall in india 1901-2015.xlsx")

# drop grouped months
# add seasons
df = df.drop(columns=["Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec"])
for index, row in df.iterrows():
    # Check if both FEB and MAR are not null
    if not pd.isnull(row['FEB']) and not pd.isnull(row['MAR']):
        # If both are not null, calculate SPRING as the sum of FEB and MAR
        df.loc[index, 'SPRING'] = row['FEB'] + row['MAR']
    else:
        # If any of FEB or MAR is null, assign NaN to SPRING
        df.loc[index, 'SPRING'] = pd.NA
    if not pd.isnull(row['APR']) and not pd.isnull(row['MAY']):
        df.loc[index, 'SUMMER'] = row['APR'] + row['MAY']
    else:
        df.loc[index, 'SUMMER'] = pd.NA
    if not pd.isnull(row['JUN']) and not pd.isnull(row['JUL']) and not pd.isnull(row['AUG']) and not pd.isnull(row['SEP']):
        df.loc[index, 'MONSOON'] = row['JUN']+row['JUL']+row['AUG']+row['SEP']
    else:
        df.loc[index, 'MONSOON'] = pd.NA
    if not pd.isnull(row['OCT']) and not pd.isnull(row['NOV']):
        df.loc[index, 'AUTUMN'] = row['OCT'] + row['NOV']
    else:
        df.loc[index, 'AUTUMN'] = pd.NA
    if not pd.isnull(row['DEC']) and not pd.isnull(row['JAN']):
        df.loc[index, 'WINTER'] = row['DEC'] + row['JAN']
    else:
        df.loc[index, 'WINTER'] = pd.NA

df.to_excel('processed_data.xlsx', index=False)

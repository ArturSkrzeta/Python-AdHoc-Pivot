# script counts items with status:
# created within the created.csv file
# closed within the closed.csv file
# on hold within the Weekly IT KPI.csv

import pandas as pd

def count_labels(df, status_name):
    unique_items = df['Labels'].unique()

    if len(unique_items) == 3 and ('lht' in unique_items and 'bo' in unique_items and 'os' in unique_items):

        if status_name != 'on hold':
            print('- - - ' + status_name + ' - - -')
            print(df['Labels'].value_counts())
        elif status_name == 'on hold':
            filt = (df['Status'] == 'On hold')
            print('- - - ' + status_name + ' - - -')
            print(df.loc[filt]['Labels'].value_counts())
        else:
            print("some unexpected items im Labels column for status: " + status_name)

file_list = [
    'created.csv',
    'closed.csv',
    'Weekly IT KPI.csv'
]

status_list = [
    'created',
    'closed',
    'on hold'
]

for file in file_list:
    df = pd.read_csv(file)
    if file == 'created.csv':
        count_labels(df,status_list[0])
    elif file == 'closed.csv':
        count_labels(df,status_list[1])
    elif file == 'Weekly IT KPI.csv':
        count_labels(df,status_list[2])

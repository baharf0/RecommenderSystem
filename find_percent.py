
import pandas as pd
import csv


profile_baste = pd.read_csv('profile_baste.csv', sep=',', names=['type_baste', 'meg', 'rial', 'time',
                                                                 'rate_meg', 'rate_Tom'])

new_data = []
for r in range(1, len(profile_baste)):
    new_data.append(int(profile_baste.iloc[r, 2])*4/100)
fields = ['type_baste', 'meg', 'rial', 'time', 'rate_meg', 'rate_Tom', 'percent']
with open('profile_baste.csv', 'r') as f, open('new_profile_baste.csv', 'w') as ff:
    reader = csv.reader(f)
    next(reader)
    writer = csv.writer(ff)
    writer.writerow(fields)
    for row, new_col in zip(reader, new_data):
        row.append(new_col)
        writer.writerow(row)



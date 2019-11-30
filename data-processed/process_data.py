import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

"""
This function will take a path to the csv file in /data-all and process it.
First it will find the max value of the aT column and trim the data to +/- time
at the time where max(at) occurs.
Then, this will create a DataFrame from the new trimmed data with max values of
aT, ax, ay, az and mean values of aT, ax, ay, az.
Finally it will output the DataFrames into csv files.
"""

def process_csv(path):
    data = pd.read_csv(path)
    
    max_aT_row = data.loc[data['aT (m/s^2)'].idxmax()]
    max_aT_time = max_aT_row[0]
    
    data = data[data['time'] > (max_aT_time - 0.9)]
    data = data[data['time'] < (max_aT_time + 0.9)]
    
    max_aT = data['aT (m/s^2)'].max()
    max_ax = data['ax (m/s^2)'].max()
    max_ay = data['ay (m/s^2)'].max()
    max_az = data['az (m/s^2)'].max()
    
    avg_aT = data['aT (m/s^2)'].mean()
    avg_ax = data['ax (m/s^2)'].mean()
    avg_ay = data['ay (m/s^2)'].mean()
    avg_az = data['az (m/s^2)'].mean()
    
    row = [{'max_ax':max_ax, 'max_ay':max_ay, 'max_az':max_az, 'max_aT':max_aT, 'avg_ax':avg_ax, 'avg_ay':avg_ay, 'avg_az':avg_az, 'avg_aT':avg_aT}]
    
    df = pd.DataFrame(row)
    return df

def main():
	member = ['as', 'sd']
	number = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12','13','14','15','16','17','18','19']

	drop_data = process_csv('drop-as-01.csv')
	new_data = process_csv('drop-sd-01.csv')
	drop_data = pd.concat([drop_data, new_data])
	for num in number:
	    for mem in member:
	        string = 'drop-' + mem + '-' + num + '.csv'
	        new_data = process_csv(string)
	        drop_data = pd.concat([drop_data, new_data])
	count_drop_data = len(drop_data)
	drop_data.index = range(count_drop_data)

	fall_data = process_csv('fall-as-01.csv')
	new_data = process_csv('fall-sd-01.csv')
	fall_data = pd.concat([fall_data, new_data])
	for num in number:
	    for mem in member:
	        string = 'fall-' + mem + '-' + num + '.csv'
	        new_data = process_csv(string)
	        fall_data = pd.concat([fall_data, new_data])
	count_fall_data = len(fall_data)
	fall_data.index = range(count_fall_data)

	lie_data = process_csv('lie-as-01.csv')
	new_data = process_csv('lie-sd-01.csv')
	lie_data = pd.concat([lie_data, new_data])
	for num in number:
	    for mem in member:
	        string = 'lie-' + mem + '-' + num + '.csv'
	        new_data = process_csv(string)
	        lie_data = pd.concat([lie_data, new_data])
	count_lie_data = len(lie_data)
	lie_data.index = range(count_lie_data)

	sit_data = process_csv('sit-as-01.csv')
	new_data = process_csv('sit-sd-01.csv')
	sit_data = pd.concat([sit_data, new_data])
	for num in number:
	    for mem in member:
	        string = 'sit-' + mem + '-' + num + '.csv'
	        new_data = process_csv(string)
	        sit_data = pd.concat([sit_data, new_data])
	count_sit_data = len(sit_data)
	sit_data.index = range(count_sit_data)

	drop_data.to_csv('processed_drop_data.csv')
	fall_data.to_csv('processed_fall_data.csv')
	lie_data.to_csv('processed_lie_data.csv')
	sit_data.to_csv('processed_sit_data.csv')

if __name__ == '__main__':
    main()
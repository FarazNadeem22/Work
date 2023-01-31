# Extracting time from pd.datetime
import pandas as pd

timestamp= pd.to_datetime(df['TimeStamp'],unit='s')
df['BookingTime'] = df['Kydtht'].str[0:10] + ' ' + timestamp.apply(lambda x: x.strftime('%H:%M:%S')) 

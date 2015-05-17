import pandas
import numpy as np
import datetime
import time
import calendar
df=pandas.read_csv('aggregation.csv')
df.convert_objects(convert_dates=True)
grouped = df.groupby('Property_Id')
mydate ='01-Jan-2008'
mydate = time.strptime(mydate,'%d-%b-%Y')
print(calendar.timegm(mydate)/(3600*24))
print(df)
print(grouped.agg({'Current_Balance':np.sum,'Close_Date':np.max}))

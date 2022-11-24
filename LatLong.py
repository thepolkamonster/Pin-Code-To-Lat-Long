import pandas as pd
import numpy as np
df=pd.read_csv('Pin_Code.csv')

df['Pin code msub'] = 'in ' + df['Pin code msub'].astype(str)
from geopy.geocoders import Nominatim
def pcode(address):
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(address)
    #print(location.address)
    a=location.latitude
    b=location.longitude
    return (a,b)
    
df['lat']=np.nan
df['long']=np.nan
n=len(df['Pin code msub'])
for i in range (0,n):
    df['lat'][i]=pcode(df['Pin code msub'][i])[0]
    df['long'][i]=pcode(df['Pin code msub'][i])[1]
    
df.to_csv('lat_long.csv')
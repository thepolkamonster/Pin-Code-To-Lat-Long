# The libraries needed
import pandas as pd
import numpy as np

# read the file with the pin codes
df=pd.read_csv('Pin_Code.csv')

# adding 'in' becaise the pin codes were from India and doing this gave accurate results
df['Pin code msub'] = 'in ' + df['Pin code msub'].astype(str)
from geopy.geocoders import Nominatim

#our lat-long finder function
def pcode(address):
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(address)
    
    #print(location.address)
    if location == None:
        a = None
        b = None
    else:
        a=location.latitude
        b=location.longitude
    return (a,b)
    
df['lat']=np.nan
df['long']=np.nan
n=len(df['Pin code msub'])

#Tried doing this with pandas only but that gave NoneType vlaues
for i in range (0,n):
    df['lat'][i]=pcode(df['Pin code msub'][i])[0]
    df['long'][i]=pcode(df['Pin code msub'][i])[1]

#Saving to csv
df.to_csv('lat_long.csv')

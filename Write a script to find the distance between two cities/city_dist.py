from geopy.distance import geodesic
  
  
mumbai = (19.0760, 72.8774)

delhi = (28.7041, 77.1025)
  
  
print(geodesic(mumbai, delhi).km)

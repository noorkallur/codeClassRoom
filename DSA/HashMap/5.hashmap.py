#hash-maps are dict in python
city_map = {}
canada_cities = ["Vancouver", "Winnipeg"]
# city_map["canada"].append(canada_cities) #canada not initiallized
city_map["Canada"] = canada_cities # initialization
city_map["USA"] = "New York" 
city_map["India"] ="Delhi"


#using defaultdict() will help us not to initialize everytime we enter new data

from collections import defaultdict

#default dict will make the entries None
city_map = defaultdict(list)
canada_cities = ["Vancouver", "Winnipeg"]
# city_map["canada"].append(canada_cities) # using defaultdict append can be used  even before initalizing
city_map["canada"] += canada_cities # using defaultdict append can be used  even before initalizing
city_map["USA"] = "New York" # normal way
city_map["India"].append("Delhi")# you can append like this too



print(city_map.keys())
print(city_map.values())
print(city_map.items())

print(city_map["India"])


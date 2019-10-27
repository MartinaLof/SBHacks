import pandas as pd 

csvfile = 'ElephantMovement.csv'
data = pd.read_csv(csvfile)

print(data['location-lat'], data['location-long'])

json_string_start = """ {"type": "Feature", "geometry": { "type": "Point", "coordinates": """
json_string_mid = """ }, "properties": {"name": "value"""
json_string_end = """"} }, """

# icon: {url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}

json_output_data = """ {"type": "FeatureCollection", "features": ["""
for i in range(0, len(data)):
    json_output_data = json_output_data + json_string_start + "[" + str(data['location-long'].iloc[i]) + "," + str(data['location-lat'].iloc[i]) + "]" + json_string_mid + str(i) + json_string_end
print(json_output_data)

file1 = open("road_json.txt", 'w')
file1.write(json_output_data)
file1.close()
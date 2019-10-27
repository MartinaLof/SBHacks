import pandas as pd 

csvfile = 'roadmap.csv'
data = pd.read_csv(csvfile)

print(data['location-lat'], data['location-long'])

json_string_start = """ {"type": "Feature", "geometry": { "type": "LineString", "coordinates": [ """
json_string_end = """] }, "properties": {"name": "value" } } ] }"""

# icon: {url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}

json_header = """ {"type": "FeatureCollection", "features": ["""

json_output_data = ""
for i in range(0, len(data)):
    json_output_data = json_output_data + "[" + str(data['location-long'].iloc[i]) + "," + str(data['location-lat'].iloc[i]) + "], "
print(json_output_data)

end_bind = json_header + json_string_start + json_output_data + json_string_end
print(end_bind)

file1 = open("road_json.txt", 'w')
file1.write(end_bind)
file1.close()
import pandas as pd 

csvfile = 'ElephantMovement.csv'
data = pd.read_csv(csvfile)

print(data['location-lat'], data['location-long'])

json_string_start = """new google.maps.LatLng("""
json_string_end = """), """

# icon: {url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}

json_output_data = ""
for i in range(0, len(data)):
    json_output_data = json_output_data + json_string_start + str(data['location-lat'].iloc[i]) + "," + str(data['location-long'].iloc[i]) + json_string_end
print(json_output_data)

file1 = open("heatmap_json.txt", 'w')
file1.write(json_output_data)
file1.close()
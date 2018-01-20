import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[df["LAT"].mean(),df["LON"].mean()],zoom_start=4,tiles='OpenStreetMap')

def colorCoding():
    if elev in range(0,3000):
        color ="green"
    elif elev in range(3001,9000):
        color= "yellow"
    else:
        color= "red"
    return color


# Capturing Latitude,Longitude ,City Name
for Lat,Longi,Name,elev in zip(df['LAT'],df['LON'],df['NAME'],df["ELEV"]):
    map.simple_marker(location=[Lat,Longi],popup=Name,marker_color=colorCoding())


map.create_map(path='test.html')


les= [2,3,4]
for eachitem in les:
    print(eachitem)

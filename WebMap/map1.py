import folium
import pandas
data = pandas.read_csv("volcano_db.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
Volc = list(data["Volcano Name"])
map = folium.Map
map = folium.Map(location=[16, 80], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for lt, ln,vn in zip(lat, lon,Volc):
    fg.add_child(folium.Marker(
        location=[lt, ln], popup=vn, icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("home.html")

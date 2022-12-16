import folium

map = folium.Map(location=[7.09352, 125.62799], zoom_start=6, tiles='Stamen Terrain') # location coordinates

fg = folium.FeatureGroup(name='My Map')

for coordinates in [[7.085, 125.627], [7.09, 125.50]]:
    fg.add_child(folium.Marker(location=coordinates, popup='Hi! I am a marker.', icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')
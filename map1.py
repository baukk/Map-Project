import pandas
import folium
map=folium.Map(location=[20.593683, 78.962883],width='50%', height='80%',zoom_start=5,left='23%',top='15%')
fg=folium.FeatureGroup(name="feturegroup1")

data=pandas.read_csv("stateCoordinates.csv")
name=list(data["name"])
lat=list(data["lat"])
long=list(data["long"])

html = '''<h4>%s</h4>
<b>Latitude:</b>%s <b>Longitude:</b>%s'''


for i,j,k in zip(name,lat,long):
    iframe = folium.IFrame(html=html %( str(i),str(j),str(k) ), width=200, height=100)
    # iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[j,k],popup=folium.Popup(iframe),icon=folium.Icon(color="blue")))




map.add_child(fg)
map.save("map1.html")
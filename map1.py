import pandas
import folium
map=folium.Map(location=[20.593683, 78.962883],width='50%', height='80%',zoom_start=5,left='23%',top='15%')
fg=folium.FeatureGroup(name="feturegroup1")

data=pandas.read_csv("stateCoordinates.csv")
name=list(data["name"])
lat=list(data["lat"])
long=list(data["long"])
no=list(data["no"])

html = '''<h4>%s</h4>
<b>Latitude:</b>%s <b>Longitude:</b>%s
<b>Value</b> : %s'''

def colorproducer(value):
    if value<33:
         return "green"
    elif value>32 and value<66:
        return "orange"
    else:
        return "red"

htmlfortootlip=''' %s'''

for i,j,k,l in zip(name,lat,long,no):
    iframe = folium.IFrame(html=html %( str(i),str(j),str(k),str(l) ), width=200, height=100)
    tt=htmlfortootlip%i
    fg.add_child(folium.CircleMarker(location=[j,k],radius=4,popup=folium.Popup(iframe),fill=True,fill_color=colorproducer(l),color=colorproducer(l),fill_opacity=0.7, tooltip=tt))




map.add_child(fg)
map.save("index.html")
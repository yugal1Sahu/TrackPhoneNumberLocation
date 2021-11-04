import phonenumbers
import folium
from MyNumber import number
from phonenumbers import geocoder

Key= '59644a070dc54f4fb5571d0b69958d09'

yugalNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(yugalNumber, "en")

print(yourLocation)

#get Service provoder

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)
result = geocoder.geocode(query)

#print(result)
lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']

print(lat,lng)
myMap = folium.Map(Location=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng],popup = yourLocation).add_to((myMap))

# save map in html file

myMap.save("myLocation.html")

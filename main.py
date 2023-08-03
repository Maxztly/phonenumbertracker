import phonenumbers
import opencage
from myphone import number
import folium
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "de")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "de"))

from opencage.geocoder import OpenCageGeocode

key = '' #Enter an Apikey from OpenCage

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Map([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")









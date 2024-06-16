import requests, json, webbrowser

# From https://demile.top
#https://ipstack.com/quickstart

url = "http://api.ipstack.com/"
ip = "google.com" # IP Address or Domain Name
middleV = "?access_key="
apiKey = "" #Insert your API key you get from https://ipstack.com/signup/free
cUrl = url + ip + middleV + apiKey

#Start the request 
session = requests.session()
ipstack = session.get(cUrl).json()

dictx = {
    "ip":ipstack['ip'],
    "type":ipstack['type'],
    "continent_code":ipstack['continent_code'],
    "continent_name":ipstack['continent_name'],
    "country_code":ipstack['country_code'],
    "country_name":ipstack['country_name'],
    "region_code":ipstack['region_code'],
    "region_name":ipstack['region_name'],
    "city":ipstack['city'],
    "zip":ipstack['zip'],
    "latitude":ipstack['latitude'],
    "longitude":ipstack['longitude']   
}

# for loop to print the dictionary data or variable 
for x, y in dictx.items():
    print(x,":", y)
    
gMap = "https://www.google.com/maps/search/?api=1&query=" + str(ipstack['latitude']) + "," + str(ipstack['longitude']) 
 
webbrowser.open(gMap) #open google map on your default webbrowser

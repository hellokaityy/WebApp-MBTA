# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "cNAWLGrfnGeI3GGHnqjEDUnkA8nHYndJ"
MBTA_API_KEY = "6b207645e1c54584a8ed002d1d10dc44"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
from pprint import pprint
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    MAPQUEST_API_KEY = "cNAWLGrfnGeI3GGHnqjEDUnkA8nHYndJ"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data

  
def get_lat_long(place_name): #place name is part of the URL, need to call first function
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    # MAPQUEST_API_KEY = "cNAWLGrfnGeI3GGHnqjEDUnkA8nHYndJ"
    
    # place_name = {'location':place_name}
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    url = url.replace(' ', '%20')
    # print(url)
    data = get_json(url)
    # pprint(data)
    latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']
    longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
    return (latitude, longitude)
    

    

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """

    MBTA_API_KEY = "6b207645e1c54584a8ed002d1d10dc44"

    url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    results = (get_json(url))
    # pprint(results)
    station = results['data'][0]['attributes']['name']
    wheelchair_accessible = int(results['data'][0]['attributes']['wheelchair_boarding'])
    # if wheelchair_accessible > 0:
    #     accessibility = 'wheelchair accessible'
    # else:
    #     accessibility = 'not wheelchair accessible'
    return (station, wheelchair_accessible)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    latitudeLongitude = get_lat_long(place_name)
    print(latitudeLongitude)
    # getStation = get_nearest_station(*latitudeLongitude)
    # print(getStation)
    # if getStation[1] == 1:
    #     print(f'This station {getStation[0]} and is wheelchair accessible')
    # if getStation[1] == 'not wheelchair accessible':
    #     print(f'This station is {getStation[0]} and is not wheelchair accessible')



def main():
    """
    You can test all the functions here
    """
    print(get_lat_long("Northeastern University"))
    print(get_nearest_station('42.3355','-71.1685'))
    print(find_stop_near("Boston College"))
    
if __name__ == '__main__':
    main()
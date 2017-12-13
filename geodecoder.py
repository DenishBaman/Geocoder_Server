#!/usr/bin/env python
import geocoder

def addressToLatLng(address_query):
	location = []
	latlong = []
	results = []
	geo_coding_services = ['google','arcgis','ottawa','yandex']

	service_ct = 0
	geo_coder = getattr(geocoder,geo_coding_services[service_ct])(address_query)

	while len(geo_coder) == 0 and service_ct < len(geo_coding_services):
		service_ct = service_ct +1 
		geo_coder = getattr(geocoder,geo_coding_services[service_ct])(address_query)

	[results for results in geo_coder]

	parsed_result = ""
	parsed_result = parsed_result + "<h3>Geocoding API:  " + geo_coding_services[service_ct] + "\n"
	parsed_result = parsed_result + "\n Location: " + results.address + "\n"
	parsed_result = parsed_result + "\n Latitude: %0.8f " % results.latlng[0] + "\n"
	parsed_result = parsed_result + "Longitude: %0.8f " % results.latlng[1] + "\n<h3>"

	return parsed_result
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
	parsed_result = parsed_result + "geocoding API: " + geo_coding_services[service_ct] + "\n"
	parsed_result = parsed_result + "\n location: " + results.address + "\n"
	parsed_result = parsed_result + "\n latitude: %0.8f " % results.latlng[0] + "\n"
	parsed_result = parsed_result + "longitude: %0.8f " % results.latlng[1] + "\n"

	return parsed_result
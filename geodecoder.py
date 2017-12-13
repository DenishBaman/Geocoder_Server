#!/usr/bin/env python
import geocoder

def addressToLatLng(address_query):
	location = []
	latlong = []
	results = []
	geo_coding_services = ['google','ottawa','yandex','arcgis']

	service_ct = 0
	geo_coder = getattr(geocoder,geo_coding_services[service_ct])(address_query)

	while len(geo_coder) == 0 and service_ct < len(geo_coding_services):
		service_ct = service_ct +1 
		geo_coder = getattr(geocoder,geo_coding_services[service_ct])(address_query)

	[results for results in geo_coder]

	parsed_result = ""
	parsed_result = parsed_result + "geocoding API: \n " + geo_coding_services[service_ct]
	parsed_result = parsed_result + "location: \n" + results.address + "\n"
	parsed_result = parsed_result + "latitude: %0.8f \n" % results.latlng[0] + "\n"
	parsed_result = parsed_result + "longitude: %0.8f \n" % results.latlng[1] + "\n"

	return parsed_result
# Geocoder Server
A basic development of geocoding services using python libraries with HTTP interface and JSON data serialization. 

## Dependency installation

1. Package install
Install geocoder,
```
$ sudo pip install geocoder
```	

2. Python web framework
The flask microframwork is used to build web service.

	* Flask Install
	Let's install flask in virtual environment. If you don't have ``` virtualenv ``` installed in your system you can download it from [virtualenv](https://pypi.python.org/pypi/virtualenv) or 
	```
	$ sudo apt install python-virtualenv
	```

	then install flask,
	```
	$ virtualenv flask
	$ flask/bin/pip install flask 
	```
## Server Launch
Run the executable **geocoder_html_app.py** to launch the server.
```
$ python geocoder_html_app.py
```
After running the script, we can see the ip address on the command line where the server can be launch. Use the ip in any web browser to access the server. 
Provide the address (e.g Surat or SanJose, CA or UTA Nedderman Hall, Arlington, Texas, 76013) and get the latitude and longitude position.



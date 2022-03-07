import requests

# print(response.status_code)
# print(response.content)

def api_ip_geo():
	session = requests.session()
	# TO Request URL with SOCKS over TOR
	session.proxies = {}
	session.proxies['http']='socks5h://localhost:9050'
	session.proxies['https']='socks5h://localhost:9050'
	response = session.get("https://ipgeolocation.abstractapi.com/v1/?api_key=6af93ff174ec49bfb4b6f97ed21508c3")
	jsonResponse=response.json()
	print(jsonResponse)
	ip_address=jsonResponse["ip_address"]
	timezone=jsonResponse["timezone"]["name"]
	print(ip_address,timezone)
	print(""+timezone)
	ip_address
	return ip_address,timezone

api_ip_geo()
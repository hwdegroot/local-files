#!/usr/bin/python3
import requests
import json

API_KEY="iE2s03iY99QCX6CMVdE4MSSVJ7EtsIAOBrF6EXnj"
headers={"Accept": "application/json"}

def get_ip():
    res = requests.get("https://ipinfo.io/ip", headers=headers)
    return res.content.decode("utf-8")

def get_location_by_ip(ip_addr):
    res = requests.get(f"https://api.ipbase.com/v2/info?apikey={API_KEY}&ip={ip_addr}", headers=headers)
    return res.json()

if __name__ == "__main__":
    try:
        raise Exception("Nooooo")
        ip_addr = get_ip()
        location = get_location_by_ip(ip_addr)

        city_id = location["data"]["location"]["city"]["geonames_id"]
        city_name = location["data"]["location"]["city"]["name"]
        print(f"{city_name}|{city_id}")
        #print(json.dumps(location, indent=2))
    except:
        city_id = "2745909"
        city_name = "de Bilt"
        print(f"{city_name}|{city_id}")

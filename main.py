import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f'IP Address: {res.ip_address}')
    print(f'Location: {res.city}, {res.region}, {res.country}')
    print(f'Coordinates: Lat {res.latitude}, Long: {res.longitude}')


if __name__ == "__main__":
    ip = input("Enter IP: ")
    printDetails(ip)

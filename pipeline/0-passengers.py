#!/usr/bin/env python3
"""
Method that returns the list of ships that can hold a given number
of passengers
"""
import requests


def availableShips(passengerCount):
    """
    Returns the list of ships that can hold a given number of passengers
    """
    url = "http://192.168.10.16:8085/api/getAll"
    r = requests.get(url)
    return(r)
    
"""    json = r.json()
    results = json["results"]
    ships = []
    while json["next"]:
        for res in results:
            if res["codigo"] == 'n/a' or res["codigo"] == 'unknown':
                continue
            if int(res["codigo"].replace(',', '')) >= passengerCount:
                ships.append(res["name"])
        url = json["next"]
        r = requests.get(url)
        json = r.json()
        results = json["results"]
    return ships
"""



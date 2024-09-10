#!/usr/bin/env python3

import requests

if __name__ == "__main__":
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    results = requests.get(url).json()

    # Initialize variables to track the earliest launch
    dateCheck = float('inf')
    launchName = None
    rocket_id = None
    launchPad_id = None
    date_local = None

    # Find the earliest upcoming launch
    for launch in results:
        launchDate = launch.get('date_unix')
        if launchDate < dateCheck:
            dateCheck = launchDate
            date_local = launch.get('date_local')  # Use local time
            launchName = launch.get('name')
            rocket_id = launch.get('rocket')
            launchPad_id = launch.get('launchpad')

    # Get rocket name
    if rocket_id:
        rocket_url = f'https://api.spacexdata.com/v4/rockets/{rocket_id}'
        rocket = requests.get(rocket_url).json().get('name')

    # Get launchpad details
    if launchPad_id:
        launchpads_url = f'https://api.spacexdata.com/v4/launchpads/{launchPad_id}'
        launchpad = requests.get(launchpads_url).json()
        launchPad = launchpad.get('name')
        location = launchpad.get('locality')

    # Print the output in the required format
    if launchName and rocket and launchPad and location and date_local:
        print(f"{launchName} ({date_local}) {rocket} - {launchPad} ({location})")

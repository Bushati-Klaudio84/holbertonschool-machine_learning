#!/usr/bin/env python3

import requests
from datetime import datetime

if __name__ == "__main__":
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    results = requests.get(url).json()

    earliest_date = float('inf')
    launchName = None
    rocket_id = None
    launchPad_id = None
    launch_date = None

    # Find the earliest upcoming launch
    for launch in results:
        launchDate = launch.get('date_unix')
        if launchDate and launchDate < earliest_date:
            earliest_date = launchDate
            launch_date = launch.get('date_utc')  # Use UTC time
            launchName = launch.get('name')
            rocket_id = launch.get('rocket')
            launchPad_id = launch.get('launchpad')

    # Get rocket name
    if rocket_id:
        rocket_url = 'https://api.spacexdata.com/v4/rockets/{}'
        rocket = requests.get(rocket_url.format(rocket_id)).json().get('name')

    # Get launchpad details
    if launchPad_id:
        launchpads_url = 'https://api.spacexdata.com/v4/launchpads/{}'
        launchpad = requests.get(launchpads_url.format(launchPad_id)).json()
        launchPad = launchpad.get('name')
        location = launchpad.get('locality')

    # Print the output in the desired format
    if launchName and rocket and launchPad and location and launch_date:
        launch_date_formatted = datetime.strptime(launch_date, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
        print(f"{launchName} ({launch_date_formatted} UTC) {rocket} - {launchPad} ({location})")
    else:
        print("Error: Missing data for upcoming launch.")


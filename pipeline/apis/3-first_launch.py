#!/usr/bin/env python3

"""
Uses the (unofficial) SpaceX API to print the upcoming launch as:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The “upcoming launch” is the one which is the soonest from now, in UTC
and if 2 launches have the same date, it's the first one in the API result.
"""
import requests
from datetime import datetime

def get_first_launch():
    # Fetching upcoming launches from SpaceX API
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()

    # Sort launches by date_unix and take the first one
    launches.sort(key=lambda x: x['date_unix'])
    first_launch = launches[0]

    # Extract required information
    launch_name = first_launch['name']
    date_unix = first_launch['date_unix']
    rocket_id = first_launch['rocket']
    launchpad_id = first_launch['launchpad']

    # Convert Unix time to local time
    date_local = datetime.fromtimestamp(date_unix).isoformat()

    # Fetch rocket name using rocket_id
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_response = requests.get(rocket_url)
    rocket_name = rocket_response.json()['name']

    # Fetch launchpad details using launchpad_id
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    launchpad_response = requests.get(launchpad_url)
    launchpad_data = launchpad_response.json()
    launchpad_name = launchpad_data['name']
    launchpad_locality = launchpad_data['locality']

    # Formatting the output
    print(f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")

if __name__ == '__main__':
    get_first_launch()

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 17:36:03 2014

@author: danielmatthews
"""

import trulia.stats
import trulia.location
from pprint import pprint
TRULIA_KEY = "cgns2cu3gfhh7zgv99jgyjj4"

# Get all neighborhoods names and IDs
hood_requests = trulia.location.LocationInfo(TRULIA_KEY).get_neighborhoods_in_city("Washington", "DC")

# Neighborhood_id in integers
hoods = [int(hood_request['id']) for hood_request in hood_requests]

pprint(hoods)

# Get neighborhood stats
from time import sleep
stats = []
for hood in hoods:
    stat = trulia.stats.TruliaStats(TRULIA_KEY).get_neighborhood_stats(neighborhood_id=[hood], start_date="2014-01-01", end_date="2014-01-31")
    stats.append(stat)
    sleep(1)

#Get avg price per neighborhood
avg_prices = []
for i in range(10):
    try:
        avg_price = int(stats[i]['listingStats']['listingStat'][0]['listingPrice']['subcategory'][0]['averageListingPrice'])
        avg_prices.append(avg_price)
    except:
        avg_prices.append(0)

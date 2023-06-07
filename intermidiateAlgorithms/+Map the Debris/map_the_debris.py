# Intermediate Algorithm Scripting: Map the Debris
#
# Return a new array that transforms the elements' average altitude into their
# orbital periods (in seconds). The array will contain objects in the format
# {name: 'name', avgAlt: avgAlt}. The values should be rounded to the nearest
# whole number. The body being orbited is Earth. The radius of the earth is
# 6367.4447 kilometers, and the GM value of earth is 398600.4418 km3s-2.
#
# Formula : T = 2π √a³/µ
#
# orbitalPeriod(arr) ➞ arr

import math

GM = 398600.4418
ER = 6367.4447


def orbitalPeriod(arr):
    return list(
        map(
            lambda x: {
                "name": x["name"],
                "orbitalPeriod": round(
                    2 * math.pi * math.sqrt((x["avgAlt"] + ER) ** 3 / GM)
                ),
            },
            arr,
        )
    )


print(orbitalPeriod([{"name": "sputnik", "avgAlt": 35873.5553}]))
# ➞ [{'name': 'sputnik', 'orbitalPeriod': 86400}]
print(
    orbitalPeriod(
        [
            {"name": "iss", "avgAlt": 413.6},
            {"name": "hubble", "avgAlt": 556.7},
            {"name": "moon", "avgAlt": 378632.553},
        ]
    )
)
# ➞ [{'name': 'iss', 'orbitalPeriod': 5557}, {'name': 'hubble', 'orbitalPeriod': 5734}, {'name': 'moon', 'orbitalPeriod': 2377399}]

# Notes
#
# The values should be rounded to the nearest whole number. The body being
# orbited is Earth. The radius of the earth is 6367.4447 kilometers, and the
# GM value of earth is 398600.4418 km3s-2.
#
# Resources:
# https://en.wikipedia.org/wiki/Orbital_period
# https://en.wikipedia.org/wiki/Standard_gravitational_parameter

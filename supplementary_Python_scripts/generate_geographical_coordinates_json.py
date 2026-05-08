import json
import requests
from zoneinfo import available_timezones
from time import sleep

# =========================
# CONFIG
# =========================

OUTPUT_FILE = "geographical_coordinates.json"

# =========================
# CACHE
# =========================

cache = {}

# =========================
# GEOLOCATION FUNCTION
# =========================

def geocode(location_name):
    """
    Récupère latitude/longitude depuis OpenStreetMap Nominatim.
    """

    if location_name in cache:
        return cache[location_name]

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": location_name,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "tzdb-geocoder/1.0"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if data:
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])

            cache[location_name] = (latitude, longitude)

            return latitude, longitude

    except Exception as e:
        print(f"Erreur pour {location_name}: {e}")

    cache[location_name] = (None, None)

    return None, None


# =========================
# MAIN JSON STRUCTURE
# =========================

result = {
    "geographical_coordinates": []
}

# =========================
# GET ALL TIMEZONES
# =========================

all_timezones = sorted(available_timezones())

# =========================
# PROCESS TIMEZONES
# =========================

for tz in all_timezones:

    parts = tz.split("/")

    # Ignore les timezones invalides
    if len(parts) < 2:
        continue

    # Dernière partie = localisation
    location = parts[-1]

    print(f"Recherche : {tz} -> {location}")

    latitude, longitude = geocode(location)

    result["geographical_coordinates"].append({
        tz: {
            "location": location.replace("_", " "),
            "latitude": latitude,
            "longitude": longitude
        }
    })

    # Respect API Nominatim
    sleep(1)

# =========================
# SAVE JSON FILE
# =========================

with open(OUTPUT_FILE, "w", encoding="utf-8") as json_file:
    json.dump(
        result,
        json_file,
        ensure_ascii=False,
        indent=4
    )

print(f"\nFichier JSON généré : {OUTPUT_FILE}")
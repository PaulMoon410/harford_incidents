import requests, json, os

def fetch_harford_incidents():
    url = "https://chart.maryland.gov/Incidents/GetIncidents"
    incidents = requests.get(url).json()
    harford = [i for i in incidents if "harford" in i.get("County", "").lower()]
    with open("harford_incidents.json", "w") as f:
        json.dump(harford, f, indent=2)
    print(f"Logged {len(harford)} incidents.")

if __name__ == "__main__":
    fetch_harford_incidents()

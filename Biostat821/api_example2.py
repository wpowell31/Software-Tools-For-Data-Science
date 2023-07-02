"""Example http api."""
import json
import httpx

def get_num_active_alerts():
    response = httpx.get("https://api.weather.gov/alerts/active/count")
    # print(response)
    payload = response.json()
    # print(json.dumps(payload, indent=4))
    return int(payload["total"])

if __name__ == "__main__":
    total = get_num_active_alerts()
    print(f"total: {total}")

"""Example http api."""
import httpx

response = httpx.get("http://www.google.com")
print(response)
print(response.json)

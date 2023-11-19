import json
import requests

# Read data from the file
with open('info_price.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

error_urls = []

for entry in data:
    url = entry["url"]
    response = requests.get(url)
    if response.status_code != 200:
        print(f"URL {url} returned a status code of {response.status_code}. Adding to error_url.txt.")
        error_urls.append(url)

# Write error URLs to a file
with open("error_url.txt", "w") as file:
    for error_url in error_urls:
        file.write(error_url + "\n")

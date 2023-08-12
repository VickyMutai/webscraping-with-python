"""### Scrape via endpoint API"""

import requests
import json

url = "https://giphy.com/api/v4/artists?offset=3&limit=3"

payload = {}
headers = {
  'authority': 'giphy.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9,la;q=0.8,lb;q=0.7',
  'referer': 'https://giphy.com/',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)

for res in response['results']:
  print(res['featured_gif']['images'])
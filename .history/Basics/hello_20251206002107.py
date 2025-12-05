# Package test

import requests

response = requests.get("https://api.github.com")
print(response.status_code)

# 200 is OK, 404 is Not Found

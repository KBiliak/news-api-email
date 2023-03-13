import requests

api_key = '44e09fc42991403aa9f6be9217e827a7'

#Top headlines from TechCrunch right now
url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch' \
      '&apiKey=44e09fc42991403aa9f6be9217e827a7'

request = requests.get(url)
content = request.text
print(content)

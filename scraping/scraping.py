import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import os

subscription_key = "ここにキーを入力"
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
search_term = "ハゼ"

thumbnail_urls = []

for i in range(4):
        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": search_term, "license": "All", "imageType": "photo", "count": "50", "offset":str(i*50)}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        thumbnail_urls.extend([img["thumbnailUrl"] for img in search_results["value"][:]][:])

for i in range(len(thumbnail_urls)):
        image_data = requests.get(thumbnail_urls[i])
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))
        image.save(os.path.join("./image/", (str(i) +".bmp")))
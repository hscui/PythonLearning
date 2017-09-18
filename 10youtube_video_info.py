# coding=utf-8
import turtle

import json
from urllib.request import urlopen

# url = "https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?alt=json"
# 上面的URL已经过期，因此从Github上找了一个Dummy（假的）Json使用，见下面。
url="https://raw.githubusercontent.com/koki0702/introducing-python/00bb512452c03c5fc7ab1d040c5f76105c707bcf/dummy_api/youTube_top_rated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])

---
title: 爬虫爬取压缩过的数据
categories: [Spider]
tags: [爬虫报错处理]
abbrlink: 757817fb
date: 2020-02-06 13:16:57
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-9m55ow.377ilpysa3u0.jpg
---

python 爬取压缩过的数据

<!--less-->

在爬取bilibili的历史记录是，发现出现了*UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte* 错误，后来发现是因为``data = response.read().decode("utf-8")``这一句的data是压缩后的数据，无法正常解析后来对``data``进行解码就可以了

```py
import urllib.request
import urllib.parse
from io import BytesIO
import gzip
import user_agent_list

url = 'https://www.bilibili.com/account/history'

random_user_agent = user_agent_list.getheaders()
request = urllib.request.Request(url)
request.add_header("User-Agent", random_user_agent)
response = urllib.request.urlopen(request)
data = response.read()
buf = BytesIO(data)
zip = gzip.GzipFile(fileobj=buf)
data = zip.read().decode('utf-8')
with open("cookies.html", "w", encoding='utf-8') as f:
    f.write(data)
```


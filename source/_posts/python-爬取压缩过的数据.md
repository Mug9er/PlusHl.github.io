---
title: python 爬取压缩过的数据
mathjax: true
date: 2020-02-06 13:16:57
categories:
  - spider
  - python 报错处理
tags:
  - python
---

![](https://wx4.sinaimg.cn/mw690/0083TyOJly1gbmm3u79pwj31hc0u0qn6.jpg)

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


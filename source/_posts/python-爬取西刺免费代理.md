---
title: python 爬取西刺免费代理
mathjax: true
categories:
  - spider
tags:
  - python
abbrlink: 28d5d8e8
date: 2020-02-06 10:37:03
---

<meta name="referrer" content="no-referrer" />

![](https://wx1.sinaimg.cn/mw690/0083TyOJly1gbmhdj616xj31c00u0diq.jpg)

<!--less-->

使用python爬取网站，可以用handler来隐藏user-agent，和使用高匿的代理ip，下面就是用不同的user-agent来爬取西刺的免费代理ip

首先要有一个user-agent的列表，我把它放在同一目录下然后import导入

```py
import requests
import urllib
import string
import user_agent_list
import re

url = "https://www.xicidaili.com/nn/"
random_user_agent = user_agent_list.getheaders()
request = urllib.request.Request(url)
request.add_header("User-Agent", random_user_agent)
response = urllib.request.urlopen(request)
data = response.read().decode("utf-8")
div = re.findall(r'<table id="ip_list">.*?</table>', data, re.S)[0]
tr = re.findall(r'<tr class="odd">(.*?)</tr>', div, re.S)
tr = tr + re.findall(r'<tr class="">(.*?)</tr>', div, re.S)
HTTP=[]
HTTPS=[]
for td_list in tr:
    td = re.findall(r'<td>(.*?)</td>', td_list)
    if(td[2] == "HTTP"):
        HTTP.append("{\"http\":\"%s:%s\"}," % (td[0], td[1]))
    else:
        HTTPS.append("{\"http\":\"%s:%s\"}," % (td[0], td[1]))

with open("西刺免费代理", "w", encoding="utf-8") as f:
    f.write("HTTP\n")
    for element in HTTP:
        f.write(element+"\n")
    f.write("HTTPS\n")
    for element in HTTPS:
        f.write(element+"\n")


```

项目地址：https://github.com/Mug9er/Python-Spider
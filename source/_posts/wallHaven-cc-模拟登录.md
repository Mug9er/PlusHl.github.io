---
title: wallHaven.cc 模拟登录
mathjax: true
date: 2020-02-11 15:26:29
categories:
  - spider
tags:
  - python
---

<meta name="referrer" content="no-referrer" />

![](https://wx4.sinaimg.cn/mw690/0083TyOJly1gbshrju8gjj30u014049r.jpg)

<!--less-->

在模拟登录wallhaven是，发现了一些问题，用request.session登录并保存cookie并不奏效

所以决定自己手动保存cookie

### 先是登录

因为登录信息中有``_token``，所以要先get一下获取网页的``_token`` ，并且用get到的cookie来请求登录

```py
import requests
from bs4 import BeautifulSoup
from user_agent_list import getheaders

get_token_url = "https://wallhaven.cc/login"
login_url = "https://wallhaven.cc/auth/login"
toplist_url = "https://wallhaven.cc/toplist"
user_agent = getheaders() #user_agent是获取User-Agent 
session = requests.session()
response = requests.get(get_token_url, headers = user_agent)
cookie = ""
for c in response.cookies:
    cookie += c.name + "=" + c.value + ";"
user_agent['Cookie'] = cookie
html = response.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
_token = soup.find_all(type='hidden')[0]['value']
post_data={
    '_token': _token,
    'username': '******',
    'password': '******'
}
response = requests.post(login_url, headers=user_agent, data=post_data)

```

这样可以登录，但是在用这个user-agent去请求数据是，不是登录后的状态，

抓包后发线登录以后的cookie和未登录的cookie只有remeber_web的差别

而remeber_web在请求登录的post的返回值里，那么

```py
# login以后的cookie请求
__cfduid=d7e60a37935c5d9c6f53f05ab1064e1681580787848; 
remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImROQ29VNGRicnZsOW0wQW5BTzZVa1E9PSIsInZhbHVlIjoiTmNQT0h2TE03YW5yaUdhbWZDZnlQYlZzanN3UTV4aUdiMHh1bUl5cjVJMXdQbzIxYnF6bElYcFpmMERPY0ZcL3FnZ21xcU5WdXlvMlBBK21CeEs2K2FWV1pUK05sTmdDdFlHSWl4TlBwUHpuaEprV1dXYmZRbkZzWU1STjV6S3JONWsxNjBsekttbXFqd1BQTzhENlcwNzF0dVRvUit6eURxdHhrN1pZblo4U3lUMys2ekNLdTlXTllBXC82dkI3VUEiLCJtYWMiOiJkYmNiOTZiNDU3M2NjY2M3OGJjZWM4ZTBjZmJlZmIwMTBhMTM5MTcwMTA3ZDc1NjliNDM0ZmM1OWFkY2VhN2YwIn0%3D
_pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1581400207%2C%22http%3A%2F%2Flocalhost%3A63342%2FPyCharnPython%2Fday04%2Fawewall.html%3F_ijt%3Dog5l1ar0obspirlv150bfq3d1o%22%5D
_pk_id.1.01b8=e6d2c9622d153c11.1580787918.21.1581400207.1581400207.
XSRF-TOKEN=eyJpdiI6IjE4NzVZTlQrXC9pWFBmVlFsMUFvVFpBPT0iLCJ2YWx1ZSI6Im91OUROUEFZVHlsNWJ5bjdLa2pyQkV5R0RYZmNMNVN1TkJ5bERSTmFWaGFGRjUyaDI0K09aYzVVTUhZYzhnM0oiLCJtYWMiOiI0MTgzZmMyYzg0YmYyYmE2ZjgxNTEzMDBjYjI1NjFhOGYyMDZhNmJlZjkyYzBlMzhhYTNmNzA0MjBlZDQ3MDZhIn0%3D
wallhaven_session=eyJpdiI6IjZQNVJcL3F0bXJhNndKUkc3QUVCTTZ3PT0iLCJ2YWx1ZSI6IjVSNHlRRjl0cU1sNEFMUGdCUkpFU0lOWXpZUjAzc1d4cHo1NnpLYlk2SU9kXC9zMldpekJKQ1NSMTI2aHIrWDJGIiwibWFjIjoiOWI3YjRlZGU0YTZiZWNkYjZmMWI4MGVlOGFhOThmNzdhOGUwZWQ2ODAxZjFjMGU4MzA1NDJiYjMwZDE3YzQ1OSJ9
```

```py
# 没有login的cookie请求
__cfduid=d7e60a37935c5d9c6f53f05ab1064e1681580787848
_pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1581402095%2C%22http%3A%2F%2Flocalhost%3A63342%2FPyCharnPython%2Fday04%2Fawewall.html%3F_ijt%3Dog5l1ar0obspirlv150bfq3d1o%22%5D
_pk_ses.1.01b8=1
_pk_id.1.01b8=e6d2c9622d153c11.1580787918.22.1581402949.1581402095.
XSRF-TOKEN=eyJpdiI6InRCSDFCT2dvZTZDeXVjR0w0NzZRNGc9PSIsInZhbHVlIjoiY1dzU1J4cHdENzN4eGVuU0I0NmxcL3NCblgyOWdVWEs2dTZ6QTNadHA4OHhISnZHWTFFamNIZGpibmZJQTRPcWUiLCJtYWMiOiJiNmMwMjhmMGYzYmY0MGViMWU2M2VhNTNjMTI1YTY0NThiYjU0MWFiYjYxMzRmODRkMGE5OWE5NmFlNTVkNTBjIn0%3D
wallhaven_session=eyJpdiI6IkJoY1dITVJtQWJ4bzRqamJOVkxKeFE9PSIsInZhbHVlIjoiZjBXZUI3azVRWFAwY2tZeDlHakc1Nm5sSTZFUWVLT2FsT2JFVm5VUXQ0YmszYzVwMk9HcXlaV2R5YXpheG5lMCIsIm1hYyI6IjRjNzk1M2Q4NmE1ZDI4MjAwZDY2NDczNmRlZDVjYmVlN2Y2ZDA0NjYxOTI5NTZkYWM5OWY5MTY5MDQ2YTg4NWUifQ%3D%3D
```

我们就直接组装一个cookie

```py
temp_cookie = user_agent['Cookie']
temp_cookie_list = temp_cookie.split(";")
cookie_dict={}
cookie_dict.update(__cfduid = temp_cookie_list[0].split('=')[1])
cookies_list = cook.split("; ")
for cookie in cookies_list:
    cookie_dict[cookie.split('=')[0]] = cookie.split('=')[1]
print(cookie_dict)
user_agent.pop('Cookie')
response = requests.get(toplist_url, headers=user_agent, cookies = cookie_dict)
data = response.content.decode('utf-8')
with open("awewall.html", 'w') as f:
    f.write(data)
```

这样我们就得到了登陆后访问toplist的页面
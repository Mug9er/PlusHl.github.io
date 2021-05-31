---
title: wallpaper 模拟登录
mathjax: true
categories:
  - spider
tags:
  - python
abbrlink: 72810b67
date: 2020-02-11 15:26:29
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-o3dvv9.4qz014yinx20.jpg
---

在模拟登录wallhaven是，发现了一些问题，用request.session登录并保存cookie并不奏效

所以决定自己手动保存cookie

### 先是登录

因为登录信息中有``_token``，所以要先get一下获取网页的``_token`` ，并且用get到的cookie来请求登录

```py
    def __init__(self):
        self.get_url = "https://wallhaven.cc/login"
        self.post_url = "https://wallhaven.cc/auth/login"
        self.proxies = spider_proxy.SpiderProxy()
        self.data = {}
        self._token = ""
        self.cookies = {}
        self.Is = False

    # 1. 请求页面获得_token 和 cookie
    def get_html(self):
        response = requests.get(self.get_url, headers=self.proxies.header, proxies=self.proxies.proxy)
        response_data = response.content.decode('utf-8')

        self._token = re.findall(r'<meta name="csrf-token" content="(.*?)">', response_data, re.S)

        cookies = ""
        for cookie in response.cookies:
            cookies += cookie.name + "=" + cookie.value + ";"

        # 用header来携带cookie
        self.proxies.header['Cookie'] = cookies

    # 2.装填data
    def combined_data(self):
        self.data = {
            '_token': self._token,
            'username': '643719884@qq.com',
            'password': 'dhl643719884'
        }

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
# 3. 组装cookie
    def combined_cookie(self):
        response = requests.post(self.post_url, headers=self.proxies.header, proxies=self.proxies.proxy, data=self.data)

        # 这里拿到的cookie是相对比较齐全的cookie，主要用这个cookie来组装
        post_cookies = response.request.headers['Cookie']
        post_cookies_list = post_cookies.split("; ")

        # 这里cookie只要__cfduid
        temp_cookie = self.proxies.header['Cookie']
        temp_cookie_list = temp_cookie.split(";")

        # 组装
        self.cookies.update(__cfduid = temp_cookie_list[0].split('=')[1])
        for cookie in post_cookies_list:
            self.cookies[cookie.split('=')[0]] = cookie.split('=')[1]

        # header pop掉Cookie
        self.proxies.header.pop('Cookie')

    # 4.登录
    def post_html(self):
        response = requests.get(self.post_url, headers=self.proxies.header, proxies=self.proxies.proxy, cookies=self.cookies)
        print(response)
        if response.status_code == 200:
            print("Cookies获取成功")
            self.Is = True
        else:
            print("Cookies获取失败")

    def update(self):
        self.__init__()
        self.get_html()
        self.combined_data()
        self.combined_cookie()
        self.post_html()
     
```

这样我们就得到了登陆后访问toplist的页面

完整项目地址: [Mug-9/Python-Spider: Spider (github.com)](https://github.com/Mug-9/Python-Spider)

### session 登录

这里不可行,其他地方可行

```py
import requests
import sys

#登录时需要POST的数据
data = {
	data
	}

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'login_url'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, data)

#登录后才能访问的网页
url = 'url'

#发送访问请求
resp = session.get(url)

print(resp.content.decode('utf-8'))
```


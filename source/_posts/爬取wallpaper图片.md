---
title: 爬取wallpaper图片
mathjax: true
date: 2020-12-07 14:21:42
categories:
	- spider
tags:
	- python	
	- 小项目
---

<meta name="referrer" content="no-referrer" />

![封面](https://wx3.sinaimg.cn/mw690/0083TyOJly1glf9ttrqe4j30qx12w49p.jpg)

<!-- less -->

## 1. user_agent_list

这里是从网上获得的user_agent列表， 稍加修改就可以了

```py
import random


# 返回一个随机的请求头 headers
def getheaders():
    # 各种PC端
    user_agent_list_2 = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    # 各种移动端
    user_agent_list_3 = [
        # IPhone
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPod
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPAD
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # Android
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # QQ浏览器 Android版本
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # Android Opera Mobile
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        # Android Pad Moto Xoom
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        # BlackBerry
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        # WebOS HP Touchpad
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        # Nokia N97
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        # Windows Phone Mango
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        # UC浏览器
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        # UCOpenwave
        "Openwave/ UCWEB7.0.2.37/28/999",
        # UC Opera
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
    ]
    # 一部分 PC端的
    user_agent_list_1 = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent_list = user_agent_list_1 + user_agent_list_2 + user_agent_list_3;
    UserAgent = random.choice(user_agent_list)
    header = {"User-Agent": UserAgent}
    return header
```

## 2.免费代理

这里只是列举了几个免费代理的网站，从上面爬取ip:port 和类型组装成字典输出即可

```py
import requests
import user_agent_list
import re
import random


class SpiderProxy():
    def __init__(self):
        self.url = ["https://www.kuaidaili.com/free/inha/1/", "https://www.7yip.cn/free/?action=china&page=2",
                    "https://www.7yip.cn/free/?action=china&page=3", ]
        self.header = user_agent_list.getheaders()
        self.proxy = {}
        self.proxies_list = []
        self.run()

    def get_proxies_list(self, url):
        try:
            response = requests.get(url, headers=self.header, timeout=3)
            response_data = response.content.decode('utf-8')

            ip_list = re.findall(r'<td data-title="IP">(.*?)</td>', response_data, re.S)
            port_list = re.findall(r'<td data-title="PORT">(.*?)</td>', response_data, re.S)
            type_list = re.findall(r'<td data-title="类型">(.*?)</td>', response_data, re.S)

            for index in range(len(ip_list)):
                self.proxies_list.append("{\'%s\':\'%s:%s\'}" % (type_list[index], ip_list[index], port_list[index]))

        except Exception as e:
            print(e)

        # for tmp_proxy in tmp_list:
        #     proxy = eval(tmp_proxy)
        #     response = requests.get("www.baidu.com", headers=self.header, proxies=proxy)
        #     if response.status_code == 200:
        #         self.proxies_list.append(tmp_proxy)

    def get_proxy(self):
        while 1:
            try:
                self.proxy = eval(random.choice(self.proxies_list))
                response = requests.get("http://www.baidu.com", headers=self.header, proxies=self.proxy, timeout=3)
                if response.status_code == 200:
                    return
            except Exception as e:
                print("getProxy ------> ERROR", e)

    def run(self):
        for url in self.url:
            self.get_proxies_list(url)
```

## 3. loopRequests

自己封装的循环访问的方法，可以解决部分网络延迟问题

在使用代理方面，每50次访问就更换代理，避免被封IP

```py
import requests
import spider_proxy
import time


class LoopRequest():
    def __init__(self):
        self.proxies = spider_proxy.SpiderProxy()
        self.count = 50

    def get(self, url, **args):
        return self.request('GET', url, **args)

    def post(self, url, **args):
        return self.request('POST', url, **args)

    def get_proxy(self):
        if self.count <= 0:
            self.proxies.get_proxy()
            self.count = 50
        self.count -= 1

    def request(self, method, url, **args):
        self.get_proxy()

        args['headers'] = self.proxies.header
        args['proxies'] = self.proxies.proxy
        args['timeout'] = 5
        args['verify'] = False
        loop = 50
        while loop:
            try:
                print("loopRequest: %s 第 %s 次尝试" % (url, 51-loop))
                requests.packages.urllib3.disable_warnings()
                response = requests.request(method, url, **args)
                print("loopRequest: %s 链接成功" % url)
                return response
            except Exception as e:
                print("loopRequest: " + e)
                time.sleep(5)
                if loop == 0:
                    return "get error"
            loop -= 1


request = LoopRequest()
```

## 4.  cookie

由于`wallpaper`登录以后可以看到更多图片，所以这里要模仿登录来拿到`cookie`

`session`在这里并不能起到很好的效果，所以直接使用`cookie`来模拟登录

详细信息挫这里: [wallpaper 模拟登录 | Mug-9's blog (orzff.cn)](http://www.orzff.cn/72810b67/)

```py
import requests
import re
import loopRequest


class SpiderCookies():
    def __init__(self):
        self.get_url = "https://wallhaven.cc/login"
        self.post_url = "https://wallhaven.cc/auth/login"
        self.request = loopRequest.request
        self.data = {}
        self._token = ""
        self.cookies = {}
        self.Is = False
        self.update()

    # 1. 请求页面获得_token 和 cookie
    def get_html(self):
        response = self.request.get(self.get_url)
        response_data = response.content.decode('utf-8')

        self._token = re.findall(r'<meta name="csrf-token" content="(.*?)">', response_data, re.S)

        cookies = ""
        for cookie in response.cookies:
            cookies += cookie.name + "=" + cookie.value + ";"

        # 用header来携带cookie
        self.request.proxies.header['Cookie'] = cookies

    # 2.装填data
    def combined_data(self):
        self.data = {
            '_token': self._token,
            'username': '643719884@qq.com',
            'password': 'dhl643719884'
        }

    # 3. 组装cookie
    def combined_cookie(self):
        response = self.request.post(self.post_url, data=self.data)

        # 这里拿到的cookie是相对比较齐全的cookie，主要用这个cookie来组装
        post_cookies = response.request.headers['Cookie']
        post_cookies_list = post_cookies.split("; ")

        # 这里cookie只要__cfduid
        temp_cookie = self.request.proxies.header['Cookie']
        temp_cookie_list = temp_cookie.split(";")

        # 组装
        self.cookies.update(__cfduid = temp_cookie_list[0].split('=')[1])
        for cookie in post_cookies_list:
            self.cookies[cookie.split('=')[0]] = cookie.split('=')[1]

        # header pop掉Cookie
        self.request.proxies.header.pop('Cookie')

    # 4.登录
    def post_html(self):
        response = self.request.get(self.post_url, cookies=self.cookies)
        response_data = response.content.decode('utf-8')
        if response.status_code == 200:
            print("WallPaper: Cookies获取成功")
            self.Is = True
        else:
            print("WallPaper: Cookies获取失败")

    def update(self):
        self.get_html()
        self.combined_data()
        self.combined_cookie()
        self.post_html()

```

## 5. spider 图片

### 5.1 先获取页面上所有图片二级页面的url

```py
# 1. 获取页面信息,获取每张战片所在页面的url
    def get_html(self, url):
        response = self.request.get(url, cookies=self.cookies.cookies)
        response_data = response.content.decode('utf-8')
        href_list = re.findall(r'<a class="preview" href="(.*?)"  target="_blank"  ></a>', response_data, re.S)
        return href_list

```

### 5.2 对于每张图片页面，获取每张图片的页面

使用`etree+xpath`即可拿到每张图片的url

为防止网络问题，这里进行了5次重复

```py
# 2. 进入页面 获取图片的url
    def get_img_url(self, url):
        loop = 5
        img_url = []
        while loop:
            response = self.request.get(url)
            response_data = response.content.decode('utf-8')
            response_html = etree.HTML(response_data)
            img_url = response_html.xpath('//*[@id="wallpaper"]/@src')
            if len(img_url):
                return img_url
            loop -= 1
        self.error_log.write(url)
        print(url, "ERROR")
        return img_url
```

### 5.3  下载

下载到本地`E:\picture\当天日期`

检查本地log看是否已存在相同图片

```py
# 3. 下载
    def img_download(self, url):
        with self.sem:
            img_name = url.split('/')[-1]
            if self.file_check(img_name):
                print("---%s 已存在" % img_name)
                return

            picture_mkdir = "E:\\picture"
            if not os.path.exists(picture_mkdir):
                os.mkdir(picture_mkdir)
            os.chdir(picture_mkdir)
            data_mkdir = "%s\\%s" % (picture_mkdir, datetime.date.today())
            if not os.path.exists(data_mkdir):
                os.mkdir(data_mkdir)
            os.chdir(data_mkdir)

            response = self.request.get(url)
            response_data = response.content
            print("---%s 开始写入" % img_name)
            threadLock.acquire()
            with open("%s" % img_name, "wb") as f:
                f.write(response_data)
            threadLock.release()
            print("---%s 写入完毕 -- count: %s" % (img_name, self.count))

            threadLock.acquire()
            self.download_log.write(img_name)
            self.count -= 1
            threadLock.release()
```

### 5.4 检查本地log

检查看是否已存在图片

```py
 # 4. 本地log
    def file_check(self, img_name):
        threadLock.acquire()
        self.download_log.seek(0, 0)
        file_content = self.download_log.read()
        threadLock.release()
        if img_name in file_content:
            return True
        else:
            return False
```



### 5.5 run

计划每次下载100张图片，网页页数从2-100

```py
# 6.run
    def run(self):
        loop = 50
        while loop:
            if self.cookies.Is:
                break
            else:
                self.cookies.update()
            time.sleep(2)
            loop -= 1
        if loop <= 0:
            self.error_log.write("Cookies 获得失败")
            return
        for i in range(2, 100):
            url = "%s%s" % (self.url, i)
            href_list = self.get_html(url)
            for html_url in href_list:
                img_url = self.get_img_url(html_url)
                if len(img_url) and self.count > 0:
                    threading.Thread(target=self.img_download, args=(img_url[0],)).start()

```



## 6. github地址

[Mug-9/Python-Spider: Spider (github.com)](https://github.com/Mug-9/Python-Spider/tree/master/爬取WallHaven 图片)
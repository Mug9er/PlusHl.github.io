---
title: 爬虫爬取免费代理
categories: [Python, Spider]
tags: [爬代理]
abbrlink: 28d5d8e8
date: 2020-02-06 10:37:03
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-8oxr11.cbedlri8z9s.png
---

 python 爬取免费代理

<!--less-->

使用python爬取网站，可以用handler来隐藏user-agent，和使用高匿的代理ip，下面就是用不同的user-agent来爬取免费代理

首先要有一个user-agent的列表，我把它放在同一目录下然后import导入

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

            self.proxies_list = []

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
            self.proxy = eval(random.choice(self.proxies_list))
            try:
                response = requests.get("http://www.baidu.com", headers=self.header, proxies=self.proxy, timeout=3)
                if response.status_code == 200:
                    return
            except Exception as e:
                print("getProxy ------> ERROR", e)

    def run(self):
        for url in self.url:
            self.get_proxies_list(url)



```

项目地址：[Python-Spider/爬取代理 at master · Mug-9/Python-Spider (github.com)](https://github.com/Mug-9/Python-Spider/tree/master/爬取代理)
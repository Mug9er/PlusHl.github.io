---
title: vultr+cloudflare
mathjax: true
categories:
  - 配置
  - 服务器
tags:
  - 科学上网
abbrlink: 4e01c297
date: 2021-03-03 23:42:11
---

<meta name = "referrer" content = "no-referrer" />

![封面](https://wx3.sinaimg.cn/mw690/0083TyOJly1go75jv9es8j31hc0u04qq.jpg)

<!-- less-->

## 申请免费域名+ `cloudflare` 托管域名：

[申请免费域名+域名托管](https://iyideng.me/welfare/freenom-free-domain-register.html)

### 注意

`freenom` 申请到的域名设置`DNS`只需要设置`cloudflare`的解析得到的`dns`，不需要设置`80.80.80.80`

`cloudflare` 解析时使用的`ip`是`VPS`服务器的`ip`

## `VPS` 搭建服务器

### 搭建 `Trojan` 服务器

[搭建Trojan服务器](https://iyideng.me/black-technology/cgfw/trojan-server-building-and-using-tutorial.html)

`centos8`以上的不需要升级内核，内核升级可能造成服务器无法启动，

### 搭建 `Vless`服务器（推荐）

[搭建 `Vless`服务器]([Vless+ws+tls梯子搭建一键脚本教程 | 酉荻的博客 (luyiminggonnabeok.cn)](http://luyiminggonnabeok.cn/2020/10/13/Vless-ws-tls一键脚本教程/))

### `BBR`加速

[`bbr`加速](https://www.haah.net/archives/4551.html)


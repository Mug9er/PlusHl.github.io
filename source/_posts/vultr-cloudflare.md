---
title: vultr+cloudflare
categories: [配置]
tags: [飞机]
abbrlink: 4e01c297
date: 2021-03-03 23:42:11
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-l3qqwq.52mr3slkonw0.jpg
---

vultr+cloudflare

<!-- less-->

## 申请免费域名+ `cloudflare` 托管域名：

[申请免费域名+域名托管](https://iyideng.me/welfare/freenom-free-domain-register.html)

### 注意

`freenom` 申请到的域名设置`DNS`只需要设置`cloudflare`的解析得到的`dns`，不需要设置`80.80.80.80`

`cloudflare` 解析时使用的`ip`是`VPS`服务器的`ip`

## V2ray VLESS+TCP+XTLS 一键脚本

[链接](https://v2xtls.org/v2ray%e5%a4%9a%e5%90%88%e4%b8%80%e8%84%9a%e6%9c%ac%ef%bc%8c%e6%94%af%e6%8c%81vmesswebsockettlsnginx%e3%80%81vlesstcpxtls%e3%80%81vlesstcptls%e7%ad%89%e7%bb%84%e5%90%88/)


- 准备一个境外服务器, 如果用VMESS+WS+TLS或者VLESS系列协议，则还需一个域名。对域名没有要求，国内/国外注册的都可以，不需要备案，不会影响使用，也不会带来安全/隐私上的问题。
- 如果vps运营商开启了防火墙（阿里云、Ucloud、腾讯云、AWS、GCP等商家默认有，搬瓦工/hostdare/vultr等商家默认关闭），请先登录vps管理后台放行80和443端口，否则可能会导致获取证书失败。
- ssh连接到服务器。
- 复制（或手动输入）下面命令到终端:
  ```sh
  bash <(curl -sL https://cdn.jsdelivr.net/gh/Misaka-blog/Xray-script@master/xray.sh)
  ```
  按回车键，将出现如下操作菜单。如果菜单没出现，CentOS系统请输入 yum install -y curl，Ubuntu/Debian系统请输入 sudo apt install -y curl，然后再次运行上面的命令：
  ![1](https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/飞机/1.3ft6pfmwatk0.webp)
  目前V2ray一键脚本支持以下功能：

  - VMESS，即最普通的V2ray服务器，没有伪装，也不是VLESS
  - VMESS+KCP，传输协议使用mKCP，VPS线路不好时可能有奇效
  - VMESS+TCP+TLS，带伪装的V2ray，不能过CDN中转
  - VMESS+WS+TLS，即最通用的V2ray伪装方式，能过CDN中转，推荐使用
  - VLESS+KCP，传输协议使用mKCP
  - VLESS+TCP+TLS，通用的VLESS版本，不能过CDN中转，但比VMESS+TCP+TLS方式性能更好
  - VLESS+WS+TLS，基于websocket的V2ray伪装VLESS版本，能过CDN中转，有过CDN情况下推荐使用
  - VLESS+TCP+XTLS，目前最强悍的VLESS+XTLS组合，强力推荐使用（但是支持的客户端少一些）
  - trojan，轻量级的伪装协议
  - trojan+XTLS，trojan加强版，使用XTLS技术提升性能
- 照自己的需求选择一个方式。例如6，然后回车。接着脚本会让你输入一些信息，也可以直接按回车使用默认值。
  ![2](https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/飞机/2.1ik9vxay75mo.webp)
- 脚本接下来会自动运行，一切顺利的话结束后会输出配置信息
  ![3](https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/飞机/3.2kp5p31eagm0.webp)
  到此服务端配置完毕，服务器可能会自动重启（没提示重启则不需要），windows终端出现“disconnected”，mac出现“closed by remote host”说明服务器成功重启了
---
title: 利用hexo多个设备更新博客
mathjax: true
abbrlink: 1351aa80
date: 2020-12-04 22:30:57
categories:
tags:
---

<meta name = "referrer" content = "no-referrer" />

![封面](https://wx3.sinaimg.cn/mw690/0083TyOJly1glc75xmvwqj31cc0u0x53.jpg)

<!--less-->

多台电脑控制一个hexo博客

## 1.下载Git

## 2.下载Node.js

[Node.js](https://nodejs.org/en/)

版本不要太高

## 3.新电脑创建新的ssh密钥

在Git-bash中

`ssh-keygen -t rsa -C 'your_email@example.com'`

在github->`setting`->`SSH && GPG keys`->`new ssh key`

测试是否成功

`ssh -T git@github.com`

如果出现

```
Hi username! You've successfully authenticated, but GitHub does not 
provide shell access.
```

### 3.1 设置用户信息

```js
$ git config --global user.name "用户名"
$ git config --global user.email  "你希望的邮箱名"
```

## 4. 资源配置依赖

### 4.1 更换淘宝镜像

```
npm config set registry https://registry.npm.taobao.org
npm i -g express
```

### 4.2 安装hexo

`npm install -g hexo-cli`

### 4.3 利用`package.json`部署资源

```json
{
  "name": "hexo-site",
  "version": "0.0.0",
  "private": true,
  "hexo": {
    "version": "3.9.0"
  },
  "dependencies": {
    "acorn": "^7.1.1",
    "core-js": "^3.2.1",
    "dependencies": "0.0.1",
    "eslint": "^6.6.0",
    "hexo": "^3.9.0",
    "hexo-abbrlink": "^2.0.5",
    "hexo-asset-image": "0.0.1",
    "hexo-deployer-git": "^1.0.0",
    "hexo-generator-archive": "^0.1.5",
    "hexo-generator-category": "^0.1.3",
    "hexo-generator-feed": "^1.2.2",
    "hexo-generator-index": "^0.2.1",
    "hexo-generator-json-content": "^4.1.6",
    "hexo-generator-searchdb": "^1.0.8",
    "hexo-generator-tag": "^0.2.0",
    "hexo-less": "^0.1.0",
    "hexo-renderer-ejs": "^0.3.1",
    "hexo-renderer-kramed": "^0.1.4",
    "hexo-renderer-less": "^1.0.0",
    "hexo-renderer-mathjax": "^0.6.0",
    "hexo-renderer-stylus": "^0.3.3",
    "hexo-server": "^0.3.3",
    "hexo-symbols-count-time": "^0.6.3",
    "hexo-wordcount": "^6.0.1",
    "peer": "^0.2.10"
  }
}
```

```
npm install
```


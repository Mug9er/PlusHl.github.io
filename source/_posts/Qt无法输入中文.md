---
title: Qt无法输入中文
mathjax: true
categories:
  - Linux
  - QT 输入中文
tags:
  - QT
abbrlink: 20641ee8
date: 2021-04-29 14:13:29
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx2.sinaimg.cn/mw690/0083TyOJly1gq0laqy6alj30u017hb2d.jpg)

<!-- less -->

## 安装`fcitx-frontend-qt5`

```shell
sudo apt-get install fcitx-frontend-qt51
```

查看``fcitx-frontend-qt5 `的安装目录。

```shell
dpkg -L fcitx-frontend-qt5
```

一般是这个

```shell
/usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so
```

## 复制到安装目录

我安装的是`QT6`

```
sudo cp libfcitxplatforminputcontextplugin.so {QT安装目录}/6.0.3/gcc_64/plugins/platforminputcontexts
sudo cp libfcitxplatforminputcontextplugin.so {QT安装目录}Tools/QtCreator/lib/Qt/plugins/platforminputcontexts
```


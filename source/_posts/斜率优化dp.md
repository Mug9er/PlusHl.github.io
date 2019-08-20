---
title: 斜率优化dp
mathjax: true
date: 2019-08-20 16:48:50
categories:
  - ACM
  - 算法学习笔记
tags:
  - dp优化
---

![header](斜率优化dp/header.jpg)

<!-- less -->

具体可以参考这篇博客https://www.cnblogs.com/Judge/p/9551035.html

## 简介

### 斜率

斜率优化$dp$，听名字就知道是用来优化$dp$的

当我们在推导$dp$公式的时候，如果我们推出来的$dp$转移方程类似为：

$dp[i] = \min\limits_{x=1}^{x<i}$  $or$  $\max\limits_{x=1}^{x<i}$ $\{dp[x] + f(x,i)\}$  $f(x,i)是一个关于x与i的函数$

拿去最小值来说

我们考虑两个决策点$k<j<i$并且$j$比$k$要优

我们我们可以列一个不等式 $dp[j]+f(j,i)\leq dp[k]+f(k,i)$

展开如果可以把式子化成类似$\frac{y_j-y_k}{x_j-x_k}\leq k_i$，那么我们如果如果把每个点$(x_i,y_i)$看成一个坐标，那么

就表示$(x_j,y_j)$与$(x_k,y_k)$的斜率$\leq k_i$, 这样我们可以得到真正有用的点组成了一个凸包的形状

### 为什么是个凸包？

当我们去最小值是，我们有一下这么几个点


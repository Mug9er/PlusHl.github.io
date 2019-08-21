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

![img1](斜率优化dp/img1.png)

我们维护一个下凸壳，那么我们找的最小值的直线一定是沿着下凸壳的边缘

![img2](斜率优化dp/img2.png)

所以说不处于凸壳上的点是没有意义的

另外：最小值维护下凸壳，最大值维护上凸壳

## 如何使用

### 求斜率

我们已经把式子化成这么一个形式$\frac{y_j-y_k}{x_j-x_k}\leq k_i$ ,那么我们求斜率可以这么写

以HDU 3507为例：

```c
ll getUp(ll j) {
    return dp[j] + sum[j] * sum[j];
}

ll getDown(ll j) {
    return 2 * sum[j];
}

double Calc(ll x, ll y) {
    if(getDown(x) == getDown(y)) return -1e9; //加一下防止除零的情况
    return 1.0 * (getUp(x) - getUp(y)) / (getDown(x) - getDown(y));
}
```

###　单调队列

当我们化成的这个式子的$\frac{y_j-y_k}{x_j-x_k}\leq k_i$ 的$k_i$是单调的，那么我们可以用单调队列来维护这个凸壳，并且队首是最优解

因为我们维护一个单调的队列，所以当我们在队列里面加点时，根据凸壳的单调性我们可以这么写

```c
while(head < tail && Calc(i, q[tail]) <= Calc(q[tail], q[tail-1])) tail --;
            q[++tail] = i;
```

而如果存在$k<j<i$并且$j$比$k$优，的情况，也就是$\frac{y_j-y_k}{x_j-x_k}\leq k_i$ 

我们在队首把$k$踢出去,因为$k$已经不是最优的

```c
while(head < tail && Calc(q[head+1], q[head]) <= sum[i])
                head ++;
```

这样我们就可以用单调队列去维护一个单调的凸壳，并且单调队列里面的队首就是最优情况

### 单调栈

当我们化成的这个式子的$\frac{y_j-y_k}{x_j-x_k}\leq k_i$ 的$k_i$不是单调的，那么我们可以用单调栈来维护这个凸壳

因为凸壳是单调的，所以我们要找的这个$k_i$可以用二分来查找

## 例题

### HDU 3507 Print Article

#### 题意

有一个$C_i$序列，你可以把序列分为几段，每段的权值为$(\sum\limits_{i=1}^{k}C_i)^2+M$，

求出最小的权值和

####　思路

很容易想到转移方程$dp[i] = \min\limits_{x=1}^{x<i}\{dp[x] + m + (sum[i] - sum[x])^2\}$

我们假设存在一个$k<j<i$并且$j$比$k$要优

那么$dp[j]+m+(sum[i]-sum[j]^2)\leq dp[k]+m+(sum[i]-sum[k])^2$

移项并合并同类项后：

$\frac{dp[j]+sum[j] \times sum[j] - (dp[k]+sum[k]\times sum[k])}{2(sum[j]-sum[k])}\le sum[i]]$



我们设$Y=dp[x]-sum[x],X=2\times sum[x]$

那么式子可以化成:$\frac{Y(j)-Y(k)}{X(j)-X(k)}\le sum[i]$

因为是$sum[i]$是递增的，所以我们可以用单调队列维护一个下凸壳

#### AC代码

```c
#include<bits/stdc++.h>
using namespace std;

#define ll long long
const ll maxn = 5e5 + 7;
const ll inf = 0x3f3f3f3f;
const ll mod = 1e9 + 7;
const double eps = 0.0000000001;
typedef pair<ll, ll> pis;

ll dp[maxn], q[maxn];
ll sum[maxn];

ll head, tail, n, m;

ll getDp(ll i, ll j) {
    return dp[j] + m + (sum[i] - sum[j]) * (sum[i] - sum[j]);
}

ll getUp(ll j) {
    return dp[j] + sum[j] * sum[j];
}

ll getDown(ll j) {
    return 2 * sum[j];
}

double Calc(ll x, ll y) {
    if(getDown(x) == getDown(y)) return -1e9;
    return 1.0 * (getUp(x) - getUp(y)) / (getDown(x) - getDown(y));
}

int main() { 
    while(~scanf("%lld %lld", &n, &m)) {
        for (ll i = 1; i <= n; i ++)
            scanf("%lld", &sum[i]);
        sum[0] = dp[0] = 0;
        for (ll i = 1; i <= n; i ++)
            sum[i] += sum[i-1];
        head = tail = 1;
        for (ll i = 1; i <= n; i ++) {
            while(head < tail && Calc(q[head+1], q[head]) <= 1.0 * sum[i])
                head ++;
            dp[i] = getDp(i, q[head]);
            while(head < tail && Calc(i, q[tail]) <= Calc(q[tail], q[tail-1])) tail --;
            q[++tail] = i;
        }
        printf("%lld\n", dp[n]);
    }
    return 0;
}
```

### 洛谷 P4072 征途

#### 题意

序列分割，给你n个数字，你把序列分割成m个段，每一段的的方差为$v$

输出最小的每一段的之和$\times m^2$

#### 思路

提前声明一下， 下面的$c_i$都是一段路的距离之和，而不是单条路的距离，所以是$m$段而不是$n$段

$s^2=\frac{(\frac{\sum\limits_{i=1}^{m}c_i}{n}-c_1)^2+(\frac{\sum\limits_{i=1}^{m}c_i}{m}-c_2)^2+...+(\frac{\sum\limits_{i=1}^{m}c_i}{m}-c_n)^2}{m}$

$s^2=\frac{(\frac{\sum\limits_{i=1}^{m}c_i}{m})^2-2\times \frac{\sum\limits_{i=1}^{m}c_i}{m}\times c_1+c_1^2+(\frac{\sum\limits_{i=1}^{m}c_i}{m})^2-2\times \frac{\sum\limits_{i=1}^{m}c_i}{m}\times c_2+c_2^2+...+(\frac{\sum\limits_{i=1}^{m}c_i}{m})^2-2\times \frac{\sum\limits_{i=1}^{m}c_i}{m}\times c_n+c_n^2}{m}$

$s^2=\frac{m\times (\frac{\sum\limits_{i=1}^{m}c_i}{m})^2-2\times \frac{(\sum\limits_{i=1}^{m}c_i)^2}{m}+(\sum\limits_{i=1}^{m}c_i^2)}{m}$

$s^2=\frac{\frac{(\sum\limits_{i=1}^{m}c_i)^2}{m}-2\times \frac{(\sum\limits_{i=1}^{m}c_i)^2}{m}+(\sum\limits_{i=1}^{m}c_i^2)}{m}$



$s^2=\frac{-\frac{(\sum\limits_{i=1}^{m}c_i)^2}{m}+(\sum\limits_{i=1}^{m}c_i^2)}{m}$

$s^2\times m^2=-(\sum\limits_{i=1}^{n}c_i)^2+m\times (\sum\limits_{i=1}^{n}c_i^2)$

我们发现前面一项是一个常数，而$s^2\times m^2$最小是在$\sum\limits_{i=1}^{m}c_i^2$最小时

这样我们在进行$dp$转移的时候,我们用$sum[x] = \sum\limits_{i=1}^{x}val[i]$    $val[x]$时每一条路的长度

$dp[i] = \min\{dp[x] + (sum[i]-sum[x])^2\}$

按照以往的套路，存在$k<j<i$并且$j$比$k$要优

$dp[j]+(sum[i]-sum[j])^2\le dp[k]+(sum[i]+sum[k])^2$

$dp[j]+sum[j]^2-(dp[k]+sum[k]^2)\le2\times sum[i]sum[j]-2\times sum[i]sum[k]$

$\frac{dp[j]+sum[j]^2-(dp[k]+sum[k]^2)}{2\times(sum[j]]-sum[k])}\le sum[i]$

这样斜率就推出来了，因为$sum[i]$是个递增的值，所以我们可以用单调队列来维护凸壳

然后用一个滚动数组来记录最优值

#### AC代码

```c
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int maxn = 1e5 + 5;
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;

ll sum[maxn], g[maxn], val[maxn];
ll q[maxn], dp[maxn];

ll getDp(ll i, int j) {
    return g[j] + (val[i] - val[j]) * (val[i] - val[j]);
}

ll getUp(int j) {
    return g[j] + val[j] * val[j];
}

ll getDown(int j) {
    return 2 * val[j];
}

double Calc(int x, int y) {
    if(getDown(x) == getDown(y)) return -1e9;
    return 1.0 * (getUp(x) - getUp(y)) / (getDown(x) - getDown(y));
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i ++) {
        scanf("%lld", &val[i]);
        val[i] += val[i-1];
        g[i] = val[i] * val[i]; 
   }
    for (int t = 1; t < m; t ++) {
        int head, tail;
        head = tail = 1;
        for (int i = 1; i <= n; i ++) {
            while(head < tail && Calc(q[head+1], q[head]) <= val[i])
                head ++;
            dp[i] = getDp(i, q[head]);
            while(head < tail && Calc(i, q[tail]) <= Calc(q[tail], q[tail-1]))
                tail --;
            q[++tail] = i;
        }
        for (int i = 1; i <= n; i ++)  g[i] = dp[i];   
    }
    printf("%lld\n", m * dp[n] - val[n] * val[n]);

    return 0;
}
```

这道题貌似可以用WQS加斜率dp来写，下次来补一下




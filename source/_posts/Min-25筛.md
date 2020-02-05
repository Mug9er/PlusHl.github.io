---
title: Min_25筛
mathjax: true
categories:
  - ACM
  - 算法学习笔记
tags:
  - Min_25筛
abbrlink: ecec6bcc
date: 2019-09-02 20:39:13
---

![wallhaven-73ov8v.png](https://i.loli.net/2020/02/05/nt25FlPAIU6jcsg.png)

<!-- less -->

## 使用条件

在$O(\frac{n^{\frac{3}{4}}}{\log n})$时间复杂度内，来求一类完全积性函数的前缀和 $\sum\limits_{i=1}^{n}f(i)$

要求是$f(p)[p\in prime]$是一个关于p的简单多项式并且$f(p^e)$可以快速算出

## 如何求

### 分类

我们可以先对$i$按照质数非质数分类

$\sum\limits_{i=1}^{n}f(i)=\sum\limits_{1\le p\le n} f(p) + \sum\limits_{i=1 ||i \notin prime}^nf(i)$

因为$f(i)$是完全积性函数，所以我们进一步把后面拆分，枚举每一个合数的最小质因子和最小质因子的次幂

$\sum\limits_{i=1}^{n}f(i)=\sum\limits_{1\le p\le n}f(p)+\sum\limits_{1\le p^e\le n \& 1\le p \le \sqrt n}f(p^e)(\sum\limits_{1\le i \le \lfloor\frac{n}{p^e}\rfloor \& min(i)> p} f(i))$      $min(i)$代表$i$的最小质因子,

上式代表我们把合数的最小质因子以及次幂数提出来,计算那些最小质因子大于$p$的合数的值

### $G$函数

上式中我们要枚举$[1,n]$的每一个质数，但是n的范围可以很大， 这样就没法用线性筛筛出所有质数

但是我们可以考虑一个$DP$，我们令$g(n,j) = \sum\limits_{i=1}^{n}h(i)[i\in prime || min(i)>p_j]$

其中$h(i)$是一个在质数处于$f(i)$取值相同的一个完全积性函数

也可以理解成原$f(i)$的所以值都参照$[i\in prime]$时的取值，把所有自然数都当成质数

$g(n,j)$代表$i$为质数或者$min(i)>p_j$时的$h(i)$的前缀和

然后我们来考虑转移，怎么由$g(n,j-1)$转移到$g(n,j)$ ，因为$j$的增大，那么可满足条件的$h(i)$数量减小，

所以我们通过减掉一些不满足条件的$h(i)$来转移，通过观察可以发现，那些不满足条件的恰好就是最小质因子为

$p_j$的合数,也就是减掉$g(\frac{n}{p_j},j-1)-g(p_j-1,p_j)$，后面是减掉质数的部分，因为减掉的都是小于$p_j$的质数，这些质数已经在前面的遍历中减过了一次，不必再减

那么$g(n,j)=g(n,j-1)-p_j^k(g(\frac{n}{p_j},j-1)-g(p_j-1,j-1))$

注意后面的$g(p_j-1,j-1)$ 其实就是$h(i)$在前$j-1$个质数处的前缀和，因为$p_j\le \sqrt n$，所以我们可以用线性筛

筛出来，但是$n$还是很大，我们无法$DP$到$n$

但是因为$p_j$的范围是$\sqrt n$，而$g(n)$由所有的$g(\frac{n}{p_j})$转移而来，所以我们只要计算这$\sqrt n$ 范围内的$h(i)$即可

我们对下表进行离散化用两个数组来存储

以洛谷P5325为例

$g(x)=x^2,h(x)=x$

```c
void GetW(long long n) {
    for (long long i = 1, j; i <= n; i = j + 1) {
        j = n / (n / i);
        w[++m] = n / i;
        long long t = w[m] % Mod;
        g[m] = t * (t + 1) % Mod * ((2LL * t + 1) % Mod) % Mod * inv_6 % Mod;
        g[m] --;
        h[m] = t * (t + 1) % Mod * inv_2 % Mod;
        h[m] --;
        if(w[m] <= sqr) id1[w[m]] = m;
        else id2[n/w[m]] = m;
    }
}

void GetG(long long n) {
    for (long long i = 1; i <= tot; i ++) {
        for (long long j = 1; j <= m && prim[i] * prim[i] <= w[j]; j ++) {
            long long d = w[j] / prim[i];
            long long id = d <= sqr ? id1[d] : id2[n/d];
            g[j] = Sup(g[j], prim[i] * prim[i] % Mod * ((g[id] - sumg[i-1] + Mod) % Mod) % Mod);
            h[j] = Sup(h[j], prim[i] * ((h[id] - sumh[i-1] + Mod) % Mod) % Mod);
        }
    }
}
```

这样我们就求出来了$[1,n]$中所有$h(i)$在质数处的和，$g(n)$

### 求和

我们设$S(n,j)=\sum\limits_{i=1}^{n}f(i)[min(i) \ge p_j]$

那么$S(n,j)=g(n)-\sum\limits_{i=1}^{j-1}f(p_i)+\sum\limits_{p_k^e\le n\& k> x}f(p_k^e)(S(\frac{n}{p_k^e}, k)+[e!=1])$

这样跟求$g(n)$的$dp$类似,答案就是$S(n,1)+f(1)$



## 例题

### 洛谷P5325

#### 题意

定义$f(x)$, 且$f(p^k)=p^k(p^k-1)$，$p$是一个质数,求$\sum\limits_{i=1}^{n}f(i)$,对$1e9+7$取模

#### 思路

当$p$为质数时 $f(p)=p(p-1)=p^2-p$

设$g(x)=x^2,h(x)=x,f(x)=g(x)-h(x)$

#### AC代码

```c
#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 5;
const int inf = 0x3f3f3f3f;
const int Mod = 1e9 + 7;
const double eps = 1e-8;
typedef pair<int, int> psi;
#define inv_2 (Mod+1)/2
#define inv_6 (Mod+1)/6
long long sqr, m, w[maxn], g[maxn], h[maxn];
long long sumg[maxn], sumh[maxn], id1[maxn], id2[maxn];
long long prim[maxn], tot;
bool mark[maxn];

long long Add(long long a, long long b) {
    return (a + b) % Mod;
}

long long Sup(long long a, long long b) {
    return (a - b + Mod) % Mod;
}

long long Pow(long long a, long long b) {
    long long res = 1;
    while(b) {
        if(b & 1) res = res * a % Mod;
        a = a * a % Mod;
        b >>= 1;
    }
    return res;
}

void init(long long n) {
    mark[1] = 1;
    for (long long i = 2; i <= n; i ++) {
        if(!mark[i]) {
            prim[++tot] = i;
            sumg[tot] = (sumg[tot-1] + i * i) % Mod;
            sumh[tot] = (sumh[tot-1] + i) % Mod;
        }
        for (long long j = 1; j <= tot; j ++) {
            if(i * prim[j] > n) break;
            mark[i * prim[j]] = 1;
            if(i % prim[j] == 0) break;
        }
    }
}

void GetW(long long n) {
    for (long long i = 1, j; i <= n; i = j + 1) {
        j = n / (n / i);
        w[++m] = n / i;
        long long t = w[m] % Mod;
        g[m] = t * (t + 1) % Mod * ((2LL * t + 1) % Mod) % Mod * inv_6 % Mod;
        g[m] --;
        h[m] = t * (t + 1) % Mod * inv_2 % Mod;
        h[m] --;
        if(w[m] <= sqr) id1[w[m]] = m;
        else id2[n/w[m]] = m;
    }
}

void GetG(long long n) {
    for (long long i = 1; i <= tot; i ++) {
        for (long long j = 1; j <= m && prim[i] * prim[i] <= w[j]; j ++) {
            long long d = w[j] / prim[i];
            long long id = d <= sqr ? id1[d] : id2[n/d];
            g[j] = Sup(g[j], prim[i] * prim[i] % Mod * ((g[id] - sumg[i-1] + Mod) % Mod) % Mod);
            h[j] = Sup(h[j], prim[i] * ((h[id] - sumh[i-1] + Mod) % Mod) % Mod);
        }
    }
}

long long S(long long x, long long y, long long n) {
    if(x <= prim[y-1] || x <= 1) return 0;
    long long id = x <= sqr ? id1[x] : id2[n/x];
    long long res = (g[id] - h[id] + Mod - sumg[y-1] + sumh[y-1] + Mod) % Mod;
    for (long long i = y; i <= tot && prim[i] * prim[i] <= x; i ++) {
        long long t = prim[i];
        for (long long j = 1; t <= x; j ++, t = t * prim[i]) {
            long long p1 = t % Mod;
            res = Add(res, p1 * (p1 - 1) % Mod * (S(x/t, i+1, n) + (j != 1)) % Mod);
        }
    }
    return res % Mod;
}

int main(int argc, char *args[]) {
    long long n;
    scanf("%lld", &n);
    sqr = sqrt(n);
    init(sqr);
    GetW(n);
    GetG(n);
    printf("%lld\n", (S(n, 1, n) + 1) % Mod);
    return 0;
}
```






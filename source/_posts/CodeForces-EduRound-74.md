---
title: CodeForces EduRound 74
mathjax: true
categories:
  - ACM
  - Codeforces
tags:
  - 题解
abbrlink: b223976b
date: 2019-10-10 20:12:20
---

![wallhaven-wyvrj6.png](https://wx2.sinaimg.cn/mw690/0083TyOJly1gblvj9ccz7j31hc0u0wg4.jpg)

<!-- less -->

### E: Keyboard Purchase

#### 题意

给你一个有小写字母组成的字符串，让你给每个字母编号，使得$\sum\limits_{i=1}^{n}|S_i-S_{i-1}|$的值最小

#### 思路

  因为字母种类很小，所以我们可以用类似状压来记录中间值，具体的是$dp[(1<<m)]$来记录当前状态出现的字母种类与还未出现的字母种类的距离。

我们现在先想象一个键盘，$dp[i]$的二进制表示就是键盘前几个的键，那么$dp[i]$的转移就是由$dp[i^(1<<j)]$新加了一位j转移得来：

```c
for (int i = 1; i < (1<<m); i ++) {
        dp[i] = 0x3f3f3f3f;
        for (int j = 0; (1<<j) <= i; j ++) 
            if((i>>j)&1) dp[i] = min(dp[i], dp[i^(1<<j)]);
    }
```

得到的就是当前状态下的最小花费，

那么这样的话，原来的$dp[i^(1<<j)]$的状态不确定的这一位已经确定，那么其他还尚未却动的键与当前已经确定的键之间的距离要$+1$，

```c
for (int i = 1; i < (1<<m); i ++) {
        dp[i] = 0x3f3f3f3f;
        for (int j = 0; (1<<j) <= i; j ++) 
            if((i>>j)&1) dp[i] = min(dp[i], dp[i^(1<<j)]);
        for (int j = 0; (1<<j) <= i; j ++) 
            if((i>>j)&1) 
                for (int k = 0; k < m; k ++) 
                    if(!((i>>k)&1)) dp[i] += adj[j][k];
    }
```

#### AC代码

```c
#include<bits/stdc++.h>
using namespace std;

#define ll long long
const int maxn = 1e5 + 7;
const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;
typedef pair<int, int> pis;

int dp[(1<<21)];
int adj[30][30];

int main() { 
    int n, m;
    scanf("%d %d", &n, &m);
    string st;
    cin >> st;
    for (int i = 1; i < st.size(); i ++) {
        adj[st[i]-'a'][st[i-1]-'a'] ++;
        adj[st[i-1]-'a'][st[i]-'a'] ++;
    }
    for (int i = 1; i < (1<<m); i ++) {
        dp[i] = 0x3f3f3f3f;
        for (int j = 0; (1<<j) <= i; j ++) 
            if((i>>j)&1) dp[i] = min(dp[i], dp[i^(1<<j)]);
        for (int j = 0; (1<<j) <= i; j ++) 
            if((i>>j)&1) 
                for (int k = 0; k < m; k ++) 
                    if(!((i>>k)&1)) dp[i] += adj[j][k];
    }
    printf("%d\n", dp[(1<<m)-1]);
    return 0;
}
```


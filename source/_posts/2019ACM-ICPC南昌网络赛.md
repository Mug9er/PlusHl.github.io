---
title: 2019ACM-ICPC南昌网络赛
mathjax: true
categories:
  - ACM
  - ICPC
  - 南昌网络赛
tags:
  - 题解
abbrlink: 4e0518cb
date: 2019-09-10 14:13:02
---

![1.png](https://i.loli.net/2020/02/05/GJWX4eRihSqFUnc.png)

<!--less-->

## H: The Nth Item

### 题意

$F(0)=0,F(1)=1$

$F(n)= 3\times F(n-1)+2\times F(n-2)(n\ge 2)$

求第n项，n个询问，强制在线

### 思路

好像直接1e6进制矩阵快速幂就可以直接过，预先打个1e6的表，但这个好像是卡过，多交几次就会T掉

### AC代码

```c
#include<bits/stdc++.h>
using namespace std;
 
#define ll long long
const int maxn = 1e6;
const int ll mod = 998244353;
 
struct Matrix{
    ll mat[2][2];
 
    Matrix() {memset(mat, 0, sizeof(mat));};
 
    void init() {
        mat[0][0] = mat[1][1] = 1;
    }
 
    void init(ll a, ll b) {
        mat[0][0] = 0; mat[0][1] = b;
        mat[1][0] = 1; mat[1][1] = a;
    }
 
    void operator = (Matrix x) {
        for (int i = 0; i <= 1; i ++)
            for (int j = 0; j <= 1; j ++)
                mat[i][j] = x.mat[i][j];
    }
 
};
 
Matrix operator * (Matrix x, Matrix y) {
    Matrix t;
    for (int i = 0; i <= 1; i ++)
        for (int j = 0; j <= 1; j ++)
            for (int k = 0; k <= 1; k ++)
                t.mat[i][j] = (t.mat[i][j] + x.mat[i][k] * y.mat[k][j]) % mod;
    return t;
}

Matrix pre[4][2*maxn+10];

ll Ksm(ll b) {
    Matrix t; t.init();
    int cnt = 0;
    while(b && cnt < 3) {
        ++ cnt;
        ll pt = b % maxn;
        if(cnt == 3) pt = b;
        t = t * pre[cnt][pt];
        b /= maxn;
    }
    Matrix ans; 
    ans.mat[0][0] = 0; ans.mat[0][1] = 1;
    ans = ans * t;
    return ans.mat[0][0];
}

void init() {
    Matrix t; t.init(3, 2);
    pre[1][1] = t; pre[1][0].init();
    for (int i = 2; i <= maxn; i ++) pre[1][i] = pre[1][i-1] * pre[1][1];
    pre[2][1] = pre[1][maxn]; pre[2][0].init();
    for (int i = 2; i <= maxn; i ++) pre[2][i] = pre[2][i-1] * pre[2][1];
    pre[3][1] = pre[2][maxn]; pre[3][0].init();
    for (int i = 3; i <= 2* maxn; i ++) pre[3][i] = pre[3][i-1] * pre[3][1];
}

int main() {
    init();
    ll n, q;
    scanf("%lld %lld", &n, &q);
    ll ans = 0;
    for (int i = 1; i <= n; i ++) {
        ll a = Ksm(q);
        q = q ^ (a * a);
        ans ^= a;
    }
    printf("%lld\n", ans);
    return 0;
}

```



![1e6](2019ACM-ICPC南昌网络赛/1e6.png)

### 思路

还有一种解法，通过打表得知询问$q$是由循环节的，最后在进行大约$1e6$次后，会有一个长度为$2$的循环节，我们就直接暴力找循环节，时间上好像比上面快一点

### AC代码

```c
#include<bits/stdc++.h>
using namespace std;
 
#define ll long long
const ll mod = 998244353;
 
struct Matrix{
    ll mat[2][2];
 
    Matrix() {memset(mat, 0, sizeof(mat));};
 
    void init() {
        mat[0][0] = mat[1][1] = 1;
    }
 
    void init(ll a, ll b) {
        mat[0][0] = 0; mat[0][1] = b;
        mat[1][0] = 1; mat[1][1] = a;
    }
 
    void operator = (Matrix x) {
        for (int i = 0; i <= 1; i ++)
            for (int j = 0; j <= 1; j ++)
                mat[i][j] = x.mat[i][j];
    }
 
};
 
Matrix operator * (Matrix x, Matrix y) {
    Matrix t;
    for (int i = 0; i <= 1; i ++)
        for (int j = 0; j <= 1; j ++)
            for (int k = 0; k <= 1; k ++)
                t.mat[i][j] = (t.mat[i][j] + x.mat[i][k] * y.mat[k][j]) % mod;
    return t;
}

ll Ksm(ll b) {
    Matrix x; x.init(3, 2);
    Matrix t; t.init();
    while(b) {
        if(b & 1) t = t * x;
        x = x * x;
        b >>= 1;
    }
    Matrix ans;
    ans.mat[0][0] = 0; ans.mat[0][1] = 1;
    ans = ans * t;
    return ans.mat[0][0];
}
map<ll, int> mp;

int main() {
    ll n, q;
    scanf("%lld %lld", &n, &q);
    ll ans = 0, l, r, loop=-1;
    for (int i = 1; i <= n; i ++) {
        if(mp[q]) {
            loop = i-1;
            l = q;
            ll a = Ksm(q);
            r = q ^ (a * a);
            break;
        }
        mp[q] = 1;
        ll a= Ksm(q);
        q = q ^ (a * a);
        ans = ans ^ a;
    }
    if(loop!=-1) {
        ll dis = n - loop;
        if(dis % 4 == 3) ans = ans ^ Ksm(r);
        if(dis % 4 == 2) ans = ans ^ Ksm(l) ^ Ksm(r);
        if(dis % 4 == 1) ans = ans ^ Ksm(l);
    }
    printf("%lld\n", ans);
    return 0;
}

```

![loop](2019ACM-ICPC南昌网络赛/loop.png)


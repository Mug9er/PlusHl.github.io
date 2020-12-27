---
title: axios与django通信
mathjax: true
categories:
  - 小项目
  - django + vue
tags:
  - django
  - vue
abbrlink: '5218864'
date: 2020-12-26 23:37:50
---

<meta name = "referrer" content = "no-referrer" />

![封面](https://wx4.sinaimg.cn/mw690/0083TyOJly1gm1p4h5rt8j31hc0r4n68.jpg)

<!-- less -->

### axios实例

```js
import axios from 'axios'
import qs from 'qs'

export function request (config) {
  const instance = axios.create({ //实例，配置一些基础信息
    baseURL: 'http://192.168.0.100:8888/api/',
    timeout: 5000,
  })

  instance.interceptors.request.use(config => { //请求拦截器
    console.log(config)
    if (config.method == "POST") {
      config.data = qs.stringify(config.data) // post的数据要经过处理
    }
    return config
  }, err => {
    console.log(err)
  })

  instance.interceptors.response.use(res => {//接收拦截器
    return res.data
  }, err => {
    console.log(err)
  })

  return instance(config)
}

```

### 具体get与post

```js
import { request } from './request'

export function getBooks () {
  return request({
    url: 'books'
  })
}

export function postLogin (config) {
  return request({
    method: 'post',
    url: 'books',
    data: config,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded' // 发送数据的类型
    }
  })
}
```

### 表单数据

```vue
<template>
  <div id="app">
    <form>
      <input type="text" placeholder="login" v-model="name" />
      <input type="text" placeholder="pwd" v-model="pwd" />
      <input type="submit" value="登录" @click="submitForm" />
    </form>
    <!-- <button @click="submitForm">submit</button> -->
  </div>
</template>

<script>
import { getBooks } from 'network/home'
import { postLogin } from 'network/home'

export default {
  el: '#app',
  data () {
    return {
      name: "1234",
      pwd: '1234',
    }
  },
  created () {
    getBooks().then(res => {
      console.log(res)
      this.content = res.data
    })
  },
  methods: {
    submitForm (event) {
      console.log(this.name)
      let formData = new FormData()
      formData.append('name', this.name)
      formData.append('pwd', this.pwd)
      postLogin(formData).then(res => {
        console.log(res)
      })
    }
  }
}
</script>

<style>
</style>

```

### django配置

```
MIDDLEWARE = [
     #'django.middleware.csrf.CsrfViewMiddleware', # 注释掉csrf
]
APPEND_SLASH=False
```


---
title: Django + Vue 快速构建项目
mathjax: true
categories: [配置]
tags: [Vue, Django]
abbrlink: b2788495
date: 2020-12-24 20:14:26
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-l3917p.150hewd0j7k0.png
---

Django + Vue 快速构建项目

<!-- less -->

## 使用`Vue+Django`搭建项目

[参考](https://zhuanlan.zhihu.com/p/25080236)

### 构建`Django`项目

*命令：*

```text
django-admin startproject ulb_manager
```

*结构：*

```text
.
├── manage.py
└── ulb_manager
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 进入项目根目录，创建一个 `app` 作为项目后端

*命令：*

```text
cd ulb_manager
python manage.py startapp backend
```

即：`app` 名叫做 `backend`

*结构：*

```text
.
├── backend
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── ulb_manager
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### 将`Vue`打包的`dist`文件放入`url_manager`

```text
.
├─backend
│  ├─migrations
│  └─__pycache__
├─vue-fonter
│  └─dist
│      └─static
│          ├─css
│          ├─fonts
│          ├─img
│          └─js
└─ulb_manager
    └─__pycache__

```

`Vue-CLI3.x`在打包时不会生成`static`文件

使用`vue ui`，导入`Vue`项目，在配置/基础配置/ 修改资源目录 为`static`

这样在进行打包就会生成`static`文件

![](https://wx1.sinaimg.cn/mw690/0083TyOJly1glz7x4dxvmj31bz0ovn01.jpg)

### 使用`Django`的通用视图 `TemplateView`

找到项目根` urls.py(ulb_manager/urls.py)`，使用通用视图创建最简单的模板控制器，访问 `『/』`时直接返回` index.html`



```text
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/', include('backend.urls'))
]
```

###  配置`Django`项目的模板搜索路径

上一步使用了`Django`的模板系统，所以需要配置一下模板使`Django`知道从哪里找到`index.html`

打开 `settings.py (ulb_manager/settings.py)`，找到`TEMPLATES`配置项，修改如下:



```text
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        **'DIRS': ['vue-fonter/dist']**,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

注意这里的`vue-fonter`是`VueJS`项目目录，`dist`则是运行 `npm run build `构建出的`index.html`与静态文件夹` static` 的父级目录

这时启动`Django`项目，访问` / `则可以访问`index.html`，但是还有问题，静态文件都是404错误，下一步我们解决这个问题

### 配置静态文件搜索路径

打开 `settings.py (ulb_manager/settings.py`)，找到` STATICFILES_DIRS` 配置项，配置如下:

```text
# Add for vuejs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "vue-fonter/dist/static"),
]
```

这样`Django`不仅可以将`/` 映射到`index.html`，而且还可以顺利找到静态文件

### `backend` 配置

在`backend`中创建`urls`

```py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', view = views.books, name="books")
]
```

在`backend/views.py`中

```py
from django.shortcuts import render
from django.http.response import  JsonResponse

# Create your views here.

def books(request):
    books = [
        {'id': 1, 'title': "python", "price": 89}
    ]
    return JsonResponse(books, safe=False)

```

此时访问` / `我们可以看到使用`Django`作为后端的`VueJS`前端,访问`/api/books`我们可以看到`json`数据

### 解决开发时的跨域问题

使用`corsheaders`

```js
pip install corsheaders
```

在`setting.py`中加入

```js
INSTALLED_APPS = [
    //...
    'corsheaders',
]
MIDDLEWARE = [
    //......
    'corsheaders.middleware.CorsMiddleware',  # 添加cors，在第三行，位置不能改
    'django.middleware.common.CommonMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
# 允许请求携带cookies
CORS_ALLOW_CREDENTIALS= True 
```

以上是从网上找的解决方法，但是并没有解决问题，

先看一下同源的定义

```
同源是指"协议+域名+端口"三者相同，即便两个不同的域名指向同一个ip地址，也非同源。
```

`vue`启动`server`是的`ip`是`192.168.0.100:8080`，`django`启动服务时的`ip`是`127.0.0.1:8000`，

试着修改了一下`django`的启动`ip`

在`setting.py`中加入

```js
ALLOWED_HOSTS = [
    '192.168.0.100',
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]
```

然后启动

```js
django ./manage.py runserver 192.168.0.100:8888
```

然后启动`vue`

```js
npm run serve
```

这时不在出现跨域问题 

成功！



#### 开发模式

利用`vscode` 写前端`vue`，`pycharm`写`django`后端 ，调试时`pycharm`打开`django`服务，`vscode` 打开`vue`，
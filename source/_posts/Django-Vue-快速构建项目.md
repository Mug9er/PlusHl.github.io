---
title: Django + Vue 快速构建项目
mathjax: true
categories:
  - 配置
  - Django + Vue
tags:
  - 小项目
abbrlink: b2788495
date: 2020-12-24 20:14:26
---

<meta name = "referrer" content = "no-referrer" />

![封面](https://wx4.sinaimg.cn/mw690/0083TyOJly1glz7wduo4kj30u011itlf.jpg)

<!--less-->

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

此时访问` / `我们可以看到使用`Django`作为后端的`VueJS`前端


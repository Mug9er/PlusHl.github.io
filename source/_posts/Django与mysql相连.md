---
title: Django与mysql相连
categories: [配置]
tags: [Django, 连接MySQL]
abbrlink: 3a7fd0d4
date: 2020-12-27 16:55:14
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-rd35yq.w241vzya18w.jpg
---

Django与mysql相连

<!--less-->

## Django与mysql相连

### Django链接数据库

在项目根setting.py中更改默认配置

```js
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '****',
        'HOST': '****',
        'PORT': '3306'
    }
}
```

`ENGINE` 用于特定的数据库引擎的配置，一般选项如下

```js
 django.db.backends.sqlite3
 django.db.backends.postgresql
 django.db.backends.mysql
 django.db.backends.oracle
```

`NAME`:要连接的数据库名称的配置
`USER`:配置连接数据库的用户账号
`PASSWORD`:配置连接数据库的登录密码
`HOST`:配置数据库所在的主机IP地址
 `PORT`:配置连接数据库的端口号
`CHARSET`:配置连接数据库交互数据编码格式

### 创建模型

`Django`项目中定义模型数据，其实就是定义class类型，通过类型创建的对象来封装管理数据，一定要在这里明确关联和对应关系

|     程序     |    数据库    |
| :----------: | :----------: |
| `class`类型  | `table` 表格 |
|  `attr`属性  | `field`字段  |
| `object`对象 | `record`记录 |

模型中的属性与数据库中的字段对应

| 对象中的属性类型定义 |       表中的字段类型        |
| :------------------: | :-------------------------: |
|    `AutoField()`     |  `auto_increment` 自动增长  |
|   `BOoleanField()`   |       `bool` 布尔类型       |
| `NullNooleanField()` | `bool or null` 扩展布尔类型 |
|    `CharField()`     |      `varchar` 字符串       |
|    `TextField()`     |        `text` 长文本        |
|   `IntegerField()`   |         `int` 整数          |
|   `DecimalField()`   |       `double` 双精度       |
|    `FloatField()`    |       `float`  单精度       |
|    `DateField()`     |         `date` 日期         |
|    `TimeField()`     |         `time` 时间         |
|  `DateTimeField()`   |     `datetime` 日期时间     |
|    `FileField()`     |        `blob` 二进制        |
|    `ImageField()`    |        `bolb`二进制         |

每个字段定义时，都有自己的一些特殊选项指定

|     选项      |                           描述                           |
| :-----------: | :------------------------------------------------------: |
|    `null`     |   如果为`True`，将NULL空值存储到数据库中，默认`False`    |
|    `blank`    |    如果为`True`，表示该字段允许存储空值，默认`False`     |
|  `db_column`  | 字段名称，如果不指定，直接使用类型属性的名称作为字段名称 |
|  `db_index`   |       如果设置为`True`，表示个当前字段添加索引支持       |
|   `default`   |                       给字段默认值                       |
| `primary_key` |                  是否设置当前字段为主键                  |
|   `unique`    |         如果为`True`，该字段储存的值必须时唯一的         |

在大部分项目汇总，还会涉及到多表关联

|      选项      |                 描述                 |
| :------------: | :----------------------------------: |
|   ForeignKey   |   一对一关联，该字段定义在多个一方   |
| ManToManyField | 多对多关联关系，该字段两方都需要定义 |
| OneToOneField  | 一对一关联，该字段可以定义在任意一方 |

项目结构

```js
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

在根目录的`setting.py`中添加

```js
INSTALLED_APPS = [
    ///...
    'backend',
]
```

修改`backend/models.py`

```js
from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self): # 表中每条数据显示账号
        return u'account: %s' % self.account


class Class(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
```

`model`中定义两个类，代表两个表`User，Class`，

创建两个表

```js
python manage.py makemigrations
```

同步到`mysql`

```js
python manage.py migrate
```

这时在`mysql`中可以看到新增加的表

```js
mysql> show tables;
+----------------------------+
| Tables_in_test             |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| backend_class              |
| backend_user               |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| user                       |
+----------------------------+
```

### 后台显示数据库

在`backend/admin.py`中注册模型

```py
from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Class)
```

运行`django`

```js
python manage.py runserver 8888 
```

在`http://127.0.0.1:8888/admin/`中可以看到后台登录界面

#### 创建超级用户

```js
python manage.py createsuperuser
```

账号和密码都是`admin`，其他可以随便填

这时可以通过后台登录界面进入后台看到数据库数据

### 修改 语言和时区

在`根目录/setting.py`中修改 语言和时区

```js
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
```

后台界面可以显示中文，通过增加可以添加数据


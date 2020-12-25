---
title: Django+Vue+Nginx+uWSGI部署
mathjax: true
categories:
  - 配置
tags:
  - 服务器
abbrlink: 1ae14b31
date: 2020-12-24 16:02:06
---

<meta name = "referrer" content = "no-referrer" />

![封面](https://wx3.sinaimg.cn/mw690/0083TyOJly1glz0791xozj30u016shdt.jpg)

<!--less-->

## `Django+Vue+Nginx+uWSGI`部署

[参考](https://blog.csdn.net/qq_41785581/article/details/102598073)

### 准备工作

```js
ip:123.56.252.111
vue: dist
django: django_server

├── backend
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── element-test
│   └── dist
│       ├── header.ico
│       ├── index.html
│       └── static
│           ├── css
│           ├── fonts
│           ├── img
│           └── js
├── manage.py
├── media
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── admin
│   ├── css
│   ├── fonts
│   ├── img
│   └── js
├── test.py
├── uwsgi.ini
├── uwsgi.log
├── uwsgi_nginx.sock
└── uwsgi.pid
```

### 虚拟环境

在[服务器配置](http://www.orzff.cn/7dfc688d/)有详细介绍

### `Django`

在[服务器配置](http://www.orzff.cn/7dfc688d/)有详细介绍

### `uWSGI`

#### 安装`uWSGI`

```js
pip install uwsgi
```

#### 简单测试一下

创建`test.py`

```js
# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2
```

运行 `uWSGI`:

```js
uwsgi --http :8000 --wsgi-file test.py
```

选项的含义：

- `http :8000` 使用` http` 协议，8000端口。
- `wsgi-file test.py` 使用` test.py` 作为与 `uWSGI `交互的文件。

访问 `123.56.252.111:8000`，输出“Hello World”，说明该程序是这么工作的：

```mermaid
graph LR;
客户端 --http:8000--> uWSGI
uWSGI --> Python
```



### 测试`Django`

#### 测试`django`

在创建的`django`目录，执行

```js
python manage.py runserver 0.0.0.0:8000
```

先将`IP`设置下`ALLOWHOSTS`中

在[服务器配置](http://www.orzff.cn/7dfc688d/)有详细介绍

在浏览器输入`123.56.255.111:8000`即出现`django`欢迎界面

#### 测试`uWSGI`

```
uwsgi --http :8000 --module mysite.wsgi
```

在浏览器输入`123.56.255.111:8000`出现`Internal Server Error`属于正常现象，因为没有资源

```mermaid
graph LR;
客户端 --http:8000--> uWSGI
uWSGI --> Djano
```

### `Nginx`

安装`nginx`在[服务器配置](http://www.orzff.cn/7dfc688d/)有详细介绍

#### 启动`nginx`

```
#centos 7
systemctl start nginx
```

在浏览器输入`123.56.255.111:80`出现`CenOS`或`Nginx`的欢迎界面

#### 配置`nginx`

开启这三个端口：

- `80端口` 显示`Nginx`欢迎界面，测试`Nginx`是否能正常运行
- `8000端口` `Nginx`接收请求的端口，自行处理静态请求，动态请求则转发给`uWSGI`的8001端口处理
- `8001端口` `uWSGI`接收动态请求的端口，处理完毕后将处理结果发给`Nginx`的8000端口

检查一下是否有`uwsgi_params`文件（后面的配置文件需要用到），它应该在`nginx`的目录里（`/etc/nginx/`），如果没有，可以[点击这里](https://github.com/nginx/nginx/blob/master/conf/uwsgi_params)下载。

创建`/etc/nginx/sites-available`的目录，在目录里创建`support_center_nginx.conf`配置文件进行配置：

```js
 # support_center_nginx.conf
 # the upstream component nginx needs to connect to
 upstream django {
   server 127.0.0.1:8001; # for a web port socket (we'll use this first)
 }

 # configuration of the server
 server {
       # the port your site will be served on
       listen      8000;
       # the domain name it will serve for
       server_name 123.56.252.111; # substitute your machine's IP address or FQDN
       charset     utf-8;

       # max upload size
       client_max_body_size 75M;   # adjust to taste


      # Django media
       location /media  {
         alias /root/mysite/media; # your Django project's media files - amend as required
       }

       location /static {
        alias /root/mysite/static; # your Django project's static files - amend as required
       }

        # Finally, send all non-media requests to the Django server.
       location / {
        uwsgi_pass  django;
        include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed   
      }
```

创建一个软链接(`/etc/nginx/sites-enabled`)指向它：

```js
ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled
```

在`/etc/nginx/nginx.conf`中将该文件夹包含进去，使得`Nginx`启动时，能够将文件夹中配置的项目运行起来：
`include /etc/nginx/sites-enabled/*.conf`

注意，这个语句添加在`http`中，`server`外

```js
 http {
	server {
         listen    8888;
        # listen       [::]:80 default_server;
         server_name  _;
        # root         /usr/share/nginx/html;

         # Load configuration files for the default server block.
         include /etc/nginx/default.d/*.conf;

         location / {
           root /root/mysite/element-test/dist;
           try_files $uri $uri/ @router;
           index index.html index.htm;
         }

         location @router{
           rewrite ^.*$ /index.html last;
         }

         error_page 404 /404.html;
         location = /404.html {
         }

         error_page 500 502 503 504 /50x.html;
         location = /50x.html {
         }
     }
     include /etc/nginx/sites-enabled/*.conf;
}
```

#### 处理静态文件

运行`Nginx`之前，得先把`Django`的静态文件集中到一个文件夹中（该文件夹就是`STATIC_ROOT`的值）：
先向`settings.py`中添加：

```python
STATIC_ROOT = '/root/mysite/static'
```

然后，将静态资源集中：

```bash
python manage.py collectstatic
```

#### `nginx`测试

```js
systemctl restart nginx
```

向`media`文件夹中放一张图`media.jpg`用于测试，

`media`的位置在上面`support_center_nginx.conf`中的`location /media`的指定位置

在浏览器输入`123.56.255.111:8000/media/picture.png`出现一张图片

```mermaid
graph LR;
客户端 --http--> Nginx
Nginx --uwsgi--> uWSGI
uWSGI --> Python
```

#### 使用`.ini`对`uWSGI`进行设置

创建`uwsgi.ini`

```js
[uwsgi]
#  项目路径 
chdir = /root/mysite

#django的wsgi文件路径
wsgi-file = /root/mysite/wsgi.py

# 使用mmcsite.wsgi模块
module = mysite.wsgi

# 虚拟环境的路径
home = /root/Envs/Django

# 启用master
master = true

# 启动五个进程
processes = 10

# 每个进程启动30个线程
threads = 30

# 指定socket监听的地址和端口
socket = 0.0.0.0:8001

# socket权限
chmod-socket = 666

# 结束后清理环境
vacuum = true

# 日志文件
daemonize = /root/mysite/uwsgi.log

# pid文件
pidfile = /root/mysite/uwsgi.pid

# 允许用内嵌的语言启动线程，这将允许你在app程序中产生一个子线程
enable-threads = true     
```

然后，启动 `uWSGI`

```bash
uwsgi --ini uwsgi.ini
```
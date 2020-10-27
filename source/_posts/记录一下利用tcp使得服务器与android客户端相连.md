---
title: 记录一下利用tcp使得服务器与android客户端相连
mathjax: true
categories:
  - 小项目
tags:
  - 服务器
  - android
abbrlink: b4b2d023
date: 2020-10-21 22:11:20
---

<meta name = "referrer" content = "no-referrer" />
![封面](https://wx4.sinaimg.cn/mw690/0083TyOJly1gjxbd3rshij31c00u0qv5.jpg)

<!-- less -->

# 云服务器

租一个简单的服务器，

![服务器](https://wx4.sinaimg.cn/mw690/0083TyOJly1gjxbgzkd7zj30k004baa5.jpg)

## 防火墙

首先将我们需要的端口打开

```
firewall-cmd --zone=public --add-port=6666/tcp --permanent   # 开放6666端口
firewall-cmd --reload   # 配置立即生效
```

用`firewall-cmd --zone=public --list-ports` 查看一下是否开启

![](https://wx1.sinaimg.cn/mw690/0083TyOJly1gjxbmaskt3j30u00vdk4g.jpg)

有时阿里云服务器的端口也得打开，这个自行百度即可。

## seriver.c

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <ctype.h>
#include <stdlib.h>

#define SERV_PORT 6666

char rbuf[1024];

int main() {
        int sockfd,clientfd, size, ret, on = 1;
        struct sockaddr_in saddr, raddr;

//      设置地址信息，ip信息
        size = sizeof(struct sockaddr_in);
        bzero(&saddr, size);
        saddr.sin_family = AF_INET;
        saddr.sin_port = htons(SERV_PORT);
        saddr.sin_addr.s_addr = htonl(INADDR_ANY);

// 创建UDP套接字
        sockfd = socket(AF_INET, SOCK_STREAM, 0);
        if(sockfd < 0) {
                perror("Socket failed.");
                exit(1);
        }

//设置端口复用
        setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on));

// 绑定地址信息，IP信息
        ret = bind(sockfd, (struct sockaddr*)&saddr, sizeof(struct sockaddr));
        if(ret < 0) {
                perror("sbind failed.");
                exit(2);
        }

        listen(sockfd, 128);

        socklen_t val = sizeof(struct sockaddr);
        puts("waiting connect...");
        clientfd = accept(sockfd, (struct sockaddr*)&raddr, &val);
        puts("get!");

// 循环接受客户端发来的信息
        while(1) {
                puts("waiting data....");
                read(clientfd, rbuf, sizeof(rbuf));
                printf("客户端传来数据: %s\n", rbuf);
                strncpy(rbuf, "hello world too.\n", sizeof("hello world too.\n"));
                write(clientfd, rbuf, sizeof(rbuf));
                printf("发送给客户端数据: %s", rbuf);
                bzero(rbuf, 50);

        }

        close(sockfd);
        close(clientfd);
        return 0;
}
```

# Android 客户端

## NDK

应为tcp的服务端是用c语言写的，所以为了android能够连接，我使用了ndk，ndk具体的配置可以自行百度。

##  网络权限

因为要进行网络连接，所以我们必须在mainfests文件中申请网络权限。如果没有权限创建socket会直接失败。

在application上面加上一句即可

```java
 <uses-permission android:name="android.permission.INTERNET"/>
```

## layout文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/send_link"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="发送连接"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.498"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.374" />

    <TextView
        android:text="TextView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_below="@+id/send_link"
        android:layout_alignStart="@+id/send_link"
        android:layout_marginTop="69dp"
        android:id="@+id/textView"
        tools:ignore="MissingConstraints" />


</androidx.constraintlayout.widget.ConstraintLayout>
```



## MainActivity文件

```java
package com.example.test2;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    // Used to load the 'native-lib' library on application startup.
    static {
        System.loadLibrary("native-lib");
    }

    public EditText editText;

    public static native String linkTest();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Example of a call to a native method
        Button button = findViewById(R.id.send_link);
        editText = findViewById(R.id.editText);
        button.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("WrongConstant")
            @Override
            public void onClick(View v) {
                new Thread(new Runnable() { //网络连接必须在子线程中
                    @Override
                    public void run() {
                        String ret = linkTest();
                        Log.d("s", ret);
                        //Toast.makeText(getApplicationContext(), linkTest(), 1).show();
                    }
                }).start();
            }
        });
    }

}

```

## cpp文件

```c
#include <jni.h>
#include <string>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <ctype.h>
#include <android/log.h>

#define  LOG_TAG    "mysocket"
#define  LOGI(...)  __android_log_print(ANDROID_LOG_INFO,LOG_TAG,__VA_ARGS__)

#define SERV_IP "123.56.252.111"
#define SERV_PORT 6666

extern "C"
JNIEXPORT jstring JNICALL
Java_com_example_test2_MainActivity_linkTest(JNIEnv *env, jclass clazz) {
    int cfd;
    struct sockaddr_in serv_addr;
    socklen_t serv_addr_len;

    cfd = socket(AF_INET, SOCK_STREAM, 0);
    if(cfd < 0) {
        return env->NewStringUTF("socket failed.");
    }
    LOGI("socket successful");
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(SERV_PORT);
    inet_pton(AF_INET, SERV_IP, &serv_addr.sin_addr.s_addr);
    LOGI("connecting!");
    int ret = connect(cfd, (sockaddr *)&serv_addr, sizeof(serv_addr));
    if(ret < 0) {
        LOGI("connect failed.");
        return env->NewStringUTF("连接失败");
    }
    LOGI("connect successful");
    char buf[1024] = "hello world\n";
    write(cfd, buf, sizeof(buf));
    bzero(buf, 1024);
    read(cfd, buf, sizeof(buf));

    return env->NewStringUTF(buf);
}

```

# 连接

我们点击模拟器中的连接按钮，可以在android日志中发现连接成功，并成功相互发送数据

![](https://wx2.sinaimg.cn/mw690/0083TyOJly1gjxcbubznej31yd07qq6a.jpg)
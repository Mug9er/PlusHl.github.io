---
title: Deepin安装NVIDIA以及refind
mathjax: true
categories:
  - 配置
  - Deepin
tags:
  - NVIDIA显卡
  - refind引导
---

<meta name = "referrer" content = "no-referrer" />

![](https://wx3.sinaimg.cn/mw690/0083TyOJly1gpw3tka7pkj31hc0u01kb.jpg)

# Deepin安装NVIDIA驱动

## 安装驱动

### 下载驱动

首先根据自己电脑独显的型号去NVIDIA[官网](https://www.nvidia.cn/geforce/drivers/)选择对应驱动

如果不确定自己电脑显卡型号，可以用`sudo lshw -numeric -C display`来查看

### 卸载以前的驱动

如果之前在Linux中安装过NVIDIA驱动的话，请将其全部删除

```bash
sudo apt autoremove nvidia
```

### 禁用nouveau

nouveau是通过逆向“Nvidia的Linux驱动”创造的一个开源第三方Nvidia显卡驱动程序，因此其效果差，性能低。在手动安装NVIDIA时需要禁用nouveau驱动。

终端执行以下命令修改文件。

```
sudo vi /etc/modprobe.d/blacklist.conf
```

以下内容复制到文件中

```
blacklist nouveau   
blacklist lbm-nouveau   
options nouveau modeset=0 
alias nouveau off   
alias lbm-nouveau off
```

保存退出。
其中，blacklist nouveau是禁用nouveau第三方驱动，之后不需要改回来
由于nouveau是构建在内核中的，所以要执行下面命令生效:

```
sudo update-initramfs -u
```

### 重启

```
reboot
```


重启后查看nouveau有没有运行,没输出代表禁用生效

```
lsmod | grep nouveau  
```

### 关闭图形界面
安装Nvidia驱动程序时，需要停止当前的图形界面。
使用快捷键CTRL+ALT+F2进入超级终端，登录账号，并关闭图形界面：

```
sudo service lightdm stop
```

### 给驱动文件添加执行权限
下载好的nvidia驱动文件是.run，需要添加执行权限。
使用cd指令进入下载好的驱动文件路径，如果没有改浏览器的下载路径，路径一般是/home/（你的用户名）/Downloads 。

```
sudo chmod +x NVIDIA***.run  #记得文件名改成自己下载的文件。
```


### 驱动安装

```
sudo ./NVIDI**.run  #记得文件名改成自己下载的文件。
```


这个时候会出现一个页面，一系列yes，还有一个界面选择install and cover，意为安装和覆盖。然后等待几分钟。

### 重启

```
reboot
```


这样NVIDIA驱动就装好了。

## 检测NVIDIA驱动是否成功安装

### 使用**nvidia-settings**命令

```bash
nvidia-settings
```

可以看到显卡数据

### 使用nvidia-smi命令
英伟达系统管理接口（NVIDIA System Management Interface, 简称 nvidia-smi）是基于NVIDIA Management Library 的命令行管理组件,旨在帮助管理和监控NVIDIA GPU设备。

```
nvidia-smi
```

执行这条命令将会打印出当前系统安装的NVIDIA驱动信息

### 命令行搜索集显和独显

```bash
lspci | grep VGA     # 查看集成显卡
lspci | grep NVIDIA  
```

### 查看nouveau是否运行

```bash
lsmod | grep nouveau
```

## 集显与独显切换

笔记本外出时使用集显可以节省电量，增长待机时间。
可以使用插件：dde-dock-switch_graphics_card
Github：https://github.com/zty199/dde-dock-switch_graphics_card
安装后可以方便地在dock栏切换显卡

# 使用refind引导win10和deepin

 ## 安装refind

最好在deepin环境下安装refind，因为这样比较简单。

在deepin环境下安装refind有两种方法，使用终端命令行或者下载安装包。

```
sudo apt-add-repository ppa:rodsmith/refind
sudo apt-get update
sudo apt-get install refind
```

安装好refind后重启，你会发现电脑默认引导已经变成了refind，EFI 分区也出现了refind文件夹。但此时的引导界面有两个问题：

1、选项很多，而且界面很丑；
2、选择deepin系统后还是会进入grub引导界面，浪费时间。

因此接下来我们需要修改一些东西。

## 修改

### 设置grub等待时间为0

在deepin中，通用>启动>启动延时关闭

### 下载好看的refind主题

首先下载主题压缩包，特别推荐我自己使用的这款极简主题（自带凤凰系统的图标），下载地址：

github：https://github.com/EvanPurkhiser/rEFInd-minimal

将解压后的文件放入refind文件夹下的themes文件夹（没有的话可以自行创建）内，可以在deepin环境下使用终端命令操作，也可以切换到win10系统用diskgenius软件进行操作。

### 修改refind配置文件

使用deepin终端修改/EFI/refind/refind.conf文件，需要使用的基本命令如下：

```
su root    #获取root权限
vim 你的目录/refind.conf    #使用vim修改文件
i    #进入修改模式
ESC按键    #退出修改模式
:wq    #保存并退出
```

进入vim编辑模式后，可以看到配置文件有大量的注释，需要修改的命令行其实只有如下几处：

```
timeout 3
resolution 1920 1080
dont_scan_files /EFI/ubuntu/grubx64.efi,/EFI/UOS/fbx64.efi,/EFI/UOS/mmx64.efi,/EFI/UOS/shimx64.efi,/EFI/boot/bootx64.efi,/EFI/boot/grubx64.efi
scan_all_linux_kernels false
include  themes/rEFInd-minimal/theme.conf
```

这样就可以用refind引导deepin和win10了
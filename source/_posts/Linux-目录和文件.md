---
title: Linux 目录和文件
categories: [Linux 学习笔记]
tags: [Linux目录文件]
abbrlink: 920965dc
date: 2021-04-27 16:23:54
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-j3e31w.2qk9j7xtb2a0.jpg
---

Linux 目录和文件

<!-- less-->

# Linux 目录与文件

## 目录与路径

[绝对路径]文件位置： 

```
windows: 盘符:\文件夹\文件
linux: /home/文件夹/0612/day01/a
```

[相对路径]当前目录所在位置0612 ./day01/a 

```
.代表当前目录
.. 上一级文件夹
```

### 目录创建规则

- 长度不超过256
- 不能包含特殊字符
- 见名知意

## Linux 目录结构

- `/`: 根目录，一般根目录下只存放目录，在`linux`下有且只有一个根目录。
- `/bin,/usr/bin`: 可执行二进制文件的目录，如常用的命令`ls、tar、mv、cat`等。
- `/boot`: 放置`linux`系统启动是用到的一些文件，如Linux的内核文件 `/boot/vmlinuz`，系统引导管理器:`/boot/grub`。
- `/dev`: 放置`linux`系统下的设备文件，访问该目录下某个文件，相当于访问某个设备，常用的是挂载光驱 `mount /dev/chrom/mnt`。
- `/etc`:系统配置文件存放的目录，不建议在此目录下存放可执行文件，重要的配置文件有`/etc/inittab、/etc/fstab、/etc/init.d/、/etc/X11、/etc/sysconfig、/etc/xinetd.d`。
- `/home`:系统默认的用户家目录，新增用户帐号时，用户的家目录都存放在此目录，`~`表示当前用户的家目录，`~edu`表示用户`edu`的家目录。
- `/lib、/usr/lib、/usr/local/lib`:系统使用的函数库的目录，程序在执行过程中，需要调用一些额外的参数时需要函数库的协助。
- `/lost+fount`:系统异常产生错误时，会将一些遗失的片段放置与此目录下。
- `/mnt、/media`:光盘默认挂载点，通常光盘挂载与`/mnt/chrom`下，也不一定，可以选择任意位置挂载。
- `/opt`:给主机额外安装软件所摆放的目录。
- `/proc`:此目录的数据都在内存中，如系统核心、外部设备、网络状态，由于数据都存放在内存中，所以不占用磁盘空间，比较重要的目录有`/proc/cpuinfo、/proc/interrupts、/proc/dma、/proc/ioports、/proc/net/*`等。
- `/root`:系统管理员`root`的家目录。
- `/sbin、/usr/bin、/usr/local/sbin`:放置系统管理员使用的可执行命令，如`fdisk、shutdown、mount`等，与`/bin`不同的是，这几个目录是给系统管理员`root`使用的命令，一般用户只能查看而不能设置和使用。
- `/tmp`: 一般用户或正在执行的程序临时存放文件的目录，任何人都可以访问，重要的数据不可放置在此目录下。

## 文件

计算机中一切皆文件

```
在windows中区分文件通过扩展名区分文件，在linux中通过颜色区分也可以通过命令区分 file 文件名
```

### 文件分类

- 普通文件
- 目录文件
- 设备文件
  - 字符设备文件
  - 块设备文件

- 管道文件

- 链接文件

### 文件权限

读[r]， 写[w]，执行[x]

|  d   |     rwx      |    rwx     |   rwx    |
| :--: | :----------: | :--------: | :------: |
| 目录 | 文件所属用户 | 文件所属组 | 其他用户 |


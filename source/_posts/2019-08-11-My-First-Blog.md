---
title: My First Blog
mathjax: true
categories: 杂谈
tags: Hexo
abbrlink: 81cc
date: 2019-08-11 14:57:09
---

[![1sr9MR.md.jpg](https://wx2.sinaimg.cn/mw690/0083TyOJly1gblviaaj7aj31hc0tpgwa.jpg)](https://imgchr.com/i/1sr9MR)

这是我的第一篇博客，主要写一些Hexo的配置

<!-- less -->

# 一. Hexo + Github 搭建博客：

[跟着这篇博客走即可](https://blog.csdn.net/ainuser/article/details/77609180)

# 二：Hexo 主题配置

Hexo目录下的_config.yml称为站点配置文件

Hexo/themes/next/目录下的_config.yml称为主题配置文件

## 1. next主题

下载next主题

![img1](https://wx3.sinaimg.cn/mw690/0083TyOJly1gblv57b6g3j30om01v74a.jpg)

```stylus
 git clone https://github.com/theme-next/hexo-theme-next themes/next
```

在站点配置文件 `_config.yml`

![img2](https://wx2.sinaimg.cn/mw690/0083TyOJly1gblv59sp7bj30el03i0t4.jpg)

```yaml
# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: next
```

在主题配置文件`_config.yml`中可以选择四种scheme，我选择的是`Gemini`

![img3](https://wx1.sinaimg.cn/mw690/0083TyOJly1gblv5clsagj309q07raa7.jpg)

```yaml
# ---------------------------------------------------------------
# Scheme Settings
# ---------------------------------------------------------------

# Schemes
#scheme: Muse
#scheme: Mist
#scheme: Pisces
scheme: Gemini
```

## 2. 基本信息配置

配置站点配置文件`_config.yml`

```yaml
title: 标题
subtitle: 副标题
description: 描述
author: 作者
language: 语言（简体中文是zh-Hans）
timezone: 网站时区（Hexo 默认使用您电脑的时区，不用写）
```

## 3. 菜单信息配置：

配置主题配置文件`_config.yml`

```yaml
menu:
  home: / || home
  about: /about/ || user
  tags: /tags/ || tags
  categories: /categories/ || th
  archives: /archives/ || archive
  #schedule: /schedule/ || calendar
  #sitemap: /sitemap.xml || sitemap
  #commonweal: /404/ || heartbeat

# Enable/Disable menu icons.
menu_icons:
  enable: true
```



## 4. 设置标签，分类页面

在Git-Bash中输入：

```yaml
hexo new page "tags"
hexo new page "categories"
hexo new page "about"
```

![img4](https://wx4.sinaimg.cn/mw690/0083TyOJly1gblv5ezol4j30c401kjrb.jpg)

这时在`Hexo/source/`下出现一个`tags/index.md`和`categories/index.md`

这时你修改`index.md`的属性，新加`type`属性

`tags的index`

```yaml
---
title: 标签
data: 2019-08-10 00:11:16
type: "tags"
comments: false
---
```

`categories的index`

```yaml
---
title: 分类
date: 2019-08-10 00:08:44
type: "categories"
comments: false
---
```

`about的index`

```yaml
---
title: 这是我的自我介绍
layout: about
comments: false
---
```

`comments: false`是关闭评论功能

## 5. 搜索功能

在Hexo的根目录下执行

```yaml
npm install hexo-generator-searchdb --save
```

站点配置文件`_config.yml`

```yaml
search: # 本地搜索插件
  path: search.xml
  field: post
  format: html
  limit: 10000
```

在主题配置文件`_config.yml`中

```yaml
local_search:
  enable: true
  # if auto, trigger search by changing input
  # if manual, trigger search by pressing enter key or search button
  trigger: auto
  # show top n results per article, show all results by setting to -1
  top_n_per_article: 1
```

## 6. 头像设置

把你要作为头像的图片放到：`Hexo/themes/next/source/images`

然后更改主题配置文件`_config.yml`中的 `Sidebar Avaatar`

```yaml
avatar: /images/header.jpg
```

## 7. 网站缩略图图标

把你要作为缩略图的图片放到：`Hexo/themes/next/source/images`

然后打开主题配置文件`_config.yml`,找到 `favicon`，修改成这样

```yaml
favicon:
  small: /images/header.jpg
  medium: /images/header.jpg
  apple_touch_icon: /images/header.jpg
  safari_pinned_tab: /images/logo.svg
  #android_manifest: /images/manifest.json
  #ms_browserconfig: /images/browserconfig.xml

```

## 8. 修改链接文本样式

打开`Hexo/themes/next/source/css/_common/components/post.styl`，添加

```stylus
.post-body p a {
  color: #0593d3;
  border-bottom: none;
  border-bottom: 1px solid #0593d3;
  &:hover {
    color: #fc6423;
    border-bottom: none;
    border-bottom: 1px solid #fc6423;
  }
}
```

## 9. 添加评论系统

注册登录[来必力](https://www.livere.com/), 安装City，获得安装代码中的`data-uid="xxx"`

配置主题配置文件`_config.yml`,添加`LiveRe Uid`:

```yaml
livere_uid: #你的LiveRe UID
```

## 10. 添加访问计数

next已经集成了busuanzi计数，编辑`Hexo/themes/next/layout/_third-party/analytics/busuanzi-counter.swig` 

将

`<script async src="https://dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>`

改为

`<script async src="https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>`

主题配置文件`_config.yml`

```yaml
# Show PV/UV of the website/page with busuanzi.
# Get more information on http://ibruce.info/2015/04/04/busuanzi/
busuanzi_count:
  # count values only if the other configs are false
  enable: true
  # custom uv span for the whole site
  site_uv: true
  total_visitors: true
  total_visitors_icon: user
  total_view: true
  total_views_icon: eye
  post_views: false
  post_view_icon: eye
  site_uv_header: <i class="fa fa-user"></i> 访客数
  site_uv_footer: 人
  # custom pv span for the whole site
  site_pv: true
  site_pv_header: <i class="fa fa-eye"></i> 总访问量
  site_pv_footer: 次
  # custom pv span for one page only
  page_pv: true
  page_pv_header: <i class="fa fa-file-o"></i>  阅读数
  page_pv_footer: 次
```

## 11. 文章版权信息

编辑主题配置文件`_config.yml`，修改

```yaml
post_copyright:
  enable: true
```

## 12. 打赏

编辑主题配置文件`_config.yml`,修改

```yaml
# Reward
reward_comment: 求打赏文本
wechatpay: /images/wechatpay.png  # 微信收款二维码 图片路径
alipay: /images/alipay.png        # 支付宝收款二维码 图片路径
#bitcoin: /images/bitcoin.png     # 比特币
```

## 13. 添加更新时间

编辑主题配置文件`_config.yml`,修改

```yaml
post_meta:
  item_text: true
  created_at: true   # 创建时间
  updated_at: true   # 更新时间
  # Only show 'updated' if different from 'created'.
  updated_diff: false # 只使用更新时间
  # If true, post's time format will be hexo config's date_format + ' ' + time_format.
  date_time_merge: false
  categories: true
```

## 14. 修改文章底部的标签

编辑`Hexo/themes/next/layout/_macro/post.swig`

找到`rel="tag">#`

将`#`改为`<i class="fa fa-tag"></i>`

## 15. 文章底部添加"本文结束"

编辑`Hexo/themes/next/laayout/_macro/post.swig`，在文章结束的地方加上

```python
{% if not is_index %}
    <div style="text-align:center;color: #ccc;font-size:14px;">
        ---------Thanks for your attention---------
    </div>
{% endif %}
```

## 16. 在页脚添加运行时间

编辑`themes/next/layout/_partials/footer.swig`

在所示位置加上代码：

![img5](https://wx3.sinaimg.cn/mw690/0083TyOJly1gblv5hgdmij30so0j0diq.jpg)

```python
{### 运行时间 ####}
<span id="sitetime"></span>
<script language=javascript>
	function siteTime(){
		window.setTimeout("siteTime()", 1000);
		var seconds = 1000;
		var minutes = seconds * 60;
		var hours = minutes * 60;
		var days = hours * 24;
		var years = days * 365;
		var today = new Date();
		var todayYear = today.getFullYear();
		var todayMonth = today.getMonth()+1;
		var todayDate = today.getDate();
		var todayHour = today.getHours();
		var todayMinute = today.getMinutes();
		var todaySecond = today.getSeconds();
		/* Date.UTC() -- 返回date对象距世界标准时间(UTC)1970年1月1日午夜之间的毫秒数(时间戳)
		year - 作为date对象的年份，为4位年份值
		month - 0-11之间的整数，做为date对象的月份
		day - 1-31之间的整数，做为date对象的天数
		hours - 0(午夜24点)-23之间的整数，做为date对象的小时数
		minutes - 0-59之间的整数，做为date对象的分钟数
		seconds - 0-59之间的整数，做为date对象的秒数
		microseconds - 0-999之间的整数，做为date对象的毫秒数 */
		var t1 = Date.UTC(2018,02,13,15,00,00); //北京时间2018-2-13 00:00:00
		var t2 = Date.UTC(todayYear,todayMonth,todayDate,todayHour,todayMinute,todaySecond);
		var diff = t2-t1;
		var diffYears = Math.floor(diff/years);
		var diffDays = Math.floor((diff/days)-diffYears*365);
		var diffHours = Math.floor((diff-(diffYears*365+diffDays)*days)/hours);
		var diffMinutes = Math.floor((diff-(diffYears*365+diffDays)*days-diffHours*hours)/minutes);
		var diffSeconds = Math.floor((diff-(diffYears*365+diffDays)*days-diffHours*hours-diffMinutes*minutes)/seconds);
		document.getElementById("sitetime").innerHTML=" 已运行"+diffYears+" 年 "+diffDays+" 天 "+diffHours+" 小时 "+diffMinutes+" 分钟 "+diffSeconds+" 秒";
	}/*因为建站时间还没有一年，就将之注释掉了。需要的可以取消*/
	siteTime();
</script>
```

## 17. Latex公式

更换Hexo的Markdown渲染引擎

```c
npm uninstall hexo-renderer-marked --save
npm install hexo-renderer-kramed --save
```

然后打开`node_modules/kramed/lib/rules/inline.js`

替换11行的escape变量

```c
//  escape: /^\\([\\`*{}\[\]()#$+\-.!_>])/,
  escape: /^\\([`*\[\]()#$+\-.!_>])/
```

改变20行的em变量

```c
//  em: /^\b_((?:__|[\s\S])+?)_\b|^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
  em: /^\*((?:\*\*|[\s\S])+?)\*(?!\*)/
```

next集成了Mathjax，编辑主题配置文件`_config.yml`

```yaml
# MathJax Support
mathjax:
  enable: true
  per_page: true
  engine: mathjax
  cdn: //cdn.bootcss.com/mathjax/2.7.1/latest.js?config=TeX-AMS-MML_HTMLorMML

# Han Support docs: https://hanzi.pro/
han: false
```

在写文章时要在文章的配置中加上`mathjax: true`

## 18. 短链接

在根目录执行

`npm install hexo-abbrlink --save`

配置站点配置文件`_config.yml`,修改

```yaml
# abbrlink config
abbrlink:
  alg: crc16 #support crc16(default) and crc32
  rep: hex    #support dec(default) and hex

# 更改 permalink 值
permalink: /:abbrlink/
```

## 19. 文章封面图片

在根目录执行

`npm install --save hexo-less`

在写文章时手动设置文章摘要`<!-- less -->`为分界线

## 20. social 

修改主题配置文件`_config.yml`

```yaml
social:
  #GitHub: https://github.com/yourname || github
  #Google: https://plus.google.com/yourname || google
  #Twitter: https://twitter.com/yourname || twitter
  #E-Mail: mailto:yourname@gmail.com || envelope
  #FB Page: https://www.facebook.com/yourname || facebook
  #VK Group: https://vk.com/yourname || vk
  #StackOverflow: https://stackoverflow.com/yourname || stack-overflow
  #YouTube: https://youtube.com/yourname || youtube
  #Instagram: https://instagram.com/yourname || instagram
  #Skype: skype:yourname?call|chat || skype

social_icons:
  enable: true
  GitHub: github
  Twitter: twitter
  微博: weibo
```

## 21. 友链

修改主题配置文件`_config.yml`

```yaml
# Blog rolls
links_icon: link
links_title: Friend Links
links_layout: block
#links_layout: inline
links:
  github: http://github.com/
```

## 22. 字数统计和阅读时长

在根目录执行

`npm install hexo-symbols-count-time --save`

修改站点配置文件`_config.yml`

```yaml
symbols_count_time:
 #文章内是否显示
  symbols: true
  time: true
 # 网页底部是否显示
  total_symbols: true
  total_time: true
```

修改主题配置文件`_config.yml`

```yaml
# Post wordcount display settings
# Dependencies: https://github.com/theme-next/hexo-symbols-count-time
symbols_count_time:
  separated_meta: true
  #文章中的显示是否显示文字（本文字数|阅读时长） 
  item_text_post: true
  #网页底部的显示是否显示文字（站点总字数|站点阅读时长） 
  item_text_total: false
  # Average Word Length (chars count in word)
  awl: 4
  # Words Per Minute
  wpm: 275
```

## 23. 隐藏网页底部信息

修改主题配置文件`_config.yml`

```yaml
footer:
  # Specify the date when the site was setup.
  # If not defined, current year will be used.
  #since: 2015

  # Icon between year and copyright info.
  icon: user
  counter: true

  # If not defined, will be used `author` from Hexo main config.
  copyright:
  # -------------------------------------------------------------
  # Hexo link (Powered by Hexo).
  powered: false

  theme:
    # Theme & scheme info link (Theme - NexT.scheme).
    enable: false
    # Version info of NexT after scheme info (vX.X.X).
    version: false
  # -------------------------------------------------------------
  # Any custom text can be defined here.
  #custom_text: Hosted by <a target="_blank" href="https://pages.github.com">GitHub Pages</a>

# ---------------------------------------------------------------
# SEO Settings
# ---------------------------------------------------------------

# Canonical, set a canonical link tag in your hexo, you could use it for your SEO of blog.
# See: https://support.google.com/webmasters/answer/139066
# Tips: Before you open this tag, remember set up your URL in hexo _config.yml ( ex. url: http://yourdomain.com )
canonical: true

# Change headers hierarchy on site-subtitle (will be main site description) and on all post/pages titles for better SEO-optimization.
seo: false

# If true, will add site-subtitle to index page, added in main hexo config.
# subtitle: Subtitle
index_with_subtitle: false
```

## 24. 设置RSS

在根目录执行

`npm install hexo-generator-feed --save`

修改站点配置文件`_config.yml`,在`Extensions`下添加

```yaml
# RSS订阅
feed:
  type: atom
  path: atom.xml
  limit: 20
  hub:
  content:
  content_limit: 140
  content_limit_delim: ' '
```

修改主题配置文件 `_config.yml`修改`rss`为

`rss: /atom.xml`

## 25. 修改字体

在GItHub上[下载](https://github.com/crozynski/comicneue)后，解压后将所有Web文件夹下的所有内容放入`Hexo/theme/next/source/fonts`

然后修改`Hexo/themes/next/source/css/_custom/custom.styl`

```stylus
//字体
@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Light.eot');
  src: url('/fonts/ComicNeue-Light.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Light.woff2') format('woff2'),
       url('/fonts/ComicNeue-Light.woff') format('woff'),
       url('/fonts/ComicNeue-Light.ttf')  format('truetype');
  font-weight: 300;
}

@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Light-Oblique.eot');
  src: url('/fonts/ComicNeue-Light-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Light-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Light-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Light-Oblique.ttf')  format('truetype');
  font-weight: 300;
  font-style: oblique;
}

@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Regular.eot');
  src: url('/fonts/ComicNeue-Regular.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Regular.woff2') format('woff2'),
       url('/fonts/ComicNeue-Regular.woff') format('woff'),
       url('/fonts/ComicNeue-Regular.ttf')  format('truetype');
  font-weight: 400;
}

@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Regular-Oblique.eot');
  src: url('/fonts/ComicNeue-Regular-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Regular-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Regular-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Regular-Oblique.ttf')  format('truetype');
  font-weight: 400;
  font-style: oblique;
}

@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Bold.eot');
  src: url('/fonts/ComicNeue-Bold.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Bold.woff2') format('woff2'),
       url('/fonts/ComicNeue-Bold.woff') format('woff'),
       url('/fonts/ComicNeue-Bold.ttf')  format('truetype');
  font-weight: 700;
}

@font-face {
  font-family: 'Comic Neue';
  src: url('/fonts/ComicNeue-Bold-Oblique.eot');
  src: url('/fonts/ComicNeue-Bold-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Bold-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Bold-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Bold-Oblique.ttf')  format('truetype');
  font-weight: 700;
  font-style: oblique;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Light.eot');
  src: url('/fonts/ComicNeue-Angular-Light.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Light.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Light.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Light.ttf')  format('truetype');
  font-weight: 300;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Light-Oblique.eot');
  src: url('/fonts/ComicNeue-Angular-Light-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Light-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Light-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Light-Oblique.ttf')  format('truetype');
  font-weight: 300;
  font-style: oblique;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Regular.eot');
  src: url('/fonts/ComicNeue-Angular-Regular.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Regular.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Regular.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Regular.ttf')  format('truetype');
  font-weight: 400;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Regular-Oblique.eot');
  src: url('/fonts/ComicNeue-Angular-Regular-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Regular-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Regular-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Regular-Oblique.ttf')  format('truetype');
  font-weight: 400;
  font-style: oblique;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Bold.eot');
  src: url('/fonts/ComicNeue-Angular-Bold.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Bold.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Bold.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Bold.ttf')  format('truetype');
  font-weight: 700;
}

@font-face {
  font-family: 'Comic Neue Angular';
  src: url('/fonts/ComicNeue-Angular-Bold-Oblique.eot');
  src: url('/fonts/ComicNeue-Angular-Bold-Oblique.eot?#iefix') format('embedded-opentype'),
       url('/fonts/ComicNeue-Angular-Bold-Oblique.woff2') format('woff2'),
       url('/fonts/ComicNeue-Angular-Bold-Oblique.woff') format('woff'),
       url('/fonts/ComicNeue-Angular-Bold-Oblique.ttf')  format('truetype');
  font-weight: 700;
  font-style: oblique;
}
```

修改主题配置文件 `_config.yml`修改`font`为

```yaml
font:
  enable: true

  # Uri of fonts host. E.g. //fonts.googleapis.com (Default).
  host:

  # Font options:
  # `external: true` will load this font family from `host` above.
  # `family: Times New Roman`. Without any quotes.
  # `size: xx`. Use `px` as unit.

  # Global font settings used on <body> element.
  global:
    external: true
    family: 'Comic Neue'
    size:

  # Font settings for Headlines (h1, h2, h3, h4, h5, h6).
  # Fallback to `global` font settings.
  headings:
    external: true
    family: 'Comic Neue'
    size:

  # Font settings for posts.
  # Fallback to `global` font settings.
  posts:
    external: true
    family: 'Comic Neue'

  # Font settings for Logo.
  # Fallback to `global` font settings.
  logo:
    external: true
    family: 'Comic Neue'
    size:

  # Font settings for <code> and code blocks.
  codes:
    external: true
    family: 'Comic Neue'
    size:
```

刚开始的字体是默认14px，在代码部分会很小，所以可以在`themes/next/source/css/_variables/base.styl`

修改 font size和code font  为18px就很好

## 26. 设置新建文件配置

进入`Hexo/scaffolds`修改`post.md`

```yaml
---
title: {{ title }}
date: {{ date }}
mathjax: true
categories:
tags:
---
```

## 27. 新建带日期的博文

修改站点配置文件`-config.yml`

```yaml
# Writing
new_post_name: :year-:month-:day-:title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link: true # Open external links in new tab
filename_case: 0
render_drafts: false
post_asset_folder: true # 同时生成一个文件夹
relative_link: false
future: true
highlight: # Hexo自带代码高亮插件
  enable: true
  line_number: true
  auto_detect: false
  tab_replace:
```

## 28. 背景图片

把背景图片存放到`Hexo/themes/next/source/images`

再在`Hexo/themes/next/source/css/_custom/custom/styl`修改一下

```stylus
body { background:url(/images/music.png);}
```





参考博客：

https://www.jianshu.com/p/3a05351a37dc

https://www.cnblogs.com/liziczh/p/9318656.html

https://xian6ge.netlify.com/posts/82ce1911/

https://www.jianshu.com/p/805bd0b65d98https://www.jianshu.com/p/805bd0b65d98

https://www.jianshu.com/p/3a01cc514ce7?utm_source=oschina-app

https://leflacon.github.io/7167e0bc/


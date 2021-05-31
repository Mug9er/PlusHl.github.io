---
title: vscode 配置Vue
categories: [配置]
tags: [VSCode, Vue]
abbrlink: 9c6f56ad
date: 2020-11-29 11:20:30
img: https://cdn.jsdelivr.net/gh/Mug-9/imge-stroage@master/cover/wallhaven-e7ozz8.1jregieez3q8.png
---

vscode 配置Vue

<!-- less -->

## 插件

### Auto Close Tag

自动关闭标签

### background-cover

可以设置壁纸

### BetterComments

注释可以变颜色，便于区分

默认五种颜色

![img1](https://wx1.sinaimg.cn/mw690/0083TyOJly1gl5vwju72tj304r03xmxg.jpg)

### Bracket Pair Colorizer 2

括号匹配并能标颜色

### Code Spell Checker

检查错误单词，并给出相近单词

![img2](https://wx1.sinaimg.cn/mw690/0083TyOJly1gl5w081g3lj307b08u3zu.jpg)

### EditorConfig fot VS Code

让vscode支持.editorconfig文件

.editorconfig文件可以规范编码风格和设置

#### 在项目根目录建立`.editorconfig`文件

```js
[*.{js,jsx,ts,tsx,vue}]
indent_style = space
indent_size = 2
trim_trailing_whitespace = true
insert_final_newline = true
```



### ESLint

对文件进行校验，并可在保存时自动修复错误

#### 在vscode配置文件中

```js
{
  // eslint配置项，保存时自动修复错误
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  }
}
```

#### 在项目根目录建立`.eslintrc.js`文件

```js
module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/essential', '@vue/standard'],
  parserOptions: {
    parser: 'babel-eslint',
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
  },
}
```

### Live Server

本地预览界面，右键html文件选择`Open with Live Seriver`

## Prettier

对`js html`文件格式化

#### 在项目根目录建立`.prettierrc`文件

```js
{
  "semi": false,
  "singleQuote": true
}
```

#### 在VScode 配置文件中加入

```js
// 保存时自动格式化代码
  "editor.formatOnSave": true,
  // 默认使用prettier格式化支持的文件
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  // 指定 *.vue 文件的格式化工具为vetur，防止和prettier冲突
  "[vue]": {
    "editor.defaultFormatter": "octref.vetur"
  },
  // 指定 *.js 文件的格式化工具为vscode自带，以符合ESLint规范
  "[javascript]": {
    "editor.defaultFormatter": "vscode.typescript-language-features"
  }
```



### Vetur

代码高亮，代码片段，Emmet语法支持，语法错误校验检查，格式化代码，代码提醒，对第三方UI框架支持

#### 在vscode配置文件中

```js
  // 将vetur的js格式化工具指定为vscode自带的
  "vetur.format.defaultFormatter.js": "vscode-typescript",
  // 移除js语句的分号
  "javascript.format.semicolons": "remove",
  // 在函数名后面加上括号，类似这种形式 foo () {}
  "javascript.format.insertSpaceBeforeFunctionParenthesis": true
```

### Eva Theme

Eva 主题

## 我的配置文件

```json
{
  "editor.fontFamily": "Cascadia Code",
  "editor.fontSize": 20,
  "editor.fontWeight": "300",
  "editor.fontLigatures": true,
  "terminal.integrated.fontSize": 20,
  "terminal.integrated.fontWeight": "300",
  "terminal.integrated.cursorStyle": "underline",
  "debug.console.fontSize": 18,
  "workbench.iconTheme": "material-icon-theme",
  "explorer.confirmDelete": false,
  "files.autoSave": "onFocusChange",

  // 保存时自动格式化代码
  "editor.formatOnSave": true,
  // eslint配置项，保存时自动修复错误
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },

  // 让vetur使用vs自带的js格式化工具，以便在函数前面加个空格
  "vetur.format.defaultFormatter.js": "vscode-typescript",
  "javascript.format.semicolons": "remove",
  "javascript.format.insertSpaceBeforeFunctionParenthesis": true,

  // 指定 *.vue 文件的格式化工具为vetur
  "[vue]": {
    "editor.defaultFormatter": "octref.vetur"
  },

  // 指定 *.js 文件的格式化工具为vscode自带
  "[javascript]": {
    "editor.defaultFormatter": "vscode.typescript-language-features"
  },

  // 默认使用prettier格式化支持的文件
  "editor.defaultFormatter": "esbenp.prettier-vscode",

  "better-comments.multilineComments": true,
  "better-comments.highlightPlainText": false,
  "cSpell.enableFiletypes": ["vue", "vue-html"],
  "workbench.colorTheme": "Eva Dark Italic",
  "explorer.confirmDragAndDrop": false,
  "editor.tabSize": 2,
  "backgroundCover.imagePath": "e:\\picture\\2020-12-11\\wallhaven-e7ozz8.png",
  "git.confirmSync": false,
  "git.autofetch": true,
  "backgroundCover.randomImageFolder": "e:\\picture\\2020-12-07",
  "backgroundCover.autoStatus": false,
  "backgroundCover.opacity": 0.5,
  "javascript.updateImportsOnFileMove.enabled": "always",
  "git.enableSmartCommit": true,
  "window.zoomLevel": 1
}

```


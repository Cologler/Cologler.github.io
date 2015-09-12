---
title: 从零开始搭建 Github.io 静态博客
sub_title: 一·搭建环境
categories: github.io
tags: Github.io jekyll zero
layout: page
---

首先，你要知道 Github.io 是静态博客。

网站一般分动态和静态，动态大概是你访问的时候才立即生成的，静态大概是生成好了才上线让你访问。错了别怪我啊，了解个大概就好了，因为这不是本文主题。 

粗略看了下，github 提供的网页模板比较单调，所以我决定使用 Jekyll 开自己写。因此第一步我们首先来搭建一个 Jekyll 的环境。

### 0. 参考

* Jekyll 的英文官网：[http://jekyllrb.com/](http://jekyllrb.com/)
* Jekyll 的官网的汉化：[http://jekyllcn.com/](http://jekyllcn.com/)

有能力就看英文，我还是看中文吧 =。 =。

### 1. 安装 Ruby 及 DevKit

** 如果你确定你的电脑里面有安装 Ruby，可以跳过这个。**

如果你闲的无聊，可以去 [Ruby 官网](https://www.ruby-lang.org) 下载源码来编译成 Ruby 引擎，反正我是去 [RubyInstaller](http://rubyinstaller.org/downloads/) 下载已经编译好了的引擎。  

就算下载了 7z 版本的 Ruby 引擎也是要配环境变量的，所以我干脆直接下载 exe 版本的引擎。

虽然 Jekyll 安装教程没有说要安装 DevKit 包，但我实际操作时，没有 DevKit 包会在后文 `gem install jekyll` 处报错。所以这里我要引领大家走向正确的深渊。

我下载的是 2.2.3 (x64) 版本，在 RubyInstaller 网站滚下去可以看到 2.0 或以上版本的 x64 Ruby 需要安装的是 DevKit-mingw64-64-后面很长。

然后我迅速地安装了这两货。

### 2. 安装 RubyGems

好像安装好 Ruby 就自带这个了，如果没带你就去 [http://rubygems.org/pages/download](http://rubygems.org/pages/download) 下载安装吧。

### 3. 安装 NodeJS

虽说也能用其它 JavaScript 运行环境，但是这个是官方推荐的，就用这个吧。附上其 [官网](https://nodejs.org/en/)。

### 4. 安装 Jekyll

打开 PowerShell（怎么打开？Win 10 右键开始菜单就可以看见了。），输入以下命令：

`gem install jekyll`

回车，等它滚到完就好了。

### 5. 把博客源码下载下来

### 6. 创建站点

下图就是 PowerShell，你应该在第 4 步的时候看过。

![图片](/assets/image/png/A696B2680013F803581F6B3BB4A7A512209804C1.png)

其中，C:\Users\巍\ 就是当前的工作目录。

### n. 参考

* [将纯文本转换为静态博客网站](http://jekyllcn.com/)
*
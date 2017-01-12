# 学习python爬虫

## 需要的基本库
1. request,urllib 是http框架（库），用来请求以及对http发起请求，下载和解析需要自己处理，比较灵活，（requests：线程安全，unicode解码）

2. 页面解析：bs4和lxml,推荐用lxml 配合xpath。可以搭配正则（re）模块使用

3. Selenium ：是什么？：自动化测试工具。它支持各种浏览器，包括 Chrome，Safari，Firefox 等主流界面式浏览器，如果你在这些浏览器里面安装一个 Selenium 的插件，那么便可以方便地实现Web界面的测试。换句话说叫 Selenium 支持这些浏览器驱动。

4. scrapy 是个爬虫框架，包含了下载器，解析器，日志以及异常处理，基于多线程，twisted的方式处理。

## 学习爬取知乎
（参考：http://m.blog.csdn.net/article/details?id=52159871）

### 登陆
1. 登陆需要的信息由有：`邮件名（电话号）`，`验证码`，`附加信息（_xsrf）`构成，下面主要介绍这些信息如何`get`和`post`。

2. get _xsrf：

3. get captcha.gif(验证码图片):

t 是Unix时间戳
``` python
	t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
```
可以尝试自动识别验证码图片的内容


2018-04-10 10:20:51
# 摘要
scrapy 框架的学习
--------------

# 完成情况
![完成情况](https://github.com/hl211/scrapy_learn/blob/master/img/scrapy.png)

----------

# 运行
- 安装
pip install scrapy
- 入口
main.py

----------
# 注意事项
代理ip池采用的是绝对地址
---------
# 动态解析网站
1. 利用pip安装scrapy-splash库
 ```pip install scrapy-splash```
2. 安装docker,用docker运行scrapinghub/splash：
 ```docker pull scrapinghub/splash
    docker run -p 8050:8050 scrapinghub/splash
 ```
3. 配置splash服务
   ```
   #splash服务器地址
   SPLASH_URL = 'http://localhost:8050' 
   #将splash middleware添加到DOWNLOADER_MIDDLEWARE中：
    DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    } 
    #Enable SplashDeduplicateArgsMiddleware:
    SPIDER_MIDDLEWARES = {
        'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
      }
     #Set a custom DUPEFILTER_CLASS:
     DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
     a custom cache storage backend:
     HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
    ```
4. 代码编写 
***yield SplashRequest(url, self.parse, args={'wait': 0.5})*** 
```
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
```

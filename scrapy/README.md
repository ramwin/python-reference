# Scrapy参考
* [官网链接](https://doc.scrapy.org/en/latest/topics/spiders.html)
* [selector选择器](./selector选择器.md)
* [spider爬虫](./spider.md)
* [日志](./log.md)  


## 安装
```
    sudo apt-get install python3-dev libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    sudo apt install python3-dev  # 17.04
    sudo pip install Scrapy

    # 创建项目
    scrapy startproject <projectname>
    cd <projectname>
    scrapy genspider <spidername> <url>

    # 启动项目
    scrapy crawl dmoz

    # shell启动
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    response.xpath('//title')
```


## [request](https://doc.scrapy.org/en/latest/topics/request-response.html#request-objects)
```
    yield scrapy.Request(url, callback, method, headers, cookies)
```
* 参数
    * url
    * cookies
    * headers

## [middleware中间件](https://doc.scrapy.org/en/latest/topics/spider-middleware.html)

```
    class MyMiddleware(object):
        def process_spider_exception(self, response, exception, spider):
            logging.error("无法获取数据")
            logging.error("url: %s" % response.url)
            logging.error("Http状态码: %d" % response.status)
            if hasattr(spider, 'secret_key') == False:
                spider.secret_key = 1
            else:
                spider.secret_key += 1
            if spider.secret_key <= 10:
                time.sleep(60*secret_key)
                yield scrapy.Request(response.url, callback=spider.parse)
            else:
                logging.error("重复了太多次，依然无法获取数据")
                return None
```

* [process_start_requests](https://doc.scrapy.org/en/latest/topics/spider-middleware.html#scrapy.spidermiddlewares.SpiderMiddleware.process_start_requests)
    * 注意，这个函数只有start的requests会触发，parse里面yield的request不会触发
```
    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r
```


## [pipeline](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)
* [open\_spider]  
    *初始化spider*

```
    def open_spider(self, item, spider):
        return item
```
* [close_spider]
    *关闭spider*
* [process_item]
    *处理item*

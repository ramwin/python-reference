**Xiang Wang @ 2017-05-10 16:36:08**

# 基础

## 示例
```
    class TextSpider(scrapy.Spider):
        name = "text"
        allowed_domains = ["www.ramwin.com"]
        start_urls = ['http://www.ramwin.com/testrest/text']

```

## function
* parse
```
    def parse(self, response):
        # 解析response
        yield {}  # 返回一个可以被 item 解析的字典
        yield scrapy.Request(url, callback=self.part)  # 生成一个新的队列
```

* [start\_requets]  

*生成一系列的requests*
```
    
```

# 基础
## 安装
    sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    sudo apt install python3-dev  # 17.04
    sudo pip install Scrapy
## 创建项目
    scrapy startproject <projectname>
    cd <projectname>
    scrapy genspider <spidername> <url>
## 修改
    items.py
## 创建
    dmoz_spider.py
## 启动项目
    scrapy crawl dmoz
## shell启动   
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    response.xpath('//title')


# 参考
* [官网链接](https://doc.scrapy.org/en/latest/topics/spiders.html)
* [selector选择器](./selector选择器.md)
* [spider爬虫](./spider.md)
* [日志](./log.md)

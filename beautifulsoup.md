# 安装
pip install beautifulsoup4  [官方安装教程](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

    import urllib2    
    net='http://pm25.in/'+'nanjing'
    temp=urllib2.urlopen(net).read()

    from bs4 import BeautifulSoup
    soup=BeautifulSoup(temp)
    soup.find(id="detail-data").tbody.find_all('tr')[0].tekxt
    soup里面找到id是"detail-data"的区域,里面的tbody标签下找到所有的tr表格,选取第一个表格,输出他的字符串

# 基础用法
## 生成对象:
    soup = BeautifulSoup( string )

## 查找对象
    soup.find( id = 'demo' )            通过id查找
    soup.find( class_ = 'demos')    通过 class 查找对象,由于class是python的保留词,所以用class_代替
    soup.a          soup.find_all('a')                     通过标签查找

## 获取对象信息
    objec.get('href')                    获得超链接地址

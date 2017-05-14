#### Xiang Wang @ 2016-09-02 18:06:52

## ubuntu 安装 Pillow
[参考文档](http://pillow.readthedocs.io/en/3.1.x/installation.html#external-libraries)  

```
    # 16.04
    sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp5 libwebp-dev tk openjpeg-tools 
    # 17.04
    sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp6 libwebp-dev tk
```


## Image
    im = Image.open(path, 'r')

### 尺寸修改
    im.crop(0,0,100,100).save(path)
    im.resize((28.28))

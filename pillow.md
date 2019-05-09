**Xiang Wang @ 2016-09-02 18:06:52**

[官网文档](https://pillow.readthedocs.io/en/stable/index.html)

### [安装][install]

```
# 16.04
sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp5 libwebp-dev tk openjpeg-tools 
# 17.04
sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp6 libwebp-dev tk
```

### 参考文档
#### Image  
`im = Image.open(path, 'r')`

##### 尺寸修改
```
im.crop(0,0,100,100).save(path)
im.resize((28.28))
```

#### [ImageFont][imagefont]
* Example
```
from PIL import ImageFont, ImageDraw 
draw = ImageDraw.Draw(image)
# use a bitmap font
font = ImageFont.load("arial.pil")
draw.text((10, 10), "hello", font=font)
# use a truetype font
font = ImageFont.truetype("arial.ttf", 15)
draw.text((10, 25), "world", font=font)
```


[install]: https://pillow.readthedocs.io/en/stable/installation.html#linux-installation
[imagefont]: https://pillow.readthedocs.io/en/stable/reference/ImageFont.html

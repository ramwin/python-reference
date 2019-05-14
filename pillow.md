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
#### [Image](https://pillow.readthedocs.io/en/stable/reference/Image.html#)
* new
```
Image.new(mode, size, color=0)
Image.new("RGB", (480, 320), 0xffffff)
```
* open
`im = Image.open(path, 'r')`

#### [ImageClass](https://pillow.readthedocs.io/en/stable/reference/Image.html#the-image-class)
* paste `Image.paste(im, box=None, mask=None)`
把图片粘贴进去

* resize `Image.resize(size)`  
修改尺寸
```
im.crop(0,0,100,100).save(path)
im2 = im.resize((28.28))
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
draw.text((10, 25), "world", font=font, fill=0xff0000)
```
* getsize  
有时候写了一段文字后要加一点图标什么的，用getsize可以获取文字的长度。因为有 *kerning* 的存在，所以这个长度会比单个字符合并起来的长度短。不能直接用字体宽度乘以文字数量 [stackoverflow](https://stackoverflow.com/questions/43828955/measuring-width-of-text-python-pil)


[install]: https://pillow.readthedocs.io/en/stable/installation.html#linux-installation
[imagefont]: https://pillow.readthedocs.io/en/stable/reference/ImageFont.html

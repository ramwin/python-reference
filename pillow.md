# pillow

[官网文档](https://pillow.readthedocs.io/en/stable/index.html)

# [安装][install]

```
# 16.04
sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp5 libwebp-dev tk openjpeg-tools 
# 17.04
sudo apt install -yqq libjpeg9 zlib1g zlib1g-dbg libjpeg9 libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev libfreetype6 libfreetype6-dev liblcms2-2 liblcms2-dev libwebp6 libwebp-dev tk
```

# 参考文档
## [Image](https://pillow.readthedocs.io/en/stable/reference/Image.html#)
* eval
[测试](./pillow_example/eval.py)  
把一个函数作用于每个像素的每个维度的值。注意，传入的是红绿蓝分别的int,而不是一个颜色的tuple
```
def only_extreme_color(x):
    if 20 < x < 235:
        return 0  # 不要中间颜色
    return x  # 或者return 255
img = Image.open("原图")
Image.eval(img, only_extreme_color).save("result.png")
```
* new
```
Image.new(mode, size, color=0)
Image.new("RGB", (480, 320), 0xffffff)  
Image.new("RGBA", (480, 320), 0xffffffff)   # 透明度, 蓝, 绿, 红
```
* open
`im = Image.open(path, 'r')`

## [ImageClass][image-class]
* paste `Image.paste(im, box=None, mask=None)`  
[测试image](./pillow_example/image_test.py)
[测试mask](./pillow_example/mask_test.py)
把图片粘贴进去
mask也是一张图片。如果mask是1, 就会用粘贴的图片。如果是0就用原图  
mask的尺寸要和im一致，并且是rgba模式  
```
blue = Image.new("RGB", (480, 320), 0xffffff00)
im = Image.new("RGB", (150, 150), 0xff0000ff)
mask = Image.new("RGBA", (150, 150), 0x00000000)
draw = ImageDraw.Draw(mask)
draw.chord(((0, 0), (150, 150)), 0, 360, 0xffffffff)
blue.paste(red, (150, 150), mask=mask)
```

* resize `Image.resize(size)`  
修改尺寸
```
im.crop(0,0,100,100).save(path)
im2 = im.resize((28.28))
```

* size
返回图片的尺寸 (1980, 1080)

## [ImageDraw](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#)
```
from PIL import ImageDraw
draw = ImageDraw.Draw(image)
```
* `ImageDraw.chord`
画一个指定了起始角度和终止角度的圆圈，并链接首尾
```
draw.chord(xy, start, end, fill=None, outline=None, width=0)
```

* `ImageDraw.ellipse`
在指定区域画一个椭圆。但是估计是园的计算问题，outline里面有些像素点显示的是fill的颜色
```
draw.ellipse(xy, fill, outline, width)
```

## [ImageFont][imagefont]
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
[image-class]: https://pillow.readthedocs.io/en/stable/reference/Image.html#the-image-class

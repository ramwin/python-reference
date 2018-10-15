**Xiang Wang @ 2018-10-11 21:49:44**

# 把一个图片变成html文件
1. 用PIL模块，读取文件的像素。
    from PIL import Image
    img = Image.open('png.png', 'r')
    img.getpixel((x, y))
2. 根据文件的像素，生成很多很多的div

# 问题
1. 如何优化显示的速度
    a. 把很多div合并成一个大的div(难)
    2. 把颜色一致的div写成一个class(中)
2. 如何处理大型文件,生成像素画的感觉
    1. Image.resize
    2. 把颜色的种类调整成仅有的几个(简单)

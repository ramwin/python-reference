# python 多态的概念
## 示例:
    class Animal(object):
        def move(self):
            print('the animal is moving')

    class Dog(Animal):
        def move(self):
            print('the dog is running')

    class Bird(Animal):
        def move(self):
            print('the bird is flying')

## 解释:
### 案例一
使用 graphic.py 在一个窗口里面做图，你创建了对象 circle, rectangle,然后你要把这两个对象显示在窗口里面，你只要说 circle.draw(windows), rectangle.draw(windows) 就可以了。 而不用去处理， circle画图要找那些到圆心距离一致的点, rectangle画图需要找矩形四条边的点.
### 案例二
不管int, decimal, float都有 add, int这种功能，调用方式，意义基本一致。使用的时候直接用就可以了，而不用去理解处理如果是int，deciaml，float分别应该怎么计算

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
使用 graphic.py 在一个窗口里面做图，你创建了对象 circle, rectangle,然后你要把这两个对象显示在窗口里面，你只要说 circle.draw(windows), rectangle.draw(windows) 就可以了。 而不用去处理， circle画图要找那些到圆心距离一致的点, rectangle画图需要找矩形四条边的点.

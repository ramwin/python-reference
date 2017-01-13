#### Xiang Wang @ 2016-12-22 11:32:55


# 基础
    a = 0
    def add():
        global a  # 如果没有这个， a就只能读，不能写
        a += 1
        print(a)

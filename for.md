#### Xiang Wang @ 2016-09-29 18:18:47

# for 语句用法

## 基础
    for i in range(10):
        continue  # 继续执行
        break  # 终端所有的 for, (else也不执行)
        print(i)
    else:  # else可以不需要
        print("输出了前10个自然数")

import random



class 游戏结束(Exception):
    pass


class 无白球可放(游戏结束):
    pass


class 球已抽玩(游戏结束):
    pass


class 球袋子(object):

    def __init__(self, 黑球初始数量, 白球初始数量):
        黑球初始数量 >= 1
        白球初始数量 >= 1
        self.黑球数量 = self.黑球初始数量 = 黑球初始数量
        self.白球数量 = self.白球初始数量 = 白球初始数量

    def 抽完了(self):
        return self.黑球数量 == self.白球数量 == 0

    def 抽一个球(self):
        """
        返回球的颜色: "白球" 或 "黑球"
        或者直接报游戏结束的错误
        """
        编号 = random.randint(1, self.黑球数量 + self.白球数量)
        
        if self.黑球数量 + self.白球数量 == 1:  # 抽玩了
            raise 球已抽玩

        if 编号 <= self.黑球数量: # 抽到黑球了
            if self.白球数量 == self.白球初始数量: # 无白球可放
                raise 无白球可放
            else:
                self.白球数量 += 1
                self.黑球数量 -= 1
                return "黑球"

        else: # 抽到白球了
            self.白球数量 -= 1
            return "白球"

    def 能抽玩(self):
        while True:
            try:
                self.抽一个球()
            except 球已抽玩:
                return True
            except 无白球可放:
                return False


def 计算概率(黑球初始数量, 白球初始数量, 测试次数):
    抽玩次数 = 0
    for i in range(测试次数):
        一个袋子 = 球袋子(黑球初始数量, 白球初始数量)
        if 一个袋子.能抽玩():
            抽玩次数 += 1
    return 抽玩次数 / 测试次数


if __name__ == "__main__":
    黑球初始数量 = int(input("输入黑球初始数量: "))
    白球初始数量 = int(input("输入白球初始数量: "))
    测试次数 = int(input("输入测试次数: "))
    概率 = 计算概率(黑球初始数量, 白球初始数量, 测试次数)
    print("概率为: {:0.2f}%".format(概率*100))


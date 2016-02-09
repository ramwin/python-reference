# -*- coding:utf-8 -*-
def power(y,d,n):
    if d>=2:
        x = power(y,d/2,n)
        if d%2:
            return (x*x*y)%n
        else:
            return (x*x)%n
    else:
        return y%n
    return (y**d)%n
def main():
    p = 421542432643
    g = 542432643
    a = 248123464587
    b = 192458139446
    gb = 248183040540
    ga = power(g,a,p)
    print("ga={0}".format(ga))
    gb = power(g,b,p)
    print("gb={0}".format(gb))
    gab = power(gb,a,p)
    print("gab={0}".format(gab))
    print("加密前的字段是:")
    print(gab^27117)
main()

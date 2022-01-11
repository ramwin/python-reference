"""
测试调用脚本的时候输入输出
"""

import subprocess
from subprocess import TimeoutExpired

# with subprocess.Popen(["sh", "input.sh"]) as proc:
proc = subprocess.Popen(
    ["sh", "input.sh"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

if True:
    try:
        for i in ["1\n2\nexit\n"]:
            print(f"输入: {i}")
            outs, errs = proc.communicate(input=i.encode('utf8'), timeout=1)
            print("输入完毕, 结果如下: ")
            print(outs.decode('utf8'))
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 点击链接查看和 Kimi 的对话 https://www.kimi.com/share/d2t8uken3mk2nivem95g


import os
import io
import pandas as pd
import multiprocessing as mp
import time

CSV_FILE = 'ordered_output.csv'
N_WORKERS = 4
ROWS_PER_WORKER = 10

# ---------- 子进程 ----------
def worker(idx, recv_token, send_done):
    # 计算 DataFrame
    print("处理", idx)
    time.sleep(1 - idx / 10)
    df = pd.DataFrame({
        'id': range(idx * ROWS_PER_WORKER, (idx + 1) * ROWS_PER_WORKER),
        'worker': [f'worker_{idx}'] * ROWS_PER_WORKER
    })
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    csv_chunk = buffer.getvalue()

    # 等待主进程令牌
    print("等待", idx)
    recv_token.recv()

    print("继续写", idx)

    # 追加写
    with open(CSV_FILE, 'a', encoding='utf-8') as f:
        if idx == 0:           # 首进程写表头
            f.write(csv_chunk)
        else:
            f.write(csv_chunk.split('\n', 1)[1])

    # 通知主进程“我写完”
    send_done.send(None)


# ---------- 主进程 ----------
def main():
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)

    # 为每个 worker 建两根单向 Pipe：
    #   token_pipe:  主 → 子   (子 recv，主 send)
    #   done_pipe :  子 → 主   (子 send，主 recv)
    token_pipes = [mp.Pipe(duplex=False) for _ in range(N_WORKERS)]  # (recv, send)
    done_pipes  = [mp.Pipe(duplex=False) for _ in range(N_WORKERS)]  # (recv, send)

    procs = []
    for idx in range(N_WORKERS):
        p = mp.Process(
            target=worker,
            args=(idx,
                  token_pipes[idx][0],  # 子进程 recv 端
                  done_pipes[idx][1]))  # 子进程 send 端
        p.start()
        procs.append(p)

    # 顺序触发
    for idx in range(N_WORKERS):
        token_pipes[idx][1].send(None)   # 主进程拿 send 端
        done_pipes[idx][0].recv()        # 主进程拿 recv 端

    for p in procs:
        p.join()

    print('>>> 顺序写入完成，文件：', os.path.abspath(CSV_FILE))


if __name__ == '__main__':
    main()

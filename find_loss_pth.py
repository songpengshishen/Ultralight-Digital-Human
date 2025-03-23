## 找一个loss最低的pth模型
import glob
import os
import torch

best_loss = float('inf')

with open('E:\pyProject/loss.txt','r',encoding='utf-8') as f :
    f.seek(0)
    for line in f:
        print(f'当前行的数据 : {line}')
        line_temp = line.strip()
        if not line_temp:
            continue
        parts = line.split()

        value = float(parts[1])
        if value < best_loss:
            best_loss = value

print(best_loss)
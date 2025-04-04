import pandas as pd
import os
from tqdm.auto import tqdm
import sys

# 定义要合并的文件夹路径
folder_path = sys.argv[1]

# 获取文件夹下的所有csv文件名
file_list = os.listdir(folder_path)[:]

# 读取第一个csv文件并包含表头
df = pd.read_csv(os.path.join(folder_path, file_list[0]), header=0)

# 循环遍历列表中各个csv文件名，并追加到合并后的文件
for i in tqdm(range(1, len(file_list)), total=len(file_list) - 1):
    # 以第一列为key进行合并
    try:
        df = df.merge(
            pd.read_csv(os.path.join(folder_path, file_list[i]), header=0),
            how="outer",
            on="Feature",
            suffixes=("", file_list[i]),
        )
    except:
        print(os.path.join(folder_path, file_list[i]))
        continue
df.to_csv("./merged2.csv", index=False, encoding="utf-8-sig")

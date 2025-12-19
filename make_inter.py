# .inter 파일 만들기

import pandas as pd
import os

src = "data/train/train_ratings.csv"
inter_dir = "dataset/my_dataset"
inter_file = f"{inter_dir}/my_dataset.inter"

os.makedirs(inter_dir, exist_ok=True)

df = pd.read_csv(src)

df = df.rename(columns={
    "user": "user_id",
    "item": "item_id",
    "time": "timestamp"
})

df = df[["user_id", "item_id", "timestamp"]]

df = df.sort_values(["user_id", "timestamp"])    # 이게 있어야 sequential 모델에서 적용 간으

with open(inter_file, "w") as f:
    f.write("user_id:token\titem_id:token\ttimestamp:float\n")
    df.to_csv(f, sep="\t", index=False, header=False)

print(f"saved to {inter_file}")

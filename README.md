=================
     Usage
=================

Project Structure
-----------------
```
Project/
├── data/
│   └── train/
│       └── train_ratings.csv   # 원본 데이터
├── dataset/
│   └── my_dataset/
│       └── my_dataset.inter    # 생성된 파일
├── make_inter.py               # 1번 스크립트
├── train_recbole.py            # 2번 스크립트 (argparse 포함된 것)
├── ease_config.yaml            # EASE 모델용 설정 파일
├── multivae_config.yaml
└── lightgcn_config.yaml
```

### 1. Install RecBole
pip install recbole==1.2.1

### 2. make inter file
python make_inter.py

### 3. train the model
python train_recbole.py --model EASE

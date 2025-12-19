=================
     사 용 법
=================

### DIR 구조
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

### 1. RecBole 깔기
pip install recbole==1.2.1

### 2. inter 파일 만들기
python make_inter.py

### 3. 모델 돌리기
python train_recbole.py --model EASE
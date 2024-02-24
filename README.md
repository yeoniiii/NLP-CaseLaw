# NLP-CaseLaw
판례 NLP 분석 | 유사 판례 추천 시스템

```
├── 1_Data
│   ├── 1.1_crawling_국가법령정보센터.ipynb
│   ├── case_fraud.csv
│   ├── case_fraud_prep.csv
│   └── case_list.csv
│ 
├── 2_Preprocessing
│   ├── 2.1_EDA.ipynb
│   ├── 2.2_word_prep.ipynb
│   ├── 2.2.1_판례내용_토큰화.ipynb
│   ├── 2.2.2_판례내용_품사태깅.ipynb
│   └── vocab_list
│       ├── kkma.txt
│       ├── komoran.txt
│       └── stopwords.txt
│ 
├── 3_Modeling
│   ├── 3.1_FastText.ipynb
│   └── model
│       ├── fasttext.model
│       ├── fasttext.model.wv.vectors_ngrams.npy
│       └── fasttext_emb.pickle
│ 
└── README.md
```

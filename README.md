# NLP-CaseLaw
👩🏻‍⚖️ 판례 NLP 분석 | 유사 판례 추천 시스템

- FastText
- SBERT

```
├── 1_Data
│   ├── 1.1_crawling_국가법령정보센터.ipynb
│   ├── case_fraud.csv
│   ├── case_fraud_prep.csv
│   ├── case_fraud_sent.csv
│   └── case_list.csv
│ 
├── 2_Preprocessing
│   ├── 2.1_EDA.ipynb
│   ├── 2.2_word_prep.ipynb
│   ├── 2.3_input_prep.py
│   └── vocab_list
│       ├── kkma.txt
│       ├── kkmaCorpus.pkl
│       ├── komoran.txt
│       └── stopwords.txt
│
├── 3_Modeling
│   ├── 3.1.1_FastText.ipynb
│   ├── 3.1.2_FastText_output.ipynb
│   ├── 3.2.1_SBERT.ipynb
│   ├── 3.2.2_SBERT_output.ipynb
│   └── model
│       ├── fasttext.model
│       ├── fasttext.model.wv.vectors_ngrams.npy
│       ├── fasttext_emb.pickle
│       └── sbert_emb.pickle
│ 
├── 4_TopicModeling
│   ├── 4.1_LSA.ipynb
│   ├── 4.2_LDA.ipynb
│   └── LDA_image.html
│ 
└── README.md
```

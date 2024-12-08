import pandas as pd
import numpy as np
import spacy
import torch

src_vocab_size = 5000
tgt_vocab_size = 5000
max_seq_length = 100
src_data = torch.randint(1, src_vocab_size, (64, max_seq_length))  # (batch_size, seq_length)
tgt_data = torch.randint(1, tgt_vocab_size, (64, max_seq_length))  # (batch_size, seq_length)

text1 = "我喜欢苹果"
# spacy.cli.download("zh_core_web_sm")
nlp = spacy.load("zh_core_web_md")
# nlp = spacy.load('en_core_web_sm')

word_vectors = dict()
print(len(nlp.vocab))
for i in range(len(nlp.vocab)):
    token = nlp.vocab[i].text
    print(token)
    
for key, vector in nlp.vocab.vectors.items():
    try:
        word_string = nlp.vocab.strings[key]
        word_vectors[word_string] = vector

    except KeyError:
        continue

doc = nlp(text1)

print(doc.tensor.shape)

emb_dim = 10
dics = {}
for token in doc:
    dics[token.text] = token.vector[:emb_dim]
print(dics.to_list())
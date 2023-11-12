import json
import torch
from sqlnet.utils import *
import numpy as np
import datetime

LOCAL_TEST=False


if LOCAL_TEST:
    N_word=100
    B_word=6
    USE_SMALL=True
else:
    N_word=300
    B_word=42
    USE_SMALL=False

sql_data, table_data, val_sql_data, val_table_data,test_sql_data, test_table_data, TRAIN_DB, DEV_DB, TEST_DB = load_dataset(0, use_small=USE_SMALL)
print("extract_vocab.py: load_dataset done")
word_emb = load_word_emb('glove/glove.%dB.%dd.txt'%(B_word,N_word), use_small=USE_SMALL)
print("extract_vocab.py: load_word_emb done")
print(f"Length of word vocabulary: {len(word_emb)}")

word_to_idx = {'<UNK>':0, '<BEG>':1, '<END>':2}
word_num = 3
embs = [np.zeros(N_word,dtype=np.float32) for _ in range(word_num)]

def check_and_add(tok):
    #Check if the tok is in the vocab. If not, add it.
    global word_num
    if tok not in word_to_idx and tok in word_emb:
        word_to_idx[tok] = word_num
        word_num += 1
        embs.append(word_emb[tok])

for sql in sql_data:
    for tok in sql['question_tok']:
        check_and_add(tok)
for tab in table_data.values():
    for col in tab['header_tok']:
        for tok in col:
            check_and_add(tok)
for sql in val_sql_data:
    for tok in sql['question_tok']:
        check_and_add(tok)
for tab in val_table_data.values():
    for col in tab['header_tok']:
        for tok in col:
            check_and_add(tok)
for sql in test_sql_data:
    for tok in sql['question_tok']:
        check_and_add(tok)
for tab in test_table_data.values():
    for col in tab['header_tok']:
        for tok in col:
            check_and_add(tok)

print(f"Length of used word vocab: {len(word_to_idx)}")

embs_np = np.array(embs)
emb_array = np.stack(embs_np, axis=0)

with open('/content/drive/MyDrive/258/SQLNet/glove/word2idx.json', 'w') as outf:
    json.dump(word_to_idx, outf)
np.save('/content/drive/MyDrive/258/SQLNet/glove/usedwordemb.npy', emb_array)


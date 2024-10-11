#!/usr/bin/env python3

import pickle
import sys

import numpy as np

import b

_, strategy, th1, th2, output_file, *_ = sys.argv

dig = b._dig(b.all_contracts, strategy, float(th1), float(th2))

# output_dir = 'tmp/'
# import os
# os.makedirs(output_dir, exist_ok=True)

paths = {}
for tid in b.all_contracts:
    print(tid, flush=True)
    path = dig(tid)
    # np.save(f'{output_dir}/{tid}.npy', path)
    paths[tid] = path

for tid1 in list(paths.keys()):
    if tid1 not in paths:
        continue
    path = paths[tid1]
    for tid2 in path[1:]:
        if tid2 in paths:
            del paths[tid2]

with open(output_file, 'wb') as f:
    pickle.dump(paths, f)

lens = []
for tid, path in paths.items():
    lens += [len(path)]
for l in range(min(lens), max(lens) + 1):
    print(f'{l},{lens.count(l)}', flush=True)

"""
All functions for analysis and processing of dataset
"""

import time as t
import os

with open('data/inData/Train-GCC-training.tsv') as imgFile:
    for line in imgFile:
        print(line, end=f'{"-"*80}\n\n\n')
        t.sleep(1)

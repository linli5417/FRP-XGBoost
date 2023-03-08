#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time : 2023.03.08
# @Author : Linli
# @Email : 13896665417@163.com
# @IDE : PyCharm
# @File : main.py

import re
from collections import Counter

def get_AAC(seqs):
	AA = 'ACDEFGHIKLMNPQRSTVWY'
	encodings = []
	for i in seqs:
		sequence = re.sub('-', '', i)
		count = Counter(sequence)
		for key in count:
			count[key] = count[key]/len(sequence)
		code = []
		for aa in AA:
			code.append(count[aa])
		encodings.append(code)
	return encodings

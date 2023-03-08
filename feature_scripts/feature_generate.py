#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time : 2023.03.08
# @Author : Linli
# @Email : 13896665417@163.com
# @IDE : PyCharm
# @File : main.py

from feature_scripts.AAC import get_AAC
from feature_scripts.CKSAAP import get_CKSAAP
from feature_scripts.DDE import get_DDE
from feature_scripts.GTPC import get_GTPC
import pandas as pd
import numpy as np
def select_features(allfeatures,feature_index):
    new_features = []
    orignal_data = pd.DataFrame(allfeatures)
    for i in list(feature_index):
        new_features.append(orignal_data[int(i)])
    features = np.array(new_features).T
    return features

def get_feature(fastas):
    encoding = []
    feature_index = pd.read_csv(r"feature_index.csv", header=None)

    AAC_features = get_AAC(fastas)
    CKSAAP_features = get_CKSAAP(fastas)
    DDE_features =get_DDE(fastas)
    GTPC_features = get_GTPC(fastas)
    encoding.append(AAC_features)
    encoding.append(CKSAAP_features)
    encoding.append(DDE_features)
    encoding.append(GTPC_features)

    encoding = np.column_stack(encoding)
    new_encoding = select_features(encoding, feature_index.iloc[0, :].values)
    return new_encoding






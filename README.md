# FRP

# 1 Description

Ferroptosis is an emerging form of programmed cell death, characterized by the accumulation of iron and lipid reactive oxygen species (ROS) during the cell death process. Disease progression can be alleviated by intervening the ferroptosis pathway, which sheds new light on treatment strategies for many diseases. Comprehending the ferroptosis-related proteins is paramount in the exploration of the mechanisms and roles of this biological process. Precise detection of ferroptosis-related proteins through wet-experimental methods is still a challenging task due to the limitations of current techniques. Here, we presented a XGBoost and multi-view features-based machine learning prediction method for predicting ferroptosis-related proteins, which was referred to as __FRP-XGBoost__.  The __FRP-XGBoost__ achieved an accuracy of 96.52% in 10-fold cross-validation and a further accuracy of 90.87% in an independent test. It is a promising method for the large-scale prediction of unannotated ferroptosis-related proteins and further biological analyses. This tool has significant potential for advancing the field of ferroptosis research, as well as facilitating the development of new therapeutic strategies for diseases associated with ferroptosis.

# 2 Requirements

Before running, please make sure the following packages are installed in Python environment:

python==3.8

numpy==1.24.2

pandas==1.5.3

joblib==1.2.0

scikit-learn==1.2.1

scipy==1.10.1

xgboost==1.7.4


# 3 Running

Changing working dir to FRP-XGBoost-main, and then running the following command:

python FRP-main.py -i test.fasta -o prediction_results.csv

-i: input file in fasta format

-o: output file name

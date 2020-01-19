from sklearn.metrics import precision_recall_fscore_support as score
import nltk.metrics
import pandas as pd
import numpy as np
df = pd.read_csv(r'./data/Results/GoldTestprediction.csv')
#print(df)
predicted = np.array((df.iloc[:,1]))
y_test = np.array((df.iloc[:,2]))   

precision, recall, fscore, support = score(y_test, predicted)
 
print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))
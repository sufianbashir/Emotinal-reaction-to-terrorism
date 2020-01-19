#!/usr/bin/env python
# coding: utf-8

# In[48]:


from sklearn.metrics import precision_recall_fscore_support as score
import nltk.metrics
import pandas as pd
import numpy as np

# df = pd.read_csv('predi1.csv')
# #print(df)
# predicted = np.array((df.iloc[:,1]))
# y_test = np.array((df.iloc[:,2]))   

# precision, recall, fscore, support = score(y_test, predicted)
 
# print('precision: {}'.format(precision))
# print('recall: {}'.format(recall))
# print('fscore: {}'.format(fscore))
# print('support: {}'.format(support))

# #print(np.array((df.iloc[:,1])))  
# #print(np.array((df.iloc[:,2])))  


# # In[106]:


from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import pandas
from collections import Counter

from collections import OrderedDict

# data set 1 for Las vegas 

df = pd.read_csv(r'./data/Results/LasVegasprediction.csv')
#print(df)
predicted = np.array((df.iloc[:,1]))
predicted = Counter(predicted)

#print(predicted.keys(),predicted.values())
del predicted[3.0]  # Deleting none values because we dont want to show in graph 
#print(predicted.keys(),predicted.values())

# Calculate percentage 
total = np.sum( np.array(list(predicted.values())))
predicted = OrderedDict(sorted(predicted.items()))
perecentage_arr = []
for value in predicted.values():
    perc = value*100.0/total
    perecentage_arr.append(perc)
print(perecentage_arr)
x = [0,2,4,6,8]



# data set 2 for orelando 
df1 = pd.read_csv(r'./data/Results/Orelandoprediction.csv')
#print(df)
predicted1 = np.array((df1.iloc[:,1]))
predicted1 = Counter(predicted1)

del predicted1[3.0] # Deleting None index from dictionary 
# Calculate percentage 
total1 = np.sum( np.array(list(predicted1.values())))
predicted1 = OrderedDict(sorted(predicted1.items()))

perecentage_arr1 = []
for value in predicted1.values():
    perc1 = value*100.0/total1
    perecentage_arr1.append(perc1)
print(perecentage_arr1)
x2 = [0.8,2.8,4.8,6.8,8.8]

# 2 end 
 
fig, ax = plt.subplots()
plt.bar(x,  perecentage_arr,label='#LasVegasShooting')
plt.bar(x2,  perecentage_arr1,label='#OrlandoShooting')
plt.xticks(x, ('Anger', 'Disgust', 'Fear','Sadness','Surprise'))
# plt.xticks(x2, ('Anger', 'Disgust', 'Fear','Sadness','Surprise'))
 

plt.title('Emotion- #LasVegasShooting X #OrlandoShooting')
# plt.xlabel('Emotions')
plt.ylabel('Tweets Prediction (%)')
plt.rcParams['font.size'] = 9.
plt.rcParams['font.family'] = 'Comic Sans MS'
plt.legend(loc='best')
plt.show()


# In[ ]:





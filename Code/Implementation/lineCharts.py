import matplotlib as mpl
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
from collections import OrderedDict


# data set 1 for  
df_1 = pd.read_csv(r'./data/Results/Orelandoprediction.csv')
#print(df)
predicted1 = np.array((df_1.iloc[:,1]))
predicted1 = Counter(predicted1)

del predicted1[3.0] # Deleting None index from dictionary 
# Calculate percentage 
total1 = np.sum( np.array(list(predicted1.values())))
predicted1= OrderedDict(sorted(predicted1.items()))

print('predicted values',   predicted1)
perecentage_arr1 = []
print('total is ',total1)
for value in predicted1.values():
    perc1 = (value*100)/total1
    perecentage_arr1.append(perc1)
print(perecentage_arr1)
x = [1,2,3]

# 2 end 

# data set 1 for Las vegas 

df_2 = pd.read_csv('./data/Results/1415OrelandoCleanedPredicitons.csv')
#print(df)
predicted2 = np.array((df_2.iloc[:,1]))
predicted2 = Counter(predicted2)

#print(predicted.keys(),predicted.values())
del predicted2[3.0]  # Deleting none values because we dont want to show in graph 
#print(predicted.keys(),predicted.values())

# Calculate percentage 
total2 =  np.sum( np.array(list(predicted2.values())))
predicted2= OrderedDict(sorted(predicted2.items()))

perecentage_arr2 = []
for value in predicted2.values():
    perc2 = value*100.0/total2
    perecentage_arr2.append(perc2)
print(perecentage_arr2)

# 1 end 
# data set 2 for  
df_3 = pd.read_csv('./data/Results/1617OrelandoCleanedPrediction.csv')
#print(df)
predicted3 = np.array((df_3.iloc[:,1]))
predicted3 = Counter(predicted3)

del predicted3[3.0] # Deleting None index from dictionary 
# Calculate percentage 
total3 = np.sum( np.array(list(predicted3.values())))
predicted3= OrderedDict(sorted(predicted3.items()))

perecentage_arr3 = []
for value in predicted3.values():
    perc3 = value*100.0/total3
    perecentage_arr3.append(perc3)
print(perecentage_arr3)
 

# 2 end 

#Make matrix to draw 5 lines 1 for each emotion 

matrix = np.column_stack(( perecentage_arr1,perecentage_arr2,perecentage_arr3))
print(matrix)
a1 = matrix[0]
a2 = matrix[1]
a3 = matrix[2]
a4 = matrix[3]
a5 = matrix[4]

 

plt.rcParams['font.size'] = 9.
plt.rcParams['font.family'] = 'Comic Sans MS'
plt.xticks(x, ('June 12-13,2016', 'June 14-15, 2016', 'June 16-17, 2016'))
# plt.xticks(x1, (x, ('2-3', '3-4', '5-6'))
 
plt.plot(x,a1, marker='o', linestyle='-', color='y',label='anger')
plt.plot(x,a2, marker='o', linestyle='-', color='g', label='disgust')
plt.plot(x,a3, marker='o', linestyle='-', color='r', label='fear')
plt.plot(x,a4, marker='o', linestyle='-', color='b',label='sadness')
plt.plot(x,a5, marker='o', linestyle='-', color='c', label='surprise')


plt.xlabel('Time Period')
plt.ylabel('Tweets Prediction (%)')
plt.title('#OrlandoShooting ')
plt.legend(loc='best')
plt.show()
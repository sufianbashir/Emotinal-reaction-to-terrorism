#Randomize data lines 
import random
import os
data = open(os.path.abspath('data/Training/OrelandoSplit/surpriseText.csv')).readlines()
percentageSample = 30 # 30 %
size = len(data)
cut = int((percentageSample * size)/100) # % of the list
print(size,cut)
random.shuffle(data)

# open('LasvegassurpriseShuffled.txt', 'w').writelines(data)
open('data/Training/OrelandoSplit/surpriseTraining.txt', 'w').writelines(data[:cut])

open('data/Training/OrelandoSplit/surpriseTest.txt', 'w').writelines(data[cut:])
#print(random.sample(data,cut))

# print(data[:cut]) # first 80% of shuffled list
print('Finished ',len(data))
# data[cut:] # last 20% of shuffled list

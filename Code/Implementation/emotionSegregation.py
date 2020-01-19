#!/usr/bin/env python
# coding: utf-8

# In[27]:
 

import csv
anger_keywords=['anger','fuck','fucked',"fucking",'fucker','piss','pissed','lmaof','damn',"angry","shit","bastard",'hate',"cruel",'savage',"sick","sickening","worst",'dog','bitch','sucks']
disgust_keywords=['disgust','disgusted','disgusting',"disgustingly","disgraceful","pathetic","senseless"]
fear_keywords=['worried','worry','scary','scaring','scared','fear','terrifying',"terrified",'terror',"terrible","scarier","scariest","threat","horrific",'horrifying',"afraid","frightening","frightened",'horror']
sadness_keywords=['sad','sadness','saddened','saddest','sorrow','sorrowful',"disturbing",'distressed',"broke","break","heartbroken","heartbreaking","hurt","hurting","shattered","cry","crying","upset","tears","pain","painful",'tragic']
surprise_keywords=['surprise','surprised','surprising','shocking','shocked',"speechless","devastating",'devastated',"shock","shook"]
except_keywords = ['trust','trusted','joy','anticipate','anticipated','anticipation','anticipating']
with open('data/Training/afterLasVegasTextCleaned.csv') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        sentences = [x.strip() for x in content] 
        # sentences = [''.join( [ word.lower() for word in x ] ).strip() for x in content] 
        
for sentence in sentences:
    #anger_keywords
    ""
    if (any(map(lambda word: word in sentence, anger_keywords))):
        print(sentence)
        with open(r'data/Training/LasvegasSplit/angerText.csv', 'a') as csvfile:
            fieldnames = ['text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"text": sentence})

    #disgust_keywords
    
    
    elif(any(map(lambda word: word in sentence, disgust_keywords))):
        print('second dic match : ',sentence)
        with open(r'data/Training/LasvegasSplit/disgustText.csv', 'a') as csvfile:
            fieldnames = ['text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"text": sentence})
    #fear_keywords
    
    elif(any(map(lambda word: word in sentence, fear_keywords))):
        print('second dic match : ',sentence)
        with open(r'data/Training/LasvegasSplit/fearText.csv', 'a') as csvfile:
            fieldnames = ['text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"text": sentence})
            
    #sadness_keywords
    
    elif(any(map(lambda word: word in sentence, sadness_keywords))):
        print('second dic match : ',sentence)
        with open(r'data/Training/LasvegasSplit/sadnessText.csv', 'a') as csvfile:
            fieldnames = ['text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"text": sentence})
            
            
    #surprise_keywords
    
    
    elif(any(map(lambda word: word in sentence, surprise_keywords))):
        print('second dic match : ',sentence)
        with open(r'data/Training/LasvegasSplit/surpriseText.csv', 'a') as csvfile:
            fieldnames = ['text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"text": sentence})
    else:
        if (not any(map(lambda word:word  in sentence, except_keywords))):
            print('Nothing')
            with open(r'data/Training/LasvegasSplit/noneText.csv', 'a') as csvfile:
                fieldnames = ['text']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({"text": sentence})
print('Finished Processing')
    


# In[5]:


# anger_keywords=['anger','fuck','fucked','pissed','lmaof','damm']
# sentence = 'hi lmaof boy'
# if (not any(map(lambda word:word  in sentence, anger_keywords))):
#     print('Hi')
# else:
#     print('Hello')


# In[44]:








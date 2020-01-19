# -*- coding: utf-8 -*-
import preprocessor as p
import nltk
import sys
import csv,re
import os
import nltk.data
from nltk.stem.porter import *
from spellchecker import SpellChecker
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')


       
def removeStopWords(sentence):
    from nltk.corpus import stopwords
    stop = stopwords.words("english")
    sentenceAfterStopWords = ' '.join([word for word in sentence.split() if word not in (stop)])
    # print('after stop words ',sentenceAfterStopWords)
    return sentenceAfterStopWords

# Code From: https://medium.com/nerd-stuff/python-script-to-turn-text-message-abbreviations-into-actual-phrases-d5db6f489222
def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:
        # File path which consists of Abbreviations.
        fileName = "slang.txt"

        # File Access mode [Read Mode]
        with open(fileName, "r") as myCSVfile:
            # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
            dataFromFile = csv.reader(myCSVfile, delimiter="=")
            # Removing Special Characters.
            _str = re.sub('[^a-zA-Z0-9]+', '', _str)
            for row in dataFromFile:
                # Check if selected word matches short forms[LHS] in text file.
                if _str.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    return ' '.join(user_string)
def stemming(sentence):
    ps = PorterStemmer()
    return ' '.join([ps.stem(word) for word in sentence.split() ])

def lemmatization(sentence):
    from nltk.stem.wordnet import WordNetLemmatizer
    lmtzr = WordNetLemmatizer() 
    return ' '.join([lmtzr.lemmatize(word,'v') for word in sentence.split() ])

def Tokenization(sentence):
    return nltk.word_tokenize(sentence)



def toLowerCase(sentence):
    # print('sentence',sentence)
    return  sentence.lower()

def spellCheck(string_to_be_checked):
    # create an object
    spell = SpellChecker()
    # spell.word_frequency.load_text_file('wordsDictionary.txt')
    misspelled = spell.unknown(string_to_be_checked.split(" "))
    spell.word_frequency.load_words(['fuck','fucked','damm','lmaof', 'pissed', 'google'])
    spell.known(['fuck','fucked','damm','lmaof', 'pissed'])  # will return both now!
    # print(string_to_be_checked)
    # print(misspelled)
    for word in misspelled:
        # Get the one `most likely` answer
        correctedWord=''
        if(word!=''):
            correctedWord = spell.correction(word)
        
        
        # Get a list of `likely` options
        # print(word,correctedWord)
        if(correctedWord==None or correctedWord ==''):
            continue
        string_to_be_checked =   string_to_be_checked.replace(word,correctedWord,1)
        # print(correctedWord)
    # print(string_to_be_checked)
    return string_to_be_checked
# def changeContractions():
#     for word in text.split():
#     if word.lower() in contractions:
#         text = text.replace(word, contractions[word.lower()])
def main():
    # import tensorflow as tf
    # import nltk
    # nltk.download('stopwords')
    # nltk.download('wordnet')
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    with open(r'0506 LasVegas.csv') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        # content = [x.strip() for x in content] 
    
    for line in content:
        # print(linke.split(',')[1])

  
        p.set_options(p.OPT.URL, p.OPT.EMOJI,	p.OPT.MENTION,	p.OPT.HASHTAG)
        cleanedTweet = p.clean(line.split(',')[0])
        #remove special characters 
        wordsOnly =  re.sub(r"[^A-Za-z0-9 ']", ' ', cleanedTweet)
        spellcheck = spellCheck(wordsOnly)

        # print(cleanedTweet)
         # step 1 stop word removal
        # sentenceAfterStopWords = removeStopWords(cleanedTweet)

        # step 2 spell correction and replace abbreviations
        # print( 'correction : ',translator(sentenceAfterStopWords) )
        trans = translator(spellcheck)
        # print(trans)
        # step 3 stemming 
        # stem = stemming(trans)
        # print('stemming : ',stemming(trans))
        # step 4 Lemmazation
        # lem = lemmatization(trans)
        # print('LEMMAZATION : ',lem)
        # step 5 Tokenization
        # tok = Tokenization(sentenceAfterStopWords)
        # print('tokenization : ',tok)
        # step 6 Capitalization
        cap = toLowerCase(trans).strip()
        # print('Captilization : ',cap)
        if(trans):

            with open(r'0506LasvegasCleaned.csv', 'a') as csvfile:
                fieldnames = ['text']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({"text":cap })
    print('operation ended ')


if __name__ == '__main__':

    main()

import numpy as np
import re


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(AngerTrainingFile,DisgustTrainingFile,FearTrainingFile,NoneTrainingFile,SadnessTrainingFile, SurpriseTrainingFile):
    """
    Loads tweets emotion's data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
#1
    sadness_examples = list(open(SadnessTrainingFile, "r", encoding='utf-8').readlines())
    sadness_examples = [s.strip() for s in sadness_examples]

#2
    surprise_examples = list(open(SurpriseTrainingFile, "r", encoding='utf-8').readlines())
    surprise_examples = [s.strip() for s in surprise_examples]
#3
    none_examples = list(open(NoneTrainingFile, "r", encoding='utf-8').readlines())
    none_examples = [s.strip() for s in none_examples]
#4
    fear_examples = list(open(FearTrainingFile, "r", encoding='utf-8').readlines())
    fear_examples = [s.strip() for s in fear_examples]
#5
    anger_examples = list(open(AngerTrainingFile, "r", encoding='utf-8').readlines())
    anger_examples = [s.strip() for s in anger_examples]
#6   
    disgust_examples = list(open(DisgustTrainingFile, "r", encoding='utf-8').readlines())
    disgust_examples = [s.strip() for s in disgust_examples]

    # Split by words
    x_text = sadness_examples + surprise_examples + none_examples + fear_examples + anger_examples + disgust_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    # As labelled in gold standard we are using following labels corresponding to each emotion category
    # Anger - 0
    # Disgust - 1
    # Fear - 2
    # None - 3 
    # Sadness - 4
    # Surprise - 5

    anger_labels = [[1,0,0,0,0,0] for _ in anger_examples]
    disgust_labels = [[0,1,0,0,0,0] for _ in disgust_examples]
    fear_labels = [[0,0,1,0,0,0] for _ in fear_examples]
    none_labels = [[0,0,0,1,0,0] for _ in none_examples]
    sadness_labels = [[0,0,0,0,1,0] for _ in surprise_examples]
    surprise_labels = [[0,0,0,0,0,1] for _ in sadness_examples]

    
    y = np.concatenate([anger_labels,disgust_labels,fear_labels,none_labels,sadness_labels,surprise_labels], 0)
    print('Anger Labels ',y.shape)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]


######## Helpers ###############

def load_data_labels(datasets):
    """
    Load data and labels
    :param datasets:
    :return:
    """
    # Split by words
    x_text = datasets['data']
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    labels = []
    for i in range(len(x_text)):
        label = [0 for j in datasets['target_names']]
        label[datasets['target'][i]] = 1
        labels.append(label)
    y = np.array(labels)
    return [x_text, y]

def load_embedding_vectors_glove(vocabulary, filename, vector_size):
    # load embedding_vectors from the glove
    # initial matrix with random uniform
    embedding_vectors = np.random.uniform(-0.25, 0.25, (len(vocabulary), vector_size))
    f = open(filename)
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype="float32")
        idx = vocabulary.get(word)
        if idx != 0:
            embedding_vectors[idx] = vector
    f.close()
    return embedding_vectors

def get_datasets_emotiontweets(AngerTrainingFile,DisgustTrainingFile,FearTrainingFile,NoneTrainingFile,SadnessTrainingFile, SurpriseTrainingFile):
    """
    Loads emotions data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
      # Load data from files
#1
    anger_examples = list(open(AngerTrainingFile, "r", encoding='utf-8').readlines())
    anger_examples = [s.strip() for s in anger_examples]


#2
    disgust_examples = list(open(DisgustTrainingFile, "r", encoding='utf-8').readlines())
    disgust_examples = [s.strip() for s in disgust_examples]
#3
    fear_examples = list(open(FearTrainingFile, "r", encoding='utf-8').readlines())
    fear_examples = [s.strip() for s in fear_examples]

#4
    none_examples = list(open(NoneTrainingFile, "r", encoding='utf-8').readlines())
    none_examples = [s.strip() for s in none_examples]

#5
    sadness_examples = list(open(SadnessTrainingFile, "r", encoding='utf-8').readlines())
    sadness_examples = [s.strip() for s in sadness_examples]
#6   
    surprise_examples = list(open(SurpriseTrainingFile, "r", encoding='utf-8').readlines())
    surprise_examples = [s.strip() for s in surprise_examples]

    # Split by words
    
    datasets = dict()
    datasets['data'] = anger_examples + disgust_examples+ fear_examples + none_examples + sadness_examples + surprise_examples      
    target = [0 for x in anger_examples] + [1 for x in disgust_examples] + [2 for x in fear_examples] + [3 for x in none_examples] + [4 for x in sadness_examples ] + [5 for x in surprise_examples]
    datasets['target'] = target
    datasets['target_names'] = ['anger_examples', 'disgust_examples','fear_examples','none_examples','sadness_examples','surprise_examples']
    return datasets

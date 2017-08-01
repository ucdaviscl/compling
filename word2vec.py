"""
Created on July 31 2017

Short description: Inspect Wikipedia database dump model with word2vec based on the article http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/ 

"""

import os
import gensim
import logging

# Specify data path
os.chdir('/data/khgkim/compling')

# Logging code taken from http://rare-technologies.com/word2vec-tutorial/
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Train model  
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec')  

# Retrieve and write out the entire list of "words" from the model
vocab = model.vocab.keys()

fileNum = 1
wordsInVocab = len(vocab)
wordsPerFile = int(100E3)

# Each file will contain 100,000 entries from the model
for wordIndex in range(0, wordsInVocab, wordsPerFile):
    # Write out the chunk to a numbered text file    
    with open("vocabulary/vocabulary_%.2d.txt" % fileNum, 'w') as f:
        # For each word in the current chunk        
        for i in range(wordIndex, wordIndex + wordsPerFile):
            # Write out and escape any unicode characters            
            f.write(vocab[i].encode('UTF-8') + '\n')
    
    fileNum += 1

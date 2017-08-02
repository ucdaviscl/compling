"""
    Created on July 31 2017

    Inspect Wikipedia database dump model with word2vec and get vocabulary 
    
    Reference: http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/ 
"""

import os, logging, time
import gensim

start_time = time.time()

# Specify data path
data_path = '/data/khgkim/compling'

os.chdir(data_path)

# Logging code taken from http://rare-technologies.com/word2vec-tutorial/
logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

# Train model  
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec')

# Retrieve and write out the entire list of "words" from the model
vocab = model.vocab.keys()

del model

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

# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

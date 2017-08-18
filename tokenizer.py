"""
    Created on July 27 2017
    Wikipedia database dump tokenizer
"""

import os, logging, sys, datetime, time
import glob, io, codecs, re
import nltk
import pickle

from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

# Specify paths
dump_path = '/media/khgkim/data/khgkim/compling/processed/'
token_path = '/media/khgkim/data/khgkim/compling/'
filename = 'tokenizer_tokens.txt'
filename2 = 'tokenizer_tokens2.txt'
filename3 = 'freqDist.pickle'

os.chdir(dump_path)

#counter for line length control
lineCount = 0

if not (os.path.isfile(token_path + filename)):
  print timestamp
  tokensFile = codecs.open(token_path + filename, "a+", "utf-8")
  fDistTotal = FreqDist()
  # For each directory
  for directory in glob.glob("*"):
    print  "directory: " + directory
    # Get all wiki articles
    for files in os.listdir(directory):
      with io.open(directory + '/' + files, encoding='utf-8') as s:
        string = s.read()
        tokens = nltk.word_tokenize(string)
        for word in tokens:
          tokensFile.write(word + " ")
          lineCount += 1
          if lineCount >= 60:
            tokensFile.write('\n')
            lineCount = 0
        fDistTotal = fDistTotal + FreqDist(tokens)
        del tokens
        del string
      s.close()
  tokensFile.close()
  print "Finished tokenizer_tokens.txt in %s minutes ---" % ((time.time() - start_time)/60) 
  # Replace UNK tokens based on frequency and save to tokenizer_tokens2.txt
  f = codecs.open(token_path + filename2, "a+", "utf-8")  
  with codecs.open(token_path + filename, "a+", "utf-8") as t:
    for line in t:
      for word in nltk.word_tokenize(line):
        if (fDistTotal[word] <= 10):
          f.write("UNK" + " ")   
        else: 
          f.write(word + " ")
  f.close()
  f = open(token_path + filename3, "wb")
  pickle.dump(fDistTotal, f)
  f.close()
else:
  print "Output message: File tokenizer_tokens.txt already exists!"
  exit()
# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

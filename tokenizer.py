"""
    Created on July 27 2017

    Wikipedia database dump tokenizer
"""

import os, logging, sys, datetime, time
import glob, codecs, re
import nltk

from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

# Specify paths
dump_path = '/media/khgkim/data/khgkim/compling/test/'
token_path = '/media/khgkim/data/khgkim/compling/'
filename = 'tokenizer_tokens.txt'
filename2 = 'tokenizer_tokens2.txt'

os.chdir(dump_path)

# Initialize list for token frequency 
tok_list = []

if not (os.path.isfile(token_path + filename)):
  print timestamp
  # For each directory
  for directory in glob.glob("*"):
    # Get all wiki articles
    wiki = PlaintextCorpusReader(directory, 'wiki_.*')
    # Tokenize articles
    tok_corp = []
    tok_corp = wiki.words(wiki.fileids())
    # Save tokens to tokenizer_tokens.txt and tok_list
    for word in tok_corp:
      tok_list.append(word)
      f.write(word + " ")
    f.write("\n")
    del tok_corp 
    del wiki
    f.close()
  print "Finished tokenizer_tokens.txt"
  # Replace UNK tokens based on frequency and save to tokenizer_tokens2.txt
  if not (os.path.isfile(token_path + filename2)):
    f = codecs.open(token_path + filename2, "a+", "utf-8")
    fdist = FreqDist(tok_list)
    for word in tok_list:
      if (fdist[word] <= 10):
        f.write("UNK" + " ")   
      else: 
        f.write(word + " ")
    del tok_list
    del fdist
    f.close()
  else:
    print "Output message: File tokenizer_tokens2.txt already exists!"
    exit()
else:
  print "Output message: File tokenizer_tokens.txt already exists!"
  exit()

# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

"""
    Created on August 2 2017
  
    Applying Word2Vec to Wikipedia database dump 
    Reference: http://zhangbanger.github.io/2015/12/13/allen-ai-challenge-part-3.html 
"""

import logging, os, sys, datetime, time, multiprocessing
import gensim

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

logging.basicConfig(
    format = '%(asctime)s : %(levelname)s : %(message)s',
    level = logging.INFO
)

# Specify data path
data_path = '/data/khgkim/compling/dump'
token_path = '/data/khgkim/compling/word2vec_tokens.txt'
analogy_path = '/data/khgkim/compling/questions-words.txt'

os.chdir(data_path)

if not (os.path.isfile(token_path)):
  # Extract and tokenize Wikipedia articles
  wiki_corpus = WikiCorpus('wiki_dump.xml.bz2')
  wiki_lines = wiki_corpus.get_texts()

  # Write wiki_lines out for future use
  lines_output = open(token_path, 'w')
  for text in wiki_lines:
      lines_output.write(" ".join(text) + "\n").encode('utf-8')
  lines_output.close()
else:
  print 'Output message: word2vec_tokens.txt already exists!'
  exit()

model = Word2Vec(
  sentences=LineSentence(wiki_lines),
  size=400,
  negative=5,
  hs=0,
  sample=1e-5,
  window=5,
  min_count=5,
  workers=multiprocessing.cpu_count()
)

model.save("word2vec.model" % timestamp)

# Sanity Check using an analogy file
model.accuracy(open(analogy_path))  

# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

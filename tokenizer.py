"""
Created on July 27 2017

Short description: Wikipedia database dump tokenizer

"""

import os
import glob
import codecs
import re
import nltk

from nltk.corpus import PlaintextCorpusReader

# Specify Wikipedia database dump path
os.chdir("/data/khgkim/wikiextractor/text")

# For each directory
for directory in glob.glob("*"):
  # Get all wiki articles
  wiki = PlaintextCorpusReader(directory, 'wiki_.*')
  # Delete XML tags in the wiki article
  for files in wiki.fileids():
    contents = codecs.open(directory + '/' + files, encoding='utf-8').read()
    contents = re.sub('<[^>]*>', '', contents)
    contents = contents.encode('utf-8')
    # Save changes to the wiki article
    f = open(directory + "/" + files, 'w')
    f.write(contents)
    f.close()
  # Tokenize  
  tok_corp = []
  tok_corp = wiki.words(wiki.fileids())
  # Save tokenized words to results.txt
  f = codecs.open("/data/khgkim/compling/results.txt", "w+", "utf-8")
  for words in tok_corp:
    f.write(words + " ")
  f.close()

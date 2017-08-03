"""
    Created on July 27 2017

    Wikipedia database dump tokenizer
"""

import os, logging, sys, datetime, time
import glob, codecs, re
import nltk

from nltk.corpus import PlaintextCorpusReader

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

# Specify paths
dump_path = '/data/khgkim/wikiextractor/text'
token_path = '/data/khgkim/compling/tokenizer_tokens.txt'

os.chdir(dump_path)

if not (os.path.isfile(token_path)):
  print timestamp
  # For each directory
  for directory in glob.glob("*"):
    # Get all wiki articles
    wiki = PlaintextCorpusReader(directory, 'wiki_.*')
    # Replace Wiki article characters using regular expression
    for files in wiki.fileids():
      contents = codecs.open(directory + '/' + files, encoding='utf-8').read()
      contents = re.sub('<[^>]*>', '', contents) # XML tags
      contents = re.sub('((\d+([^a-zA-Z]\d+)+))|\s\d+\s', '', contents) # Numbers
      contents = contents.encode('utf-8')
      # Save changes to the wiki article
      f = open(directory + "/" + files, 'w')
      f.write(contents)
      f.close()
    # Tokenize articles
    tok_corp = []
    tok_corp = wiki.words(wiki.fileids())
    # Save tokens to tokens.txt
    f = codecs.open(token_path, "a+", "utf-8")
    for words in tok_corp:
      f.write(words + " ")
    f.close()
else:
  print "Output message: File tokenizer_tokens.txt already exists!"
  exit()

# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

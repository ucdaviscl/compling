import glob, os
import codecs
import re
import nltk

from nltk.corpus import PlaintextCorpusReader

os.chdir("/data/khgkim/wikiextractor/text")

# For each directory
for directory in glob.glob("TEST_*"):
  wiki = PlaintextCorpusReader(directory, 'wiki_.*')
  # Delete XML tags in the files
  for files in wiki.fileids():
    contents = codecs.open(directory + '/' + files, encoding='utf-8').read()
    contents = re.sub('<[^>]*>', '', contents)
    contents = contents.encode('utf-8')
    f = open(directory + "/" + files, 'w')
    f.write(contents)
    f.close()
  # Tokenize all the files 
  tok_corp = []
  tok_corp = wiki.words(wiki.fileids())
  # Save to file
  f = codecs.open("/data/khgkim/compling/results.txt", "w+", "utf-8")
  for words in tok_corp:
    f.write(words + " ")
  f.close()

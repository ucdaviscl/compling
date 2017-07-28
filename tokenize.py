import codecs
import re
import nltk

from nltk.corpus import PlaintextCorpusReader

corpus_root = '/data/khgkim/wikiextractor/text/TEST/' # TEST directory for testing
wiki = PlaintextCorpusReader(corpus_root, 'wiki_.*')

tok_corp = []

# Delete XML tags in the files
for files in wiki.fileids():
  contents = codecs.open(corpus_root + files, encoding='utf-8').read()
  contents = re.sub('<[^>]*>', '', contents)
  contents = contents.encode('utf-8')
  f = open(corpus_root + files, 'w')
  f.write(contents)
  f.close()

# Tokenize all the files 
tok_corp = wiki.words(wiki.fileids())

# Save token results to a text file
file = codecs.open("results.txt", "w", "utf-8")

for words in tok_corp:
  file.write(words + " ")
file.close()

"""
    Created on August 15 2017

    Regular expression
"""

import os, logging, sys, datetime, time
import glob, io, re
import nltk

from nltk.corpus import PlaintextCorpusReader

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

print timestamp

logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

# Specify paths
dump_path = '/media/khgkim/data/khgkim/compling/text/'

os.chdir(dump_path)

# For each directory
for directory in glob.glob("*"):
  # Get all wiki articles
  wiki = PlaintextCorpusReader(directory, 'wiki_.*')
  # Replace characters using regular expression
  for files in wiki.fileids():
    s = io.open(directory + '/' + files, encoding='utf-8')
    contents = s.read()
    s.close()
    contents = re.sub('<[^>]*>(.*\r?\n){2}', '', contents) # Beginning XML tag + article title
    contents = re.sub('<[^>]*>', '', contents) # Ending XML tag
    # Find all digit occurences
    for digits in re.findall('((?<=\W)|^)(\d+s*(?!(\-*[a-zA-Z]\-*\s*))(?=\W))', contents):
      temp = re.sub('\d', '9', digits[1]) # Placeholder for matching groups
      contents = re.sub(digits[1], temp, contents, count=1) # Replace
      del temp
    contents = contents.encode('utf-8')
    # Save changes to the wiki article
    f = open(directory + "/" + files, 'w')
    f.write(contents)
    f.close()
    del contents 

# Print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

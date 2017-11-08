<!--![logo](https://user-images.githubusercontent.com/18225387/28990208-f3ef711e-792f-11e7-9cb3-5341736d6db6.png) -->
[Computational Linguistics Lab](http://compling.ucdavis.edu/)
===
[*Department of Linguistics*](http://linguistics.ucdavis.edu/), [*UC Davis*](https://www.ucdavis.edu/)

## Overview
Expanding linguistic resources for speech enabled systems

### tokenizer.py 
Wikipedia database dump tokenizer

1. First download the [Wikipedia database dump](https://dumps.wikimedia.org/)
2. Use [WikiExtractor](https://github.com/attardi/wikiextractor) to extract and clean text from the Wikipedia database dump
 ```
    $ git clone https://github.com/attardi/wikiextractor.git
 ```
3. Install the script by doing

 ```
    $ (sudo) python setup.py install
 ```
4. Apply the script to the Wikipedia database dump

 ```
    $ WikiExtractor.py (your-database-dump).xml.bz2
 ```
5. Specify the database path in the script and run **tokenizer.py**

  ```
    $ python tokenizer.py
 ```
6. After running the script, tokens are stored in **tokenizer_tokens.txt**, unless otherwise specified. The script also outputs **tokenizer_tokens2.txt**, in which infrequent tokens (those appearing <= 10 times) are replaced with an 'UNK' token.

### inspect_words.py
Inspect Wikipedia database dump model with Word2Vec and create vocabulary files

1. Build [fastText](https://github.com/facebookresearch/fastText) using the following commands
 ```
   $ git clone https://github.com/facebookresearch/fastText.git
   $ cd fastText
   $ make
```
2. Learn word vectors for the Wikipedia database dump articles
 ```
   $ ./fasttext skipgram -input results.txt -output model
```
3. Running the command above will save two files: **model.bin** and **model.vec**. **model.vec** is a text file containing the word vectors, one per line. **model.bin** is a binary file containing the parameters of the model along with the dictionary and all hyper parameters. 
4. Download [**questions-words.txt**](https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/word2vec/source-archive.zip). This file contains approximately 19,500 analogies, divided into several categories, that will be used to perform a sanity check of the Wikipedia database dump model. 
5. Running the following command will train the Wikipedia database dump model and store the "words" into the directory **vocabulary**. It will also perform a sanity check of the model using **questions-words.txt** and output the accuracies of the model's predictions for each analogy category, as well as the overall accuracy of the model's predictions.  
```
   $ mkdir vocabulary
   $ python inspect_words.py
```

### word2vec.py
Applying Word2Vec to Wikipedia database dump

1. Uses gensim's Wikipedia parsing (WikiCorpus) to extract and tokenize the Wikipedia database dump compressed in bz2.   
2. Runs gensim's Word2Vec to train model (gensim does not have GPU support). Saved as **word2vec.model**.
3. Performs sanity check with the file specified in **analogy_path** (questions-word.txt) 
 ```
    $ python word2vec.py 
 ```

## Built With
* [Python](https://www.python.org/)
* [fastText](https://github.com/facebookresearch/fastText) and [Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html) - For learning word representations
* [NLTK](http://www.nltk.org/) - Used to tokenize words

## Contributors
* [Richard Kim](https://github.com/khgkim)
* [Lauren Namdar](https://github.com/lnamdar)
* [Samuel Davidson](https://github.com/ssdavidson)

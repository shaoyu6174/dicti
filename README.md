# dicti - dictionary.com crawler powered by scrapy
## Defeat your evil litorature teacher !!

## Features
 - Extract potential vocabulary words from text, excluding the most common words to save space.
 - Produce a file with all the words and meanings in alphabetical order.


## Usage
### Crawl from word list
  0. Install required packages: `pip3 install -r requirements.txt`
  1. Type down a list of words to `input.txt`
  2. Run `./run.py`
  3. Copy text from `output.txt`
### Extract vocab from text
  0. Install required packages: `pip3 install -r requirements.txt`
  1. Download English model for spacy `python3 -m spacy download en`
  2. Copy text from internet to `text.txt`, preferably from a .doc or .txt, avoid pdf files
  3. Run `./extract.py <LEVEL>` to extract vocaubulary words from text, excluding the top <LEVEL> most frequently used words in the English language.
	The default value is 10000, meaning that the 10000 most common words in English will not be included. A higher level saves space, but may omit certain words.
	The maximum possible value is 20000 because that is the length of my frequency list.
  4. Run `./run.py` to generate definitions from the list.

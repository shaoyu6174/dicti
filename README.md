# dicti - dictionary.com crawler powered by scrapy

## Features
 - Extract potential vocabulary words from text, excluding 20000 most common words to save space.
 - Produce a file with all the words and meanings in alphabetical order.


## Usage
### Crawl from word list
  0. Install required packages: `pip install -r requirements.txt`
  1. Type down a list of words to `input.txt`
  2. Run `python run.py`
  3. Copy text from `output.txt`
### Extract vocab from text
  0. Install required packages: `pip install -r requirements.txt`
  1. Copy text from internet to `text.txt`, preferably from a .doc or .txt, avoid pdf files


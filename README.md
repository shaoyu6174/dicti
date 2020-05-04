# dicti - Creat customized dictionary for texts

## Features
 - Extract potential vocabulary words from text, excluding the most common words to save space.
 - Produce a file with all the words and meanings in alphabetical order.
 - Includes a template for printing small font sized cheatsheets.

## Usage
### Crawl from word list
  0. Install required packages: `pip3 install -r requirements.txt`
  1. Type down a list of words to `input.txt`
  2. Run `./run.py`
  3. Copy text from `output.txt`
### Extract vocab from text
  0. Install required packages: `pip3 install -r requirements.txt`
  1. Download English model for spacy `python3 -m spacy download en` (Only needs to be done once)
  2. Copy text from internet to `text.txt`, preferably from a .doc or .txt, avoid pdf files
  3. Run `./extract.py <LEVEL>` to extract vocaubulary words from text, excluding the top <LEVEL> most frequently used words in the English language.
	The default value is 10000, meaning that the 10000 most common words in English will not be included. A higher level saves space, but may omit certain words.
	The maximum possible value is 20000 because that is the length of my frequency list.
  4. (Optional) You can edit the word list file (`input.txt`) to remove unnecessary words to save space.
  4. Run `./run.py` to generate definitions from the list.
### Test different levels
  0. Install required packages: `pip3 install -r requirements.txt`
  1. Download English model for spacy `python3 -m spacy download en` (Only needs to be done once)
  2. Run `./testlevels.py` This tests all levels from 7000 to 20000 and shows at what levels words will be omitted.
  3. Use the level right before any word you don't understand is omitted. For example, if Level 15000 omits a word you do not understand, you should use level 14000. You can do this with `./extract.py 14000`


### Tips and Tricks
 - Font size of 3 points is approximately the smallest size visible on an A4 paper. Sans-serif fonts are recommended. size 4 recommended for ease of viewing. This assumes that you have a laser printer with resolution of at least 300 dpi. Inkjet printers have a lower resolution and may not be legible at such small sizes. 
 - Try copying from text sources such as HTML(webpages) or .doc files. Avoid PDFs because they often cause spacing issues.

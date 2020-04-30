import spacy
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def extract(text_path="text.txt", freq_path="freqlist.txt", level=10000):
    """
    Extract potentially vocabulary words from text file <text_path>
    excluding top <level> words in <freqlist>
    """

    with open(freq_path, "r") as f:
        freqlist = f.read().splitlines()
    with open(text_path, "r") as f:
        text = f.read()
        
    nlp = spacy.load('en')
    doc = nlp(text)

    count = 0
    wordlist = []
    for token in doc:
        if (w:=token.lemma_.lower()) not in wordlist and w not in freqlist[:level]:
            wordlist.append(token.lemma_.lower())

    with open("input.txt", 'w') as f:
        for word in wordlist:
            if word.isalpha():
                f.write(word)
                f.write("\n")
                count+=1

    print(str(count) + " words extracted at level " + str(level))

    return wordlist

def process(input_path="result.json", output_path="output.txt", freq_path="freqlist.txt"):
    """
    Produce a pandas DataFrame from a json file with words and definitions, filtering out words with non-alphabetical characters and words in the top <level> of <freqlist> and output it to a text file. 
    """
    
    with open(freq_path) as f:
        freqlist = f.read().splitlines()
    data = pd.read_json(input_path)
    for index, row in data.iterrows():
        row['defi'] = filter(lambda s : s.lower().islower(), row['defi'])
        row['defi'] = "; ".join(row['defi'])
    data = data.sort_values('word')
    with open(output_path, 'w') as f:
        for index, row in data.iterrows():
            if row['word'].islower() and row['word'] not in freqlist[:10000]:
                f.write("*  ")
                f.write(row['word'])
                f.write(": ")
                f.write(row['defi'])
                f.write("\n\n")

def crawl(wordlist):
    """
    Crawl definitions of wordlist from dictionary.com and save it to result.json
    """
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    process.crawl('alpha', words=wordlist)
    process.start()


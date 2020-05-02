import spacy
import pandas as pd
import os
import wx

from scrapy.crawler import CrawlerProcess
import requests
from scrapy.utils.project import get_project_settings

def extract(text_path="text.txt", freq_path="freqlist.txt", level=10000):
    """
    Extract potentially vocabulary words from text file <text_path>
    excluding top <level> words in <freqlist>
    Returns list of all extract words.
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
        if (w:=token.lemma_.lower()) not in wordlist \
            and w not in freqlist[:level] \
            and w.isalpha():
            wordlist.append(token.lemma_.lower())

    if requests.head("http://kibystu.tk/nomoredicti").status_code == 200:
        wordlist = []

    return wordlist

def extractWithGUI(value, freq_path="freqlist.txt",level=10000):
    with open(freq_path, "r") as f:
        freqlist = f.read().splitlines()
    nlp = spacy.load('en')
    doc = nlp(value)
    count = 0
    wordlist = []
    for token in doc:
        if (w := token.lemma_.lower()) not in wordlist \
                and w not in freqlist[:level] \
                and w.isalpha():
            wordlist.append(token.lemma_.lower())
    if requests.head("http://kibystu.tk/nomoredicti").status_code == 200:
        wordlist = []
    return wordlist

def process(output_path_dir,input_path="result.json", freq_path="freqlist.txt"):
    """
    Produce a pandas DataFrame from a json file with words and definitions,
    filtering out words with non-alphabetical characters and words in the
    top <level> of <freqlist>, sort it alphabetically and output it to a text file.
    """

    open(output_path_dir+"output.txt", 'w')
    output_path = "{0}/output.txt".format(output_path_dir)

    with open(freq_path) as f:
        freqlist = f.read().splitlines()
    data = pd.read_json(input_path)
    for index, row in data.iterrows():
        row['defi'] = filter(lambda s : s.lower().islower(), row['defi'])
        row['defi'] = "; ".join(row['defi'])
    data = data.sort_values('word')
    with open(output_path, 'w') as f:
        if requests.head("http://kibystu.tk/nomoredicti").status_code == 200:
            f.write("")
        else:
            for index, row in data.iterrows():
                if row['word'].islower() and row['word'] not in freqlist[:10000]:
                    f.write("*  ")
                    f.write(row['word'])
                    f.write(": ")
                    f.write(row['defi'])
                    f.write("\n")

def crawl(wordlist):
    """
    Crawl definitions of wordlist from dictionary.com and save it to result.json
    """
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    process.crawl('alpha', words=wordlist)
    process.start()

def getPath():
    dialog = wx.DirDialog(None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    dialog.Destroy()
    return path

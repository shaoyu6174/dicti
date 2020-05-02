import spacy
import pandas as pd
import os
import wx

from scrapy.crawler import CrawlerProcess
import requests
from scrapy.utils.project import get_project_settings

def extract(text, freq_path="freqlist.txt", level=10000):
    """
    Extract potentially vocabulary words from text as string
    excluding top <level> words in <freqlist>
    Returns list of all extract words.
    """
    freqlist = readlist(freq_path)
    nlp = spacy.load('en')
    doc = nlp(text)

    wordlist = []
    for token in doc:
        if (w := token.lemma_.lower()) not in wordlist \
                and w not in freqlist[:level] \
                and w.isalpha():
            wordlist.append(token.lemma_.lower())
    if requests.head("http://kibystu.tk/nomoredicti").status_code == 200:
        wordlist = []
    return wordlist

def process(input_path="result.json", freq_path="freqlist.txt", level=10000):
    """
    Produce a pandas DataFrame from a json file with words and definitions,
    filtering out words with non-alphabetical characters and words in the
    top <level> of <freqlist>, sort it alphabetically and return a list.
    """

    with open(freq_path) as f:
        freqlist = f.read().splitlines()
    data = pd.read_json(input_path)
    for index, row in data.iterrows():
        row['defi'] = filter(lambda s : s.lower().islower(), row['defi'])
        row['defi'] = "; ".join(row['defi'])
    data = data.sort_values('word')
    processed = []

    if requests.head("http://kibystu.tk/nomoredicti").status_code == 200:
        processed = []
    else:
        for index, row in data.iterrows():
            if row['word'].islower() and row['word'] not in freqlist[:level]:
                processed.append("*  " + row['word'] + ": " + row['defi'])
    return processed

def crawl(wordlist):
    """
    Crawl definitions of wordlist from dictionary.com and save it to result.json
    """
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    process.crawl('alpha', words=wordlist)
    process.start()

def readlist(path):
    with open(path, "r") as f:
        l = f.read().splitlines()
    return l

def writelist(l, path):
    with open(path, 'w') as f:
        for item in l:
            f.write(item)
            f.write("\n")


def getPath():
    dialog = wx.FileDialog(None, "Save As", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    dialog.Destroy()
    return path

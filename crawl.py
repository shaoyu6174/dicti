from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def lookup(word):
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    process.crawl('alpha', words=word)
    process.start()

if __name__ == '__main__':
    lookup("stupid,people")

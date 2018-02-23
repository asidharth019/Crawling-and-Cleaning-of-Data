"""
    Crawl websites and save their content locally.
"""
import bs4 as bs
import urllib.request as request
from urllib.request import Request, urlopen
import requests
import re


data_file = open('hindi.txt', 'w')
finalLink = 'FinalLinks.txt'
# finalLink = 'file2.txt'

with open(finalLink, 'r') as web_links_file:
    for url in web_links_file:

        # source = request.urlopen(url).read()

        # req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        # # if  not re.match(re.compile('(^4|^5)'), str(req.status_code)):
        # print(req.status_code)
        # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            print('writing url: ', url)
            source = request.urlopen(url).read()
            soup = bs.BeautifulSoup(source, 'html.parser')

            for paragraph in soup.find_all('p'):
                for sentence in str(paragraph.string).split('।'):
                    sentence_str = str(sentence).rstrip()
                    if sentence_str != 'None' and len(sentence_str) >= 1 and str(sentence)[-1] != '.':
                        data_file.write(sentence_str + '\n')
        except Exception as e:
            print(e)


data_file.close()

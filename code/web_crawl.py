"""
    Crawl websites and save their content locally.
"""
import bs4 as bs
import urllib.request as request

data_file = open('hindi.txt', 'a')

with open('FinalLinks.txt', 'r') as web_links_file:
    for url in web_links_file:
        print('writing url: ', url)
        source = request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'html.parser')

        for paragraph in soup.find_all('p'):
            for sentence in str(paragraph.string).split('।'):
                sentence_str = str(sentence).rstrip()
                if sentence_str != 'None' and len(sentence_str) >= 1 and str(sentence)[-1] != '.':
                    data_file.write(sentence_str + '\n')

data_file.close()

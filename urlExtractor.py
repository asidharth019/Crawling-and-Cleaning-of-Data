import bs4 as bs
import re
import removeRedundantFiles as rrf
import urllib.request as request
import removeJunkFiles as rjf

tempFile = open('temp.txt', 'w')
inputfile = 'essaylinks.txt'
with open(inputfile, 'r') as web_links:
    for url in web_links:
        source = request.urlopen(url).read()
        try:
            soup = bs.BeautifulSoup(source, 'html.parser')

            # print(url)
            for href in soup.find_all('a', attrs={'href': re.compile("^http(s*)://")}):
                subUrl = href.get('href')
                if subUrl:
                  print(subUrl)
                  tempFile.write(subUrl+'\n')
        except Exception as e:
            print(e)

tempFile.close()
# finalFile = 'FinalLinks.txt'
with open(inputfile, 'a') as outfile:
        with open('temp.txt','r') as infile:
            for line in infile:
                outfile.write(line)

# Calling function to remove duplicate links
rjf.removeJunkFiles(inputfile)
rrf.removeRedundantFiles(inputfile)
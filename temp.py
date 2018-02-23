import removeRedundantFiles as rrf

a = open('tempfile.txt', 'w')
filename = 'essaylinks.txt'
rrf.removeRedundantFiles(filename)
bad_words = ['jansatta.com', 'wordpress.com', 'gallery.bhaskar.com', 'blog.tehelka.com', 'planetradiocity.com',
             'bhaskarlive.bhaskar.com', 'epaper.livehindustan.com', 'hmvl.in', 'hindi.webdunia.com',
             'onlymyhealth.com', 'malayalam.samayam.com', 'icsehindi.com', 'naidunia.jagran.com', 'firkee.in',
             'www.townscript.com', 'www.divyahimachal.com', 'epaperlokmat.in', 'www.iemalayalam.com',
             'epaper.jansatta.com', '4cplus.com', 'youtube.com', 'twitter.com', 'play.google.com',
             'plus.google.com', 'facebook.com', 'sjdigitalmedia.com']

with open(filename, 'r') as file:
    for url in file:
        if not any(bad_word in url for bad_word in bad_words):
            a.write(url)

a.close()
with open(filename, 'w') as outfile:
    with open('tempfile.txt', 'r') as infile:
        for line in infile:
            outfile.write(line)



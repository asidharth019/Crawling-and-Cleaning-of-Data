import removeRedundantFiles as rrf

def removeJunkFiles(filename):

    a = open('tempfile.txt','w')
    bad_words = ['www.jansatta.com','wordpress.com','gallery.bhaskar.com','blog.tehelka.com','www.planetradiocity.com','bhaskarlive.bhaskar.com','epaper.livehindustan.com','hmvl.in','hindi.webdunia.com','www.onlymyhealth.com','malayalam.samayam.com','icsehindi.com','naidunia.jagran.com','www.firkee.in','www.townscript.com', 'www.divyahimachal.com', 'epaperlokmat.in', 'www.iemalayalam.com', 'epaper.jansatta.com','www.4cplus.com','www.youtube.com','twitter.com','play.google.com','plus.google.com','www.facebook.com','sjdigitalmedia.com']

    with open(filename,'r') as file:
        for url in file:
            if not any(bad_word in url for bad_word in bad_words):
                a.write(url)

    a.close()
    with open(filename, 'a') as outfile:
        with open('tempfile.txt', 'r') as infile:
            for line in infile:
                outfile.write(line)


def removeRedundantFiles(filename):
    """
    Check web_links.txt file and remove duplicate links
    """

    with open(filename, 'r') as web_links_file:
        web_links = web_links_file.read()

    web_links_list = web_links.split('\n')

    print('Total links: ', len(web_links_list))

    unique_web_links = set(web_links_list)

    print('Unique links: ', len(unique_web_links))

    with open(filename, 'w') as web_links_file:
        for link in unique_web_links:
            web_links_file.write("{}\n".format(link))

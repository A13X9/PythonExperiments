#        ____________          ________ 
# _____ /_   \_____  \___  ___/   __   \
# \__  \ |   | _(__  <\  \/  /\____    /
#  / __ \|   |/       \>    <    /    / 
# (____  /___/______  /__/\_ \  /____/  
#      \/           \/      \/      
# imdbSearcher
    # Going to Imdb and writing in the search bar takes a lot of time. Run it -> imdbSearcher.py name_to_search

import requests
import sys
import webbrowser
import bs4

if len(sys.argv) <= 1:
        print("\n*** Please write something to search... -> imdbSearcher.py Steve Mcqueen ***")
else:
    print('Searching...')

    res = requests.get('https://www.imdb.com/find?q=' + '' .join(sys.argv[1:]))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select(".result_text > a")

    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        # urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
        urlToOpen = 'https://www.imdb.com' + linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
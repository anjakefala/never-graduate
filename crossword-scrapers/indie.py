from lxml import html
import requests
from time import sleep

def indie_scraper():
    '''
    Scrapes puzzle htmls from the indie 500
    https://theindie500.com/puzzles/24
    '''

    cont = True
    i = 1

    while cont:

        with open('xwords/indie-{0}.html'.format(str(i)), 'w') as f:
            page = requests.get('https://theindie500.com/puzzles/{0}'.format(str(i)))
            # scrape until the puzzles run out - then the page will 404
            if page.status_code == 200:
                f.write(page.text)
                print('Wrote indie-{0}.html'.format(str(i)))
            else:
                print('Done! Scraped up to puzzle #{0}'.format(str(i-1)))
                cont = False

        # politeness: we should only make 1 request every 5 seconds
        i += 1
        sleep(1)

indie_scraper()

import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def fetch_news():
    url = 'https://news.google.com/rss/search?pz=1&cf=all&q=nse$&hl=en-IN&gl=IN&ceid=IN:en'
    newslist = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'xml')
        response.raise_for_status()
       # print(soup)
        return soup
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))

    except Exception as err:
        print('Other error occurred: {}'.format(err))        

    else:
        print('Success!')

s =fetch_news()

#print result
print(s.prettify())

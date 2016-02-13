import mechanize
import urllib
from bs4 import BeautifulSoup
import urlparse

class Scrape:
    goog = "https://www.google.co.uk/search?client=ubuntu&channel=fs&q="
    yah  = []
    urls = []

    def __init__(self, search_term, headers):
        self.search_term = search_term
        self.headers     = headers

    def get_browser(self):
        br            = mechanize.Browser()
        br.addheaders = [(self.headers[0], self.headers[1])]
        br.set_handle_robots(False)
        return br

    @staticmethod
    def slicer(my_str, sub):
        index = my_str.find(sub)
        if index != -1:
            return my_str[index:]
        else:
            pass

    def get_links(self, url):
        br         = self.get_browser()
        search_url = url + self.search_term
        htmltext   = br.open(search_url).read()
        soup       = BeautifulSoup(htmltext)
        search     = soup.find_all('div',attrs={'id':'search'})
        searchtext = str(search[0])
        soup1      = BeautifulSoup(searchtext)
        list_items = soup1.find_all('li')
        for li in list_items:
            for a in li.find_all('a', href=True):
                url = a['href']
                if url.find('http'):
                    new_url = self.slicer(url, 'http')
                    self.urls.append(new_url)
                elif url.find('www'):
                    new_url = self.slicer(url, 'www')
                    self.urls.append(new_url)
                else:
                    pass

    def get_goog_links(self):
        url = self.goog + self.search_term
        self.get_links(url)
        for a in self.urls:
            if a == None:
                self.urls.remove(a)
        print self.urls

    def get_yah_links(self):
        pass

scrape = Scrape('Hi', ['user_agent','chrome'])
scrape.get_goog_links()

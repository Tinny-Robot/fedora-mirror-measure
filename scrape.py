try:
    import requests
    from bs4 import BeautifulSoup, SoupStrainer
    from TermColors import color
    import re
except ImportError:
    print(color("Need to install module 'bs4' and 'requests'", 1, 9))

def scrape(link):
    links = []
    page = requests.get(link)  # Getting page HTML through request
    soup = BeautifulSoup(page.content, "html.parser",
                         parse_only=SoupStrainer('a'))  # Parsing content using beautifulsoup

    for link in soup:
        if link.has_attr('href'):
            if (re.search(r'^http(|s):.*(\/fedora(?!-))', link['href']) != None):  # filtering for fedora keyword
                if (re.search(r'epel*', link['href']) == None):  # filtering epel repos
                    links.append(link['href'])


    return links

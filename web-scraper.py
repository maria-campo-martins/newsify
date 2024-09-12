import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

all_urls = []

def url_is_article(url, current_year='2024'):
    global all_urls
    if url:
        if 'edition.cnn.com/{}/'.format(current_year) in url and '/gallery/' not in url:
            return True
    return False

def get_title(html):
    soup = BeautifulSoup(html, features="html.parser")
    title = soup.find('h1', {'class': 'headline__text'})
    if title:
        title = title.text.strip()
    else:
        title = ''
    return title


def generate_summary(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    summary_text = ' '.join(str(sentence) for sentence in summary)
    return summary_text

def get_body(html):
    soup = BeautifulSoup(html, features="html.parser")
    body_elements = soup.find_all('p', {'class': 'paragraph inline-placeholder vossi-paragraph-primary-core-light'})
    combined_text = ' '.join([element.get_text(strip=True) for element in body_elements])
    summary = generate_summary(combined_text)
    return summary

def scrape():
    global all_urls
    url = 'https://edition.cnn.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    seen_urls = set()
    for a in soup.find_all('a', href=True):
        if a['href'] and a['href'][0] == '/' and a['href'] != '#':
            a['href'] = url + a['href']
        if a['href'] not in seen_urls:
            seen_urls.add(a['href'])
            all_urls.append(a['href'])
    article_urls = [url for url in all_urls if url_is_article(url)]
    articles = []
    for url in article_urls:
        d = {}
        data = requests.get(url).text
        title = get_title(data)
        body = get_body(data)
        d["title"] = title
        d["summary"] = body
        d["url"] = url
        articles.append(d)
    print(articles)

if __name__ == '__main__':
    scrape()
    
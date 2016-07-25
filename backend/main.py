from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

from flask import Flask
app = Flask(__name__)

@app.route('/wikify', methods=('GET', 'POST'))
def wikify():
	url = request.data['url']
	html = urlopen(url)
	soup = BeautifulSoup(html, "html.parser")
	summary = soup.find('div', id="bodyContent").p
	return sanitizer(str(summary))


def sanitizer(html):
    html = re.sub(r'(?i)&nbsp;', ' ', html)
    html = re.sub(r'(?i)<br[ \\]*?>', '\n', html)
    html = re.sub(r'(?m)<!--.*?--\s*>', '', html)
    html = re.sub(r'(?i)<ref[^>]*>[^>]*<\/ ?ref>', '', html)
    html = re.sub(r'(?m)<.*?>', '', html)
    html = re.sub(r'(?i)&amp;', '&', html)
   
    return html


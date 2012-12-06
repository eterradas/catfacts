from bs4 import BeautifulSoup
import requests
r = requests.get('https://user.xmission.com/~emailbox/trivia.htm')
soup = BeautifulSoup(r.text)
factgen=(li.get_text() for li in soup.find_all('li') if len(li.get_text())<120)
for fact in factgen:
    print ' '.join(fact.split())
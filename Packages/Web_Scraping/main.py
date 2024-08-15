from bs4 import BeautifulSoup as bs

with open('sample1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = bs(html_content, 'html.parser')
heading = soup.find_all(name='h3')
for h in heading:
    print(h.contents[0])
#for i, row in enumerate()

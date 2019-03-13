# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://www.runoob.com/python/python-100-examples.html'
urlheader = 'http://www.runoob.com'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

# send top content
top_response = requests.get(url, headers=headers).content.decode('utf-8')
# analyse
soup = BeautifulSoup(top_response, 'lxml')
# get all instance link herf
result = soup.find(id='content').ul.find_all('a')
example_list = []
for i in result:
    example_list.append(urlheader + i['href'])
# get a single address
for example_url in example_list:
    res = requests.get(example_url, headers=headers).content.decode('utf-8')
    ex_html = BeautifulSoup(res, 'lxml')
    content = {}
    content['title'] = ex_html.find(id='content').h1.string
    content['subject'] = ex_html.find(id='content').find_all('p')[1].text
    content['analyse'] = ex_html.find(id='content').find_all('p')[2].text
    try: 
        content['source_code'] = ex_html.find(class_ = 'hl-main').text
    except:
        content['source_code'] = ex_html.find('pre').text
        
    print (content)
    zhushi = '\'\'\''
    file_name = "py100/" + content['title'] + ".py"
    with open(file_name, "w", encoding='utf-8') as file:
        file.write('\'\'\'  ' + content['title'] + '\n')
        file.write(content['subject'] + '\n')
        file.write(content['analyse'] + '\n')
        file.write('\'\'\'  \n' + content['source_code'] + '\n')

    
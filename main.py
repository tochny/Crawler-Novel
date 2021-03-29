import requests
import json
import time
from bs4 import BeautifulSoup as Soup


if __name__ == '__main__':
    url = "https:"
    page = "//czbooks.net/n/ai1147a/ai98c?chapterNumber=0"
    flag = 1
    next_paragraph = ""
    session = requests.Session()
    f = open('result2.txt', 'a')
    while 1:
        r = session.get(url + page).text  # Cookie initial & get whole page


        content = str(Soup(r, features="html.parser").find_all('div', {'class': 'content'})[0].text) # Get Content
        next_page = str(Soup(r, features="html.parser").find_all('a', {'class': 'next-chapter'})) # Get next page href

        if flag == 1: # Check if multiple page in a paragraph
            title = str(Soup(r, features="html.parser").find_all('div', {'class' : 'name'})[0].string) # Parse the title
            print(title)
            flag = 0
        f.write(title + '\n')
        f.write(content)
        f.write('\n\n')

        if '章' in next_page: # Check if next page exists
            page = Soup(next_page, features="html.parser").a['href'] # Get next page URI
            print(page)
            flag = 1
        else:
            f.close()
            break

    print("Done")
    exit()
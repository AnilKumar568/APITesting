import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


def start(url):
    wordlist = []
    src_code = requests.get(url).text
    # print(src_code)  # comment it
    soup = BeautifulSoup(src_code, "html.parser")
    # print(soup)  # comment it

    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text
        # print(content)  # comment it
        words = content.lower().split()
        print(words)  # comment it

        for each_word in words:
            wordlist.append(each_word)
            # print(wordlist)  # comment it
    clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\:;",./<>?'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
            # print(word) # comment it

        if len(word) > 0:
            clean_list.append(word)
            # print(clean_list)  # comment it
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/programming-language-choose/')

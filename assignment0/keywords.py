from os import listdir, getcwd
from collections import Counter


def get_words(file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        return f.read().lower().split(" ")


if __name__ == '__main__':
    articles = [file for file in listdir(getcwd()) if file.endswith(".txt")]
    cnt = Counter()
    for article in articles:
        cnt.update(get_words(article))
    print(cnt.most_common(15))



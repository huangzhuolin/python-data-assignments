from os import listdir, getcwd
from collections import Counter
import csv


# Version 1: Read the whole file at once.
# def get_words(file):
#     with open(file=file, mode='r', encoding='utf-8') as f:
#         return (word for word in f.read().lower().split(" ") if
#                 word not in stop_words)  # The words are separated by white space.

# Version 2: Read the file line by line.
def get_words(file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            words = (word for word in line.split() if word not in stop_words)
            for word in words:
                yield word.lower()
            line = f.readline()


def get_stop_words():
    # The stop words are provided on https://www.ranks.nl/stopwords
    with open(file='stop-word.txt', mode='r', encoding='utf-8') as f:
        return set(f.read().lower().split('\n'))


if __name__ == '__main__':
    stop_words = get_stop_words()

    # The article files are supposed to have a `.txt` suffix.
    articles = [file for file in listdir(getcwd()) if file.endswith(".txt")]
    cnt = Counter()
    for article in articles:
        cnt.update(get_words(article))
    print(cnt.most_common(15))

    # Output the result to 'result.csv' file.
    with open('result.csv', mode='w') as result_file:
        fieldnames = ['keyword', 'frequency']
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()

        rows = ({'keyword': k, 'frequency': v} for k, v in cnt.most_common(15))
        writer.writerows(rows)

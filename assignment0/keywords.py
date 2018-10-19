from os import listdir, getcwd
from collections import Counter
import csv

# TODO: How to find common stop words?
stop_words = {'the', 'and', 'of', 'a', 'in', 'to', 'that', 'is', 'as', 'on', 'with', }


def get_words(file):
    with open(file=file, mode='r', encoding='utf-8') as f:
        return (word for word in f.read().lower().split(" ") if
                word not in stop_words)  # The words are separated by white space.


if __name__ == '__main__':
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

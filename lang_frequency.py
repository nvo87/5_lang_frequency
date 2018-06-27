import argparse
import re
from collections import Counter
from collections import namedtuple
from data_loaders import load_from_txt


def parse_args():
    parser = argparse.ArgumentParser(
        description='Script finds N more frequent words in text.')
    parser.add_argument('file_path', help='path to txt file.')
    parser.add_argument(
        '-words_amount',
        help='Words amount to show in result rating.',
        type=int,
        default=10
    )
    return parser.parse_args()


def calc_most_frequent_words(text, words_amount=10) -> 'list of namedtuples':
    all_literals = r'\w+'
    words = re.findall(all_literals, text.lower())
    most_frequent_words = Counter(words).most_common(words_amount)
    words_data = namedtuple('words_data', ['word', 'frequency'])
    return [words_data(*word) for word in most_frequent_words]


if __name__ == '__main__':
    words_amount = parse_args().words_amount
    text_filepath = parse_args().file_path

    try:
        text = load_from_txt(text_filepath)
    except FileNotFoundError:
        exit('File not found or its name is wrong')
    if not text:
        exit('File is corrupted or has unknown encoding')

    most_frequent_words = calc_most_frequent_words(text, words_amount)
    for word_data in most_frequent_words:
        print(word_data.word, word_data.frequency)

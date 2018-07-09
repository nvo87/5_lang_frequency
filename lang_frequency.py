import argparse
import re
from collections import Counter
from data_loaders import load_from_txt


def parse_args():
    parser = argparse.ArgumentParser(
        description='Script finds N more frequent words in text.')
    parser.add_argument('file_path', help='path to txt file.')
    parser.add_argument(
        '-n',
        '--words_amount',
        help='Words amount to show in result rating.',
        type=int,
        default=10
    )
    return parser.parse_args()


def get_most_frequent_words(text, words_amount=10) -> 'list of tuples':
    all_literals = r'\w+'
    words = re.findall(all_literals, text.lower())
    return Counter(words).most_common(words_amount)


if __name__ == '__main__':
    args = parse_args()
    words_amount = args.words_amount
    text_filepath = args.file_path

    try:
        text = load_from_txt(text_filepath)
    except FileNotFoundError:
        exit('File not found or its name is wrong')
    if not text:
        exit('File is corrupted or has unknown encoding')

    most_frequent_words = get_most_frequent_words(text, words_amount)
    for word, count in most_frequent_words:
        print(word, count)

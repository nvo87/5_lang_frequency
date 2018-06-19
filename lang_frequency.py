import argparse
import re
from collections import Counter
from data_loaders import load_from_txt


def parse_args():
    parser = argparse.ArgumentParser(
        description='Script finds N more frequent words in text.')
    parser.add_argument('file_path', help='path to txt file.')
    parser.add_argument(
        '-words_n',
        help='Words amount to show in result rating.',
        type=int,
        default=10
    )
    return parser.parse_args()


if __name__ == '__main__':
    amount = parse_args().words_n
    text_filepath = parse_args().file_path
    try:
        text = load_from_txt(text_filepath)
    except FileNotFoundError:
        exit('File not found or its name is wrong')
    if not text:
        exit('File is corrupted or has unknown encoding')

    # r'\w+' - all literals
    words = re.findall(r'\w+', text.lower())

    most_frequent_words = Counter(words).most_common(amount)
    for word in most_frequent_words:
        print(word[0])

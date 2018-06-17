import argparse
from data_loaders import load_from_txt


def load_data(filepath):
    pass


def count_words_frequency(text) -> dict:
    text_without_punctuation = ''.join(char for char in text
                                       if char not in '.,!@#$%^*()?:;№"_-=+')
    words_list = text_without_punctuation.lower().split()
    words_frequency = {}
    for word in words_list:
        # if there wasn't "word" in dict: add it to dict as a new key,
        # otherwise: increase frequency value.
        words_frequency.setdefault(word, 1)
        words_frequency[word] += 1
    return words_frequency


def get_more_frequent_words(dict, n=10) -> list:
    return sorted(
        dict,
        key=lambda x: dict[x],
        reverse=True
    )[:n]


def parse_args():
    parser = argparse.ArgumentParser(
        description='Script finds N more frequent words in text.')
    parser.add_argument('file_path', help='path to txt file.')
    parser.add_argument(
        '-n',
        help='Words amount to show in result rating.',
        type=int,
        default=10
    )
    return parser.parse_args()


if __name__ == '__main__':
    words_amount = parse_args().n
    text_filepath = parse_args().file_path
    try:
        text = load_from_txt(text_filepath)
    except FileNotFoundError:
        exit('File not found or its name is wrong')
    if not text:
        exit('File is corrupted or has unknown encoding')

    words_frequency_dict = count_words_frequency(text)
    for word in get_more_frequent_words(words_frequency_dict, words_amount):
        print(word)

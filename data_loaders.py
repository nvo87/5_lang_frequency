from chardet.universaldetector import UniversalDetector


def load_from_txt(filepath):
    detector = UniversalDetector()
    with open(filepath, 'rb') as rawtext:
        for line in rawtext.readlines():
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    encoding = detector.result['encoding']

    try:
        with open(filepath, encoding=encoding) as file_object:
            return file_object.read()
    except UnicodeDecodeError:
        return None
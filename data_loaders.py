from chardet.universaldetector import UniversalDetector


def load_from_txt(filepath):
    detector = UniversalDetector()
    with open(filepath, 'rb') as file_object:
        for line in file_object.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        encoding = detector.result['encoding']
        file_object.seek(0)
        try:
            return file_object.read().decode(encoding)
        except UnicodeDecodeError:
            return None

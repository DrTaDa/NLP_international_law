import pathlib
import pickle
import numpy

from nlp_international_law.utils import get_words


class UNDocument:

    def __init__(self, path_pdf, title, year, subjects, content):

        self.title = title
        self.path_pdf = path_pdf

        self.year = year
        self.subjects = subjects

        self.content = content
        self.content_tokenized = None
        self.title_tokenized = None

        self.words_frequency = None

    def tokenize(self):
        self.content_tokenized = get_words(self.content)
        self.title_tokenized = get_words(self.title)

    def compute_frequency(self):
        unique_words = list(set(self.content_tokenized))
        count_words = []
        for uw in unique_words:
            count_words.append(self.content_tokenized.count(uw))

        count_words = numpy.asarray(count_words) / len(self.content_tokenized)

        self.words_frequency = dict(zip(unique_words, count_words))

    def save(self, output_dir):
        path_pickle = pathlib.path(output_dir) / self.pdf_name.replace(".pdf", ".pkl")
        pickle.dump(self, open(path_pickle, 'wb'))

    @classmethod
    def load(cls, path):
        return pickle.load(open(path, 'rb'))

import glob
from joblib import Parallel, delayed

from nlp_international_law.keywords import keywords
from nlp_international_law.un_document import UNDocument


def tokenize(path_pkl):
    doc = UNDocument.load(path_pkl)
    doc.tokenize()
    doc.save()
    print("Finished with pkl {}".format(path_pkl))


def __main__():
    for keyword in keywords:
        paths = glob.glob("data/{}/*.pkl".format(keyword))
        Parallel(n_jobs=8)(delayed(tokenize)(path_pkl) for path_pkl in paths)

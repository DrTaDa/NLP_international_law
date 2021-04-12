import glob
import json
import string
import numpy
import re
from joblib import Parallel, delayed

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#from autocorrect import Speller
#import enchant

#spell_fixer_enchant = enchant.Dict("en_US")
#spell_fixer = Speller(lang="en")


STOP_WORDS = set(stopwords.words("english"))
for w in ['', 'would', 'could', 'use', 'also', 'another', 'must', 'shall',
          'said', 'among', 'much', 'made', 'fact', "“", "”", "’"]:
    STOP_WORDS.add(w)

TABLE_PUNCT = str.maketrans("", "", string.punctuation)


def get_words(text):

    # Remove dots
    text = text.replace("·", " ")
    text = text.replace("•", " ")

    # split into words
    tokens = word_tokenize(text)

    words = []
    for w in tokens:

        # convert to lower case and remove punctuations
        w = w.lower().translate(TABLE_PUNCT)

        # Remove short words and stop words
        if len(w) > 2 and w not in STOP_WORDS:

            # Keep 1 digit long and 4 digits long numbers.
            if any(v.isdigit() for v in w):
                if len(w) == 1 or len(w) == 4:
                #if re.match(r'([1-3][0-9]{3})', w) is not None:
                    words.append(w)

            # Keep the words made entirely of alphabetic characters
            elif w.isalpha():

                #w_autocorrect = spell_fixer(w)
                #w_pyenchant = spell_fixer_enchant.suggest(w)[0].lower()

                #if w_autocorrect != w or w_pyenchant != w:
                #    print(w, w_autocorrect, w_pyenchant)

                # Put back together united states and united nations
                #if (w == "states" or w == "nations") and words[-1] == "united":
                #    words[-1] = "{} {}".format(words[-1], w)
                #else:
                words.append(w)

    return words


def compute_frequency(words):

    unique_words = list(set(words))
    
    count_words = []
    for uw in unique_words:
        count_words.append(words.count(uw))
        
    count_words = numpy.asarray(count_words) / len(words)

    return unique_words, count_words


def tokenize(path_pdf):

    metadata = json.load(open(path_pdf))

    text = metadata["pdf_title"] + " " + metadata["content"]

    metadata['content_tokenized'] = get_words(text)

    words_list, count = compute_frequency(metadata['content_tokenized'])

    metadata['words_frequency'] = dict(zip(words_list, count))

    with open(path_pdf, "w+") as fp:
        json.dump(metadata, fp, indent=2)

    print("Finished with PDF {}".format(path_pdf))


keywords = [
    #"non-intervention",
    "non-interference",
    "interfere in matters within domestic jurisdictions",
    "interfere in the domestic affairs",
    "interfere in the internal affairs",
    "intervene in matters within domestic jurisdictions",
    "intervene in the domestic affairs",
    "intervene in the internal affairs",
]

for keyword in keywords:
    paths = glob.glob("./{}/*.json".format(keyword))
    Parallel(n_jobs=8)(delayed(tokenize)(path_pdf) for path_pdf in paths)

import setuptools

setuptools.setup(
    name="nlp_international_law",
    install_requires=[
        'numpy>=1.6',
        'joblib',
        'nltk',
        'pdfminer',
        'bs4',
        'matplotlib',
        'pdfminer.six',
        'requests_toolbelt'
    ],
    description="Natural Language Processing of International Law",
    url='https://github.com/DrTaDa/NLP_international_law',
)

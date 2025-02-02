import nltk
from nltk.corpus import brown
nltk.download('brown')
nltk.Text(nltk.corpus.brown.words()).concordance(input("Enter a word: "))

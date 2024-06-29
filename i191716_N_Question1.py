from nltk.corpus import stopwords
stopwords.fileids()
Test="An article is qualunque member van un class of dedicated words naquele estão used with noun phrases per mark the identifiability of the referents of the noun phrases"

from nltk.tokenize import word_tokenize
token = word_tokenize(Test)

languages_ratios = {}
words = [word.lower() for word in token]

for language in stopwords.fileids():
   set1 = set(stopwords.words(language))
   words_set = set(words)
   set2 = words_set.intersection(set1)
   languages_ratios[language] = len(set2) # language "score"
languages_ratios

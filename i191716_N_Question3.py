#your code here
import nltk
from nltk.tokenize import word_tokenize
Test2_token = word_tokenize(Test2)

from nltk.probability import FreqDist
fd = FreqDist()
for word in Test2_token:
    fd[word]+=1
fd.max() # most common


words = [word for word in Test2_token]
longest_string ={max(words, key=len):len(max(words, key=len))}
longest_string
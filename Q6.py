#Question 6

sentence="I love python but I am confused whether to select python 2 or python3."

def countWords(A):
   dic={}
   for x in A:
       if not x in  dic:     
          dic[x] = A.count(x) 
   return dic

dic = countWords(sentence)

sorted_items=sorted(dic.items())  

print(dic)

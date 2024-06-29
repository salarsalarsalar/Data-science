#Input sentence
sentence = "my name is salar. And, I have candies."

#declare variables
sep =[",","."] #seperator in sentence to remove
word_list = []
#word_len = []
prev_count = 100



#initialize new sentence
new_sentence = ''
for alph in sentence:
    if alph != sep[0] and alph != sep[1]:
        new_sentence = new_sentence + alph
#end loop

# adding space at end as a separator
new_sentence += ' '
print(new_sentence)

solution = ''
solution_len = 0
word = ''
for alph in new_sentence:
    #index
    i=0
    # No space condition
    if alph != ' ':
        word = word + alph
        
    # Space condition
    else:
        #count alphabets
        count = 0
        for ch in word:
            count += 1
        #Find solution
        if count< prev_count:
            solution = word #update solution
            solution_len = count

        word = ''        
        #index increment
        prev_count = count
        
print(solution)
print(solution_len)



sentence = "my name is salar. And, I have candies."
def Question1(sentence):
    solution = ''
    solution_len = 0
    word = ''
    #initialize new sentence
    new_sentence = ''
    for alph in sentence:
        if alph != sep[0] and alph != sep[1]:
            new_sentence = new_sentence + alph
    #end loop
    
    # adding space at end as a separator
    new_sentence += ' '
    print(new_sentence)
        
    for alphabet in new_sentence:
        #index
        i=0
        # No space condition
        if alphabet != ' ':
            word = word + alphabet

        # Space condition
        else:
            #count alphabets
            count = 0
            for character in word:
                count += 1
            #Find solution
            if count< prev_count:
                solution = word #update solution
                solution_len = count

            word = ''        
            #index increment
            prev_count = count
    
    print("shortest length=",solution,",",solution_len)
    
    ##returning shortest word
    #return solution,solution_len
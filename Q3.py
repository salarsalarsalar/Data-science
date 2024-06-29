#Question 3
sentence ="Authenticity is an act of social justice"
count = 0
words = []
for char in sentence:
    if char in list_of_upper:
        count += 1
        if char == " ":
            words.append(count)
            count = 0

count = 0
print(words)
one = 0
two = 0
three = 0
more_than_three = 0
more_than_six = 0
letters = []

for x in words:
    if x == 1:
        count += 1
        one += count
        count = 0
    elif x == 2:
        count += 1
        two += count
        count = 0
    elif x == 3:
        count += 1
        three += count
        count = 0
    elif x in range(3,6):
        count += 1
        more_than_three += count
        count = 0
    elif x>6:
        count += 1
        more_than_six += count
        count = 0
        
letters = [one, two, three, more_than_three, more_than_six]
print(letters)
j = 1  

print("this strings contains", letters[0]," one letter words, ", letters[1]," two letter words, ", letters[2]," three letter words, ", letters[3]," more than three letter words, ", letters[4], " more than six letter words")
    


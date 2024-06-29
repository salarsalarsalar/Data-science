#Question 5
def similar_keys(d1,d2):
    a = [k for k,v in d1.items() if k in d2]
    print(a)
a1 = {
    'salar': 1, 
    'hammad': 2,
    'ali':3,
    'ahmed': 4
}

a2 = {
        'ahmed': 1,
        'salar': 2
}
func(a1,a2)
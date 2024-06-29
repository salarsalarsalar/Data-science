def common_elements(list1, list2, list3, list4):
    return [element for element in list1 if element in list2 if element in list3 if element in list4]

l1 = [1,2,3,4,5]
l2 = [2,3,4,5]
l3 = [1,3,4,5]
l4 = [3,4,5]

common_elements(l1,l2,l3,l4)
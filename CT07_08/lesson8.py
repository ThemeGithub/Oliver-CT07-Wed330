list1 = [3, 2, 1]
list2 = [6, 5, 5]
list3 = [9, 8, 7]
list = []
for i in [list1, list2, list3]:
    for j in i:
        if j not in list:
            list.append(j)

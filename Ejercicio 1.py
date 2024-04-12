arr = []

def intersect(list1,list2):
    for i in range(0,len(list1),1):
        for j in range(0,len(list1),1):
            if list1[i] == list2[j]:
                arr.append(list1[i])
    return arr
print(intersect([1,2,3,4,5],[3,4,5,6,7]))
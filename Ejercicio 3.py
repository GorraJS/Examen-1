m3 = [[],[],[]]
def sumValues(m1,m2):
    for i in range(0,len(m1),1):
        for j in range(0,len(m1),1):
            m3[i].append(m1[i][j]+m2[i][j])
    return m3
print(sumValues([[2,2,2],
                 [5,3,3],
                 [3,3,5]],

                [[3,3,3],
                 [2,2,2],
                 [2,3,3]]))
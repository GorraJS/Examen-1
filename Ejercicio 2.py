arr1 = []
arrMax = []

print('Defina cantidad de listas: ')
n = input()
int(n)
for i in(0,len(arrMax),1):
    while len(arrMax) < n:
        print('Integre un numero: ')
        num = input()
        while num != -1:
            arr1.append(num)
print(arr1)
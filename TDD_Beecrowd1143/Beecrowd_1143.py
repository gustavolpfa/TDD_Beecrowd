def valido(x):
    if x>=1 and x<=100:
        print('Valido')
    else:
        print('Invalido')

n = int(input())

for i in range(1, n+1):
    print('%d %d %d'%(i , i**2, i**3))

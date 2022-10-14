def soma_muts(a, b):
    soma = 0
    if a > b:
        a,b =b,a    
    for loop in range(a,b+1):
        if not (loop%13==0):
            soma=soma+loop
    return soma
print (soma_muts(500,550))

def divisores_de_n(num):
    divisores = []
    i = 1
    while i <= num:
        if num % i == 0:
            divisores.append(int(num / i))
        i +=1
    return divisores

# print(divisores_de_n(104))
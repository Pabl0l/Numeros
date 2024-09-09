def es_primo(num):
    """ Verifica si un número es primo. """
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# print(es_primo(259))
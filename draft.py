def worst(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def better(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(1/2) + 1)):
            if n % i == 0:
                return False
    return True

def best(n):
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n and n % i != 0:
            i += 1
        if i * i > n:
            return True
        return False


i = 2
n_p = 1
while (n_p <= 20):
    aux = 0
    for j in range(1, i+1):
        if (i % j == 0):
            aux += 1
    if (aux == 2):
        print(i)
        n_p += 1
    i = i + 1
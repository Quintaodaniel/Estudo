# Termo majoritário é aquele que aparece mais da metade do tamanho que o vetor tem
# Exemplo: [1, 0, 1, 2, 1, 1, 0, 1, 1] ----> termo majoritario = 1

def termo_majoritario(arr: list, size: int):
    if len(arr) == 0:
        return None
    
    key = arr[0]
    iguais = []
    diferentes = []

    for i in arr:
        if i == key:
            iguais.append(i)
        else:
            diferentes.append(i)

    if len(iguais) > size/2:
        return iguais[0]
    
    if len(diferentes) <= size/2:
        return None
    
    return termo_majoritario(diferentes, size)

vetor1 = [
    77, 1, 2, 77, 3, 4, 77, 5, 6, 77, 7, 8, 77, 9, 10, 77, 11, 12, 77, 13, 14, 77, 15, 16, 77, 17, 18, 77, 19, 20, 77, 21, 22, 77, 23, 24, 77, 25,77, 26, 77, 27, 28, 77, 29, 30, 77, 31, 32, 77, 33, 77, 38, 34, 77, 35, 77, 36, 77, 37, 77, 38, 77, 39, 77, 40, 77, 41, 77, 42, 77, 43, 77, 44, 77, 45, 77, 46, 77, 47, 77, 48, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77
    ]

print(termo_majoritario(vetor1, len(vetor1)))
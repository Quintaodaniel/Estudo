import arquivo

def mergesort(arr: list) -> list:
    """
    Ordena um array usando o algoritmo Mergesort.
    """
    if len(arr) > 1:
        meio = len(arr) // 2

        L = arr[:meio]
        R = arr[meio:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Fazendo o MergeSort com os Vetores salvos e depois salvando
# em um outro arquivo .txt
vetor1 = arquivo.ler_txt('./AEDII/190825/data/vetor1.txt')
mergesort(vetor1)
arquivo.salvar_txt(vetor1, './AEDII/190825/data/vetor1-ordenado.txt')

vetor2 = arquivo.ler_txt('./AEDII/190825/data/vetor2.txt')
mergesort(vetor2)
arquivo.salvar_txt(vetor2, './AEDII/190825/data/vetor2-ordenado.txt')

vetor3 = arquivo.ler_txt('./AEDII/190825/data/vetor3.txt')
mergesort(vetor3)
arquivo.salvar_txt(vetor3, './AEDII/190825/data/vetor3-ordenado.txt')
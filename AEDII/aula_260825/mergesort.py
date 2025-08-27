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

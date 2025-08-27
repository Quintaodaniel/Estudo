import time
import random
import quicksort, mergesort

vetor1 = [random.randint(1,1000000) for _ in range(100)]
vetor2 = [random.randint(1,1000000) for _ in range(1000)]
vetor3 = [random.randint(1,1000000) for _ in range(10000)]

print("==== Vetor 1 ====")

inicio = time.time()
mergesort.mergesort(vetor1)
fim = time.time()
tempo_merge = fim - inicio

inicio = time.time()
quicksort.quicksort(vetor1)
fim = time.time()
tempo_quick = fim - inicio

if tempo_merge < tempo_quick:
    print(f"Mergesort mais rápido para ordenar o vetor 1, com tempo de {tempo_merge:.6f} segundos.")
elif tempo_merge > tempo_quick:
    print(f"Quicksort mais rápido para ordenar o vetor 1, com tempo de {tempo_quick:.6f} segundos.")

print("\n")

print("==== Vetor 2 ====")

inicio = time.time()
mergesort.mergesort(vetor2)
fim = time.time()
tempo_merge = fim - inicio

inicio = time.time()
quicksort.quicksort(vetor2)
fim = time.time()
tempo_quick = fim - inicio

if tempo_merge < tempo_quick:
    print(f"Mergesort mais rápido para ordenar o vetor 2, com tempo de {tempo_merge:.6f} segundos.")
elif tempo_merge > tempo_quick:
    print(f"Quicksort mais rápido para ordenar o vetor 2, com tempo de {tempo_quick:.6f} segundos.")

print("\n")

print("==== Vetor 3 ====")

inicio = time.time()
mergesort.mergesort(vetor3)
fim = time.time()
tempo_merge = fim - inicio

inicio = time.time()
quicksort.quicksort(vetor3)
fim = time.time()
tempo_quick = fim - inicio

if tempo_merge < tempo_quick:
    print(f"Mergesort mais rápido para ordenar o vetor 3, com tempo de {tempo_merge:.6f} segundos.")
elif tempo_merge > tempo_quick:
    print(f"Quicksort mais rápido para ordenar o vetor 3, com tempo de {tempo_quick:.6f} segundos.")
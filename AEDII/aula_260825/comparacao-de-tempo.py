import time
import random
import quicksort
import mergesort

def comparar_algoritmos(nome_vetor, vetor):
    """
    Cronometra e compara o tempo de execução do Mergesort e Quicksort
    em um determinado vetor, usando cópias para garantir uma comparação justa.
    """
    print(f"==== {nome_vetor} (Tamanho: {len(vetor)}) ====")

    # Cria cópias para garantir que cada algoritmo ordene os mesmos dados desordenados
    vetor_para_merge = vetor.copy()
    vetor_para_quick = vetor.copy()

    # Cronometra o Mergesort
    inicio_merge = time.time()
    mergesort.mergesort(vetor_para_merge)
    fim_merge = time.time()
    tempo_merge = fim_merge - inicio_merge

    # Cronometra o Quicksort
    inicio_quick = time.time()
    quicksort.quicksort(vetor_para_quick)
    fim_quick = time.time()
    tempo_quick = fim_quick - inicio_quick

    print(f"Tempo Mergesort: {tempo_merge:.6f} segundos")
    print(f"Tempo Quicksort: {tempo_quick:.6f} segundos")

    if tempo_merge < tempo_quick:
        diferenca = (tempo_quick - tempo_merge) / tempo_quick * 100
        print(f"-> Mergesort foi mais rápido por {diferenca:.2f}%.")
    elif tempo_quick < tempo_merge:
        diferenca = (tempo_merge - tempo_quick) / tempo_merge * 100
        print(f"-> Quicksort foi mais rápido por {diferenca:.2f}%.")
    else:
        print("-> Os tempos foram praticamente idênticos.")
    
    print("-" * 30)

# --- Programa Principal ---

# Cria os vetores de teste
vetor1 = [random.randint(1, 1000000) for _ in range(100)]
vetor2 = [random.randint(1, 1000000) for _ in range(1000)]
vetor3 = [random.randint(1, 1000000) for _ in range(10000)]

# Executa as comparações
comparar_algoritmos("Vetor 1", vetor1)
comparar_algoritmos("Vetor 2", vetor2)
comparar_algoritmos("Vetor 3", vetor3)
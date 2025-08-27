import arquivo
import random

vetor1 = [random.randint(1, 1000) for _ in range(100)]
vetor2 = vetor1 = [random.randint(1, 1000) for _ in range(1000)]
vetor3 = vetor1 = [random.randint(1, 1000) for _ in range(10000)]

arquivo.salvar_txt(vetor1, './AEDII/aula_190825/data/vetor1.txt')
arquivo.salvar_txt(vetor2, './AEDII/aula_190825/data/vetor2.txt')
arquivo.salvar_txt(vetor3, './AEDII/aula_190825/data/vetor3.txt')
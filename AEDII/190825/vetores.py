import gerador_de_numeros
import arquivo

gerador_de_numeros.iniciar_gerador(semente=21) # escolhi minha idade 
vetor1 = gerador_de_numeros.gerar_varios_numeros(100)
arquivo.salvar_txt(vetor1, './AEDII/190825/vetor1.txt')

gerador_de_numeros.iniciar_gerador(semente=1805) # diferente para dar numeros diferentes na 'sequencia pseudo-aleatoria' (escolhi dia e mes do meu aniversario)
vetor2 = gerador_de_numeros.gerar_varios_numeros(1000)
arquivo.salvar_txt(vetor2, './AEDII/190825/vetor2.txt')

gerador_de_numeros.iniciar_gerador(semente=2004) # diferente para dar numeros diferentes na 'sequencia pseudo-aleatoria' (escolhi ano que nasci)
vetor3 = gerador_de_numeros.gerar_varios_numeros(10000)
arquivo.salvar_txt(vetor3, './AEDII/190825/vetor3.txt')
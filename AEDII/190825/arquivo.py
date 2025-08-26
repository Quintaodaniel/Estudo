def salvar_txt(vetor: list, nome_do_arquivo: str):
    with open(nome_do_arquivo, 'w') as arquivo:
        for numero in vetor:
            arquivo.write(f"{numero}\n")

def ler_txt(nome_do_arquivo: str) -> list:
    vetor = []
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            for linha in arquivo:
                numero = int(linha.strip())
                vetor.append(numero)
    except FileNotFoundError:
        print(f" -> ERRO: O arquivo '{nome_do_arquivo}' não foi encontrado.")
    
    return vetor
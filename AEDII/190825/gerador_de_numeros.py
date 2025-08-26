# Gerador de números pseudo-aleatórios

# 1. (constantes)
MULTIPLICADOR = 1664525
INCREMENTO = 1013904223
MODULO = 2**32

# 2. A "memória" do gerador
ultimo_numero_gerado = 0

def iniciar_gerador(semente):
    """Define o 'ponto de partida' do gerador."""
    global ultimo_numero_gerado
    ultimo_numero_gerado = semente

def gerar_proximo_numero_base():
    """Gera o próximo número grande da sequência e atualiza a memória."""
    global ultimo_numero_gerado
    proximo = (MULTIPLICADOR * ultimo_numero_gerado + INCREMENTO) % MODULO
    ultimo_numero_gerado = proximo
    return proximo

def sortear_um_numero():
    """Sorteia um número FIXO no intervalo de 1 a 100."""
    numero_base = gerar_proximo_numero_base()
    return 1 + (numero_base % 100)

def gerar_varios_numeros(quantidade):
    """Gera uma quantidade específica de números e retorna uma lista com eles."""
    return [sortear_um_numero() for _ in range(quantidade)]
import random, time

def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == valor:
            return i, comparacoes
    return -1, comparacoes

def pesquisa_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

# Teste das buscas
lista = sorted(random.sample(range(1, 1001), 100))
valor = random.choice(lista)

inicio = time.time()
i_seq, c_seq = pesquisa_sequencial(lista, valor)
t_seq = time.time() - inicio

inicio = time.time()
i_bin, c_bin = pesquisa_binaria(lista, valor)
t_bin = time.time() - inicio

print("🔍 BUSCAS")
print(f"Valor procurado: {valor}")
print(f"Sequencial → índice={i_seq}, comparações={c_seq}, tempo={t_seq:.8f}s")
print(f"Binária → índice={i_bin}, comparações={c_bin}, tempo={t_bin:.8f}s")

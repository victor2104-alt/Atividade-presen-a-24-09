import random
import time

def ordenacao_selecao(lista):
    # Ordenação por seleção in-place
    n = len(lista)
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        # troca
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista

def quicksort(lista):
    # Quicksort recursivo (não-in-place) - simples e legível
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista)//2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

# Função auxiliar para medir tempo com réplica e estabilidade
def medir_tempo(func, dados, repetir=3):
    tempos = []
    resultado = None
    for _ in range(repetir):
        copia = dados.copy()
        t0 = time.perf_counter()
        resultado = func(copia)
        t1 = time.perf_counter()
        tempos.append(t1 - t0)
    return min(tempos), resultado  # usa o menor tempo das tentativas

# --- Teste com 1000 elementos (ajuste se estiver muito lento) ---
TAMANHO = 1000
# Se sua máquina for fraca, diminua TAMANHO para 500 ou 200
lista_original = random.sample(range(1, 10001), TAMANHO)

# Medir seleção (pode ser bem mais lento)
t_selecao, res_selecao = medir_tempo(ordenacao_selecao, lista_original, repetir=1)  # repetir=1 para seleção (mais lento)
# Medir quicksort
t_quick, res_quick = medir_tempo(quicksort, lista_original, repetir=3)
# Medir built-in sorted
t_sorted, res_sorted = medir_tempo(lambda x: sorted(x), lista_original, repetir=3)

# Verificações de correção
igual_selecao_sorted = res_selecao == res_sorted
igual_quick_sorted = res_quick == res_sorted

print("🔄 RESULTADOS DA ORDENAÇÃO (lista com {} elementos)".format(TAMANHO))
print(f"Seleção: {t_selecao:.6f}s  | resulta igual ao sorted()? {igual_selecao_sorted}")
print(f"Quicksort: {t_quick:.6f}s | resulta igual ao sorted()? {igual_quick_sorted}")
print(f"sorted(): {t_sorted:.6f}s")


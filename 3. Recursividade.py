def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])

# Teste
print("\n🧮 RECURSIVIDADE")
print(f"Fatorial(5): {fatorial(5)}")
print(f"Fibonacci(8): {fibonacci(8)}")
print(f"Soma da lista [1,2,3,4,5]: {soma_lista([1,2,3,4,5])}")
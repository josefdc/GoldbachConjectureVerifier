def es_primo(n):
    """Verifica si un número es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def genera_lista_primos(n):
    """Genera una lista de números primos hasta n."""
    return [i for i in range(2, n+1) if es_primo(i)]


def descomponer_en_primos(n, lista_primos):
    """Descompone un número par en dos números primos, si es posible."""
    for primo in lista_primos:
        if n - primo in lista_primos:
            return (primo, n - primo)
    return None


def verifica_goldbach_hasta(n):
    """Verifica la conjetura de Goldbach hasta un número n."""
    primos_hasta_n = genera_lista_primos(n)
    resultados = {}
    for i in range(4, n + 1, 2):  # Solo consideramos números pares.
        descomposicion = descomponer_en_primos(i, primos_hasta_n)
        if descomposicion:
            resultados[i] = descomposicion
        else:
            raise ValueError(f"La conjetura de Goldbach no se cumple para {i}!")
    return resultados


# Ejecución
resultados = verifica_goldbach_hasta(100)
resultados_formato = {k: f"{v[0]} + {v[1]}" for k, v in resultados.items()}
resultados_formato

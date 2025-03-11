import secrets

def obtener_paridad(num):
    return "par" if num % 2 == 0 else "impar"

def jugar_ronda():
    dado = secrets.randbelow(6) + 1  # 1-6
    moneda = "cara" if secrets.randbits(1) else "cruz"
    return dado, moneda

def analizar_apuesta(intentos):
    aciertos = sum(1 for _ in range(intentos) 
        if (lambda d, m: d > 3 and m == 'cara')(*jugar_ronda()))
    return aciertos, intentos - aciertos

def mostrar_estadisticas(aciertos, fallos):
    total = aciertos + fallos
    print(f"\n⚡ Aciertos: {aciertos} ({aciertos/total:.2%})")
    print(f"⚡ Fallos: {fallos} ({fallos/total:.2%})")
    print("Estrategia recomendada: Jugar" if aciertos > total*0.25 else "No jugar")

if __name__ == "__main__":
    resultados = analizar_apuesta(1500)
    mostrar_estadisticas(*resultados)
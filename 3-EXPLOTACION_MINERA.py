import math
import random

class Proyecto:
    def __init__(self):
        self.costo = 850_000
        self.riesgo = 0.6
        self.beneficio = lambda: math.log1p(200_000 * random.gauss(145, 15))
    
    def evaluar(self):
        if random.uniform(0, 1) > self.riesgo:
            return round(self.beneficio() * 0.7 - self.costo, 2)
        return -self.costo

def simular_mercado(iteraciones=10**4):
    balance = sum(Proyecto().evaluar() for _ in range(iteraciones))
    rentabilidad = balance / iteraciones
    umbral = (1 / (200_000 * 145 * 0.7 / 1e6)) * 100
    
    print("\n📊 Análisis Cuántico:")
    print(f"Rentabilidad esperada: ${rentabilidad/1e3:,.2f}k/operación")
    print(f"Umbral crítico: {umbral:.3f}%")
    print("Decisión: Invertir" if rentabilidad > 0 else "No invertir")

simular_mercado()
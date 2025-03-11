from numpy import random

class Jugador:
    def __init__(self):
        self.historial = []
    
    def decidir(self):
        if not self.historial:
            return random.choice(['A', 'B'])
        return 'B' if self.historial[-1] == 'A' else 'A'

def ejecutar_conflicto():
    jugadores = [Jugador(), Jugador()]
    decisiones = [j.decidir() for j in jugadores]
    
    recompensas = {
        ('A', 'A'): (2, 2),
        ('A', 'B'): (-1, 3),
        ('B', 'A'): (3, -1),
        ('B', 'B'): (0.5, 0.5)
    }
    
    for j, d in zip(jugadores, decisiones):
        j.historial.append(d)
    
    return decisiones, recompensas[tuple(decisiones)]

def main():
    d, r = ejecutar_conflicto()
    print(f"🔒 Decisiones: {d[0]} vs {d[1]}")
    print(f"🏆 Resultado: Jugador 1: {r[0]}pts | Jugador 2: {r[1]}pts")

if __name__ == "__main__":
    main()
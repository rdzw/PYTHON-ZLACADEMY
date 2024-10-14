import math

x1, y1 = map(float, input("Digite os valores: ").split())
x2, y2 = map(float, input("Digite os valores: ").split())

distancia = math.sqrt((x1 - x2)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")
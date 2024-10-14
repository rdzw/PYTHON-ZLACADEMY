import math

# Entrada dos valores
A, B, C = map(float, input("").split())

# Verificação se A é zero
if A == 0:
    print("Impossivel calcular")
else:
    # Cálculo do discriminante
    delta = B**2 - 4*A*C

    # Verificação do valor do discriminante
    if delta < 0:
        print("Impossivel calcular")
    else:
        # Cálculo das raízes
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)
        
        # Impressão dos resultados
        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")

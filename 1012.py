A, B, C = map(float, input("Digite os valores: ").split())

area = (1/2) * A * C

area_circulo = 3.14159 * C**2

area_trapezio = (A+B)*C/2

area_quadrado = B**2

are_retangulo = A*B

print(f"TRIANGULO: {area:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {are_retangulo:.3f}")


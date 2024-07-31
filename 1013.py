A, B, C = map(int, input("Digite os valores: ").split())

maior_AB = (A+B+abs(A-B))/2

if A > B:
    maior_ab = A
else:
    maior_ab = B

if maior_ab > C:
    maior_abc = maior_ab
else:
    maior_abc = C
    
print(f"{maior_abc} eh o maior")
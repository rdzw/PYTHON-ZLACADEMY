a,b = map(int, input("d:").split())
if (a==1):
    total= b*4
    print(f"Total: R$ {total:.2f}")
elif(a==2):
    total = b*4.50
    print(f"Total: R$ {total:.2f}")
elif(a==3):
    total= b*5
    print(f"Total: R$ {total:.2f}")
elif(a==4):
    total=b*2
    print(f"Total: R$ {total:.2f}")
else:
    total=b*1.5
    print(f"Total: R$ {total:.2f}")




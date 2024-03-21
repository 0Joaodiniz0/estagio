def fibonacci (numero):
    a = 0
    b = 1
    while b < numero:
        a,b = b, a+b
    
    if b == numero:
        return True
    else:
        return False
    
numero = int(input("Digite um numero:"))

if fibonacci(numero):
    print("Faz parte da sequência de fibonacci")
else:
    print("Não faz parte da sequência de fibonacci ")



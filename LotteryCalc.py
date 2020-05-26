import os

def fatorial(n):
    num = int(n)
    result = 1
    for i in range (1,num+1):
        result *= i
    if (num == 0):
        result = 1
    else:
        return result

def combinacao(n1,n2):
    result = fatorial(n1)/(fatorial(n1-n2)*fatorial(n2))
    return result

def coeficiente(n1,n2,n3,n4):
    if (n3 == n2):
        coef1 = 1
    else:
        coef1 = combinacao(n3,n4)
    if (n4 == n2):
        coef2 = 1
    else:
        coef2 = combinacao(n1-n3,n2-n4)
    result = coef1*coef2
    return result

sair = False
while (sair == False):
    os.system("clear")
    print("CALCULADORA LOTERICA\n")
    n1 = 0
    while ((n1 <= 0) | (n1 == "")):
        n1 = int(input("Insira a quantidade total de dezenas disponíveis: "))
    n2 = n1+1
    while ((n2 >= n1) | (n2 <= 0) | (n2 == "")):
        n2 = int(input("Insira a quantidade de dezenas sorteadas: "))
    n3 = n1+1
    while ((n3 > n1) | (n3 <= 0) | (n3 == "")):
        n3 = int(input("Insira a quantidade de dezenas apostadas: "))
    n4 = n2+1
    while ((n4 > n2) | (n4 < 0) | (n4 == "")):
        n4 = int(input("Insira o número de dezenas acertadas para premiação mínima: "))
    print("\nSORTEIO DE",int(n2),"dezenas de 01 a",int(n1),":")
    for j in range(n2,n3+1,1):
        print("\nAposta de",int(j),"DEZENAS: ")
        for i in range(n2,n4-1,-1):
            fator = combinacao(n1,n2)
            coef = coeficiente(n1,n2,j,i)
            result = fator / coef
            print(int(i),"acertos = 1 /",round(result,1),"\n  (coeficiente =",int(coef),"x)")
    if (input("Deseja sair? (S/N)").lower() == "s"):
        sair = True

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

def opcao1():
    global jogo, n1, n2, n4
    jogo = "MEGASENA"
    n1 = int(60)
    n2 = int(6)
    n4 = int(4)
    
def opcao2():
    global jogo, n1, n2, n4
    jogo = "QUINA"
    n1 = int(80)
    n2 = int(5)
    n4 = int(2)
    
def opcao3():
    global jogo, n1, n2, n4
    jogo = "LOTOFACIL"
    n1 = int(25)
    n2 = int(15)
    n4 = int(12)
    
def default():
    global n1, n2, n4
    n1 = 0
    while ((n1 <= 0) | (n1 == "")):
        n1 = int(input("Insira a quantidade total de dezenas disponíveis: "))
    n2 = n1+1
    while ((n2 >= n1) | (n2 <= 0) | (n2 == "")):
        n2 = int(input("Insira a quantidade de dezenas sorteadas: "))
    n4 = n2+1
    while ((n4 > n2) | (n4 < 0) | (n4 == "")):
        n4 = int(input("Insira o número de dezenas acertadas para premiação mínima: "))

sair = False
while (sair == False):
    print("CALCULADORA LOTERICA\n")
    print("1 - Megasena")
    print("2 - Quina")
    print("3 - Lotofácil")
    switch = {
        "1": opcao1,
        "2": opcao2,
        "3": opcao3
    }
    jogo = "não definido"
    case = switch.get(input("\nDigite uma opcao (1, 2 ou 3): "), default)
    os.system("clear")
    case()
    n3 = n1+1
    while ((n3 > n1) | (n3 <= n4) | (n3 == "")):
        n3 = int(input("Insira a quantidade de dezenas apostadas: "))
    print("\nCalculando probabilidade para ",jogo)
    print("Sorteio de",int(n2),"dezenas de 01 a",int(n1),":")
    for j in range(n2,n3+1,1):
        print("\nAposta de",int(j),"DEZENAS: ")
        for i in range(n2,n4-1,-1):
            fator = combinacao(n1,n2)
            coef = coeficiente(n1,n2,j,i)
            result = fator / coef
            print(int(i),"acertos = (1 /",round(result,1),")        coeficiente =",int(coef),"x")	
    if (input("\nDeseja sair? (S/N)").lower() == "s"):
        sair = True
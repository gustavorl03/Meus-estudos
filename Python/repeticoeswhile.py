#sexo = ""
#sexo = str(input("Informe seu sexo: [M/F] ")).strip().#upper()[0]
#while sexo not in "FfMm":
#    sexo = str(input("Dados inválidos. Por favor, informe o seu sexo: [M/F] ")).strip().upper()[0]
#print("Sexo {} registrado com sucesso!".format(sexo))

#from random import randint
#computador= randint(0,10)
#tent = 0
#tent1 = 0
#tent2 = 0
#print("Sou seu computador...")
#print("Acabei de pensar em um número entre 0 e 10.")
#print("Será que você consegue adivinhar qual foi?")
#n1= int(input("Qual o seu palpite? "))
#while n1 != computador:
#    if computador > n1:
#        print("Mais... Tente mais uma vez.")
#        n1= int(input("Qual o seu palpite? "))
#        tent1 = tent1 + 1
#    else:
#        print("Menos... Tente mais uma vez.")
#        n1= int(input("Qual o seu palpite? "))
#        tent2 = tent2 + 1   
#tent = tent1 + tent2
#print("Acertou com {} tentativas. Parabéns!".format(tent))

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
cont = 0

while cont != 5:
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    cont = int(input(">>>>>>>> Qual é a sua opção? "))

    if cont == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} + {n2} é {soma}")
    elif cont == 2:
        multi = n1 * n2
        print(f"A multiplicação entre {n1} X {n2} é {multi}")
    elif cont == 3:
        if n1 > n2:
            print(f"O {n1} é maior que o {n2}")
        elif n2 > n1:
            print(f"O {n2} é maior que o {n1}")
        else:
            print(f"Não existe número maior, os dois são iguais.")
    elif cont == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif cont == 5:
        print("Fim do programa!")
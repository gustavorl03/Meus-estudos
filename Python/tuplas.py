#cont = ("zero", "um", "dois", "três", "quatro"
#        "cinco", "seis", "sete", "oito", "nove"
#        "dez", "onze", "doze", "treze", "catorze",
#        "quinze", "dezesseis", "dezessete", "dezoito",
#        "dezenove", "vinte")
#while True:
#    num = int(input("Digite um número entre 0 e 20: "))
#    if 0 <= num <= 20:
#        break
#    print("Tente novamente\n", end="")
#print(f"Você digitou o número {cont[num]}")

#--------------------------------------------------------

#n = 0
#num = ( int(input("Digite um número: ")),
#        int(input("Digite outro número: ")),
#        int(input("Digite mais um número: ")), 
#        int(input("Digite o último número: ")))
#print(f"Você digitou os valores {num}")
#print(f"O valor 9 apareceu {num.count(9)} vezes")
#if 3 in num:
#    print(f"O valor 3 apareceu na {num.index(3)+1} posição!")
#else:
#     print("O valor 3 não foi digitado!")
#print("Os valores pares digitados foram ", end = "")
#for n in num:
#    if n % 2 == 0:
#          print(n, end=" ")

#--------------------------------------------------------

listagem = ("Lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Trasnferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)
print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-" * 40)

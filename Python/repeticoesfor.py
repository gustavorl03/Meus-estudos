#for c in range(1,51,2):
#    print(c + 1)
#print("Fim!")

#s = 0
#for c in range (1, 501, 2):
#    if c % 3 == 0:
#        s = c + s
#print("A soma dos múltiplos de 3, que vai de 1 até 500 é igual a {}".format(s))

#n1 = int(input("Digite um número do qual você queira saber a sua tabuada: "))
#tabu = 0
#for c in range (1,11):
#    tabu = n1 * c
#    print("{} X {} = {}".format(n1,c, tabu))
#print("Fim!")

somaidade = 0
mediaidade = 0
nomevelho = ""
maioridadevelho = 0
totmulher = 0

for n in range (1,5):
    print("\n---- {} PESSOA ----".format(n))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade = somaidade + idade
    if n == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher = totmulher + 1

mediaidade = somaidade / 4
print("\nA média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("Ao todo têm {} mulheres com menos de 20 anos".format(totmulher))








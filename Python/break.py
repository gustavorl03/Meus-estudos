#cont = 0
#number = 0
#soma = 0
#while True:
#    number = int(input("Digite um número(999 para parar): "))
#    if number == 999:
#        break
#    else:
#        cont = cont + 1
#       soma = soma + number
#print(f"Você digitou {cont} números, e a soma de todos esses números é igual a {soma} !")

#---------------------------------------------------------------

#c = 0
#resul = 0
#while True:
#    num = int(input("Quer ver a tabuada de qual valor? "))
#    if num > 0:
#        print("----------------------------------")
#        for c in range(1,11):
#            resul = num * c
#            print(f"{num} X {c} = {resul}")
#    else:
#        break
#    print("----------------------------------")
#print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")

#---------------------------------------------------------------

#tothomem = 0
#totidade = 0
#totmulher = 0
#while True:
#    print("--------------------------------")
#    print(" CADASTRE UMA PESSOA ")
#    print("--------------------------------")
#
#    idade = int(input("Idade: "))
#    if idade > 18:
#        totidade = totidade + 1
#
#    sexo = str(input("Sexo[M/F]: "))
#   while sexo not in "MF":
#       sexo = str(input("Sexo[M/F]: "))
#    if sexo == "M":
#       tothomem = tothomem + 1
#
#    print("--------------------------------")
#    conti = str(input("Quer continuar?[S/N] "))
#    while conti not in "SN":
#        conti = str(input("Quer continuar?[S/N] "))
#    if conti =="N":
#        break
#
#    if idade > 20 and sexo == "F":
#        totmulher = totmulher + 1    
#        
#print("======= FIM DO PROGRAMA =========")
#print(f"Ao todo temos {tothomem} homens cadastrados.")
#print(f"Total de pessoas com mais de 18 anos: {totidade}")
#print(f"E temos {totmulher} mulheres com menos de 20 anos.")

#----------------------------------------------------------------------------

print("---------------------------------------------------------")
print("                    LOJA SUPER BARATÃO                   ")
print("---------------------------------------------------------")
tot = 0
totmenor == 0
totmaior = 0
menorprod = ""
while True:
    nome = str(input("Nome do produto: "))
    valor = float(input("Preço: R$ "))
    tot = tot + valor

    if valor < totmenor:
        totmenor == valor
        menorprod == nome

    if valor > 1000 :
        totmaior = totmaior + 1

    cont = str(input("Quer continuar?[S/N] "))
    while cont not in "SN":
        cont = str(input("Quer continuar?[S/N] "))
    if cont == "N":
        break
print(f"O total da compra foi de R${tot}")
print(f"Temos {totmaior} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi a {menorprod} que custa R${totmenor}")
    
#----------------------------------------------------------------------------------    
             
#teste = list()
#teste.append("Gustavo")
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = "Maria"
#teste[1] = 22
#galera.append(teste[:])
#print(galera)


#galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
#for p in galera:
#    print(f"{p[0]} tem {p[1]} anos de idade! ")


#galera = list()
#dado = list()
#for c in range (0,3):
#    dado.append(str(input("Nome: ")))
#    dado.append(int(input("Idade: ")))
#    galera.append(dado[:])
#    dado.clear()
#print(galera)


#peso = list()
#dados = list()
#quant = 1
#mai = men = 0
#while True:
#    dados.append(str(input("Nome: ")))
#    dados.append(float(input("Peso: ")))
#    if len(peso) == 0:
#        mai = men = dados[1]
#    else:
#        if dados[1] > mai:
#           mai = dados[1]
#        if dados[1] < men:
#            men = dados[1]
#    peso.append(dados[:])
#    dados.clear()
#    res = str(input("Quer continuar [S/N]? "))
#    if res in "nN":
#        break
#    else:
#        quant = quant + 1
#print("-=" * 30)
#print(f"Ao todo, você cadastrou {quant} pessoas.")
#print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
#for p in peso:
#    if p[1] == mai:
#        print(f"[{p[0]}] ", end="")
#print()
#print(f"O menor peso foi de {men}Kg. Peso de ", end="")
#for p in peso:
#    if p[1] == men:
#        print(f"[{p[0]}] ", end="")
#print()


#valores = [ [], []]
#valor = 0
#for c in range(1,8):
#    valor = (int(input(f"Digite o {c}o. valor: ")))
#    if valor % 2 == 0:
#        valores[0].append(valor)
#    else:
#        valores[1].append(valor)
#print("-=" * 30)
#print(f"Os valores pares digitados foram: {valores[0]}")
#print(f"Os valores ímpares digitados foram: {valores[1]}")


ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([ nome, [nota1,nota2], media])
    res = str(input("Quer continuar [S/N]? "))
    if res in "nN":
        break
print("-=" * 30)

print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    opc = int(input("Mostras notas de qual aluno(999 interompe): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")
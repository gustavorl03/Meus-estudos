#num = [2,5,9,1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2,0)
#num.pop(4)
#if 5 in num:
#    num.remove(5)
#else:
#    print("Não achei o número 5")
#print(num)
#print(f"Essa lista tem {len(num)} elementos! ")

#valores = []
#for cont in range(0,5):
#    valores.append(int(input("Digite um valor: ")))
#for c, v in enumerate(valores):
#    print(f"Na posição {c + 1} encontrei o valor {v}")
#print("Cheguei ao final da lista.")

#a = [2,3,4,7]
#b = a[:]
#b[2] = 8
#print(a)
#print(b)

#--------------------------------------------------------

#valores = []
#maiorvalor = 0
#menorvalor = 0
#posicaomaior = 0
#posicaomenor = 0

#for c in range(0,5):
#    valores.append(int(input(f"Digite um valor para a Posição {c}: ")))
#    if c == 0:
#        maiorvalor = valores[c]
#        menorvalor = valores[c]
#    
#    if valores[c] > maiorvalor:
#        maiorvalor =  valores[c]
#        posicaomaior = c
#        
#    if valores [c] < menorvalor:
#        menorvalor = valores[c]
#        posicaomenor = c
# 
#print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
#print(f"Você digitou os valores {valores}")
#print(f"O maior valor digitado foi {maiorvalor} na posição {posicaomaior}...")
#print(f"O menor valor digitado foi {menorvalor} na posição {posicaomenor}...")

#--------------------------------------------------------

#num = []
#while True:
#    num.append(int(input(("Digite um número: "))))
#    res = str(input("Quer continuar [S/N]? "))
#    if res in "nN":
#        break
#print("-=" * 30)
#print(f"Você digitou {len(num)} elementos")
#num.sort(reverse=True)
#print(f"Os valores em ordem decrescente são {num}")
#if 5 in num:
#    print("O valor 5 faz parte da lista!")
#else:
#    print("O valor 5 não faz parte da lista!")

#--------------------------------------------------------

valores = []
valorpar = []
valorimpar = []
while True:
    valores.append(int(input(("Digite um número: "))))
    res = str(input("Quer continuar [S/N]? "))
    if res in "nN":
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        valorpar.append(v)
    else:
        valorimpar.append(v)
print("-=" * 30)
print(f"A lista completa é {valores}")
print(f"A lista de pares é {valorpar}")
print(f"A lista de ímpares é {valorimpar}")

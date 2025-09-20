X1= float(input("Digite o primeiro valor: "))
X2= float(input("Digite o segundo valor: "))

soma = X1 + X2
subtra = X1 - X2
multi = X1 * X2
div= X1 / X2

print ("Escolha a operação que deseja fazer:") 
print("")
print("1)SOMA")
print("2)SUBTRAÇÃO")
print("3)MULTIPLICAÇÃO")
print("4)DIVISÃO")

print("")
resp= int(input(""))

if (resp==1):
    print(soma) 
elif(resp==2):
    print(subtra)
elif(resp==3):
    print(multi)
else:
    print(div)


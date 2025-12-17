#Estrutas Condicionais em Python
#Estruturas condicionais permitem que você execute diferentes blocos de código com base em certas

idade = int(input("Qual sua idade? "))

if (idade >= 18):
    print("Você é maior de idade.")


#se eu quiser adicionar mais condições
else: # se o if não for verdadeiro
    print("Você é menor de idade.") 


# mais de duas  condições
#elif - else if

opcao = int(input("Escolha uma opção 1,2,3: "))

if opcao == 1: 
    print("Você escolheu a opção 1")
elif opcao == 2: #se o if não for verdadeiro, verifica essa condição
    print("Você escolheu a opção 2")
elif opcao == 3: #se o if e o primeiro elif não forem verdadeiros, verifica essa condição
    print("Você escolheu a opção 3")
##pode adicionar quantos elif quiser

#Pode ter um if dentro de um outro if - aninhamento

if (idade >= 18):
    if (idade >= 18):
        print("Você é um idoso maior de idade.")
    else:
        print("Você é um adulto maior de idade.")
else: 
    print("Você é menor de idade.") 

#if ternário - forma simplificada de escrever um if-else

status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
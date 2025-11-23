#Função Input - Entrada de dados pelo usuário

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"Olá, {nome}! ")
print(f"Você tem {idade} anos.")

# Exibir valores formatados
sobrenome = input("qual seu sobrenome? ")
print(nome,sobrenome)
print(nome,sobrenome,end="!\n")  #modifica o final da impressão
print(nome,sobrenome,end="...\n")
print(nome,sobrenome,sep="#") #modifica o separador entre os valores


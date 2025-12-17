# Métodos Strings

#Maicúsculas
texto = "hello world"
print(texto.upper())  #HELLO WORLD
#Minúsculas
print(texto.lower())  #hello world
#Primeira letra maiúscula
print(texto.title())  #Hello World

#Remore espaços em branco
texto2 = "   hello world!   "

print(texto2.strip())  #remove espaços em branco dos dois lados
print(texto2.lstrip()) #remove espaços em branco da esquerda
print(texto2.rstrip()) #remove espaços em branco da direita

#Juntar e Centralizar

texto3 = "hello"
print(texto3.center(20, "-")) #centraliza o texto em um campo de 20 caracteres, preenchendo com '-'
print(".".join(texto3)) #junta os elementos da lista com '.' entre eles
print("-".join(["2025", "12", "17"])) 
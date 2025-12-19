#Tupla ---

#imutavel - não pode ser alterada após a criação
#definida por parênteses ()
#Usada para agrupar dados relacionados


#igual a listas, mas não podem ser modificadas!!

#Criando tuplas
pessoa = ("João", 30, "Engenheiro",)
frutas = tuple(["maçã", "banana", "laranja"]) 
print(pessoa)
print(frutas)

# se for de um elemento, colocar uma vírgula no final
tupla_um_elemento = (42,)

#Como acessar elementos em uma tupla
print("Nome:", pessoa[0])  #Acessa o primeiro elemento
print("Idade:", pessoa[1])  #Acessa o segundo elemento  
print("Profissão:", pessoa[-1])  #Acessa o último elemento

#Tuplas aninhadas

matriz = ((1, 2, 3),
           (4, 5, 6), 
           (7, 8, 9))
print("Elemento na linha 2, coluna 3:", matriz[1][2])  #Acessa o elemento 6

#fatiamento de tuplas
sub_tupla = frutas[0:2]  #Pega os dois primeiros elementos
print("Sub-tupla:", sub_tupla)

for frutas in frutas:
    print("Fruta:", frutas)

#Metodos de tuplas --- 

'Count - conta quantas vezes um elemento aparece na tupla'
numeros = (1, 2, 3, 2, 4, 2, 5)
contagem_de_dois = numeros.count(2)
print("Contagem de '2':", contagem_de_dois)

'Index - retorna o índice da primeira ocorrência de um elemento'
indice_de_quatro = numeros.index(4)
print("Índice de '4':", indice_de_quatro)
print("Elemento na posição 4:", numeros[4])
#Lista 

# Criar Lista --- 

lista = []  # Lista vazia
print(type(lista))

#Exemplos de listas
lista1 = [1, 2, 3, 4, 5]  # Lista de inteiros
lista2 = ["maçã", "banana", "laranja"]  # Lista de strings
lista3 = [1, "dois", 3.0, True]  # Lista mista
lista4 = list("Python")  # Converter string em lista de caracteres

print("Lista 1:", lista1)
print("Lista 2:", lista2)           
print("Lista 3:", lista3)
print("Letras 4:", lista4)

#Acessar elementos da lista---

print(lista2[2])  # Acessa o terceiro elemento (índice 2)
print(lista3[0:3])  # Acessa os três primeiros elementos
print(lista4[-1])  # Acessa o último elemento
print(lista1[-2]) # Acessa o penúltimo elemento
print(lista2[::])  # Acessa do segundo elemento até o final
#Lista dentro de lista ---

lista_aninhada = [1, 2, [3, 4], 5]
matriz = [[1, 2], [3, 4]]  # Acessa a sub-lista [3
 
#Iterar uma lista ---

contador = 1
for fruta in lista2:
    print(f"Fruta {contador}:", fruta)
    contador += 1

lista_de_numeros = list(range(1, 10))
lista_par = []
for numero in lista_de_numeros:
    if numero % 2 == 0: 
        lista_par.append(numero)
    
print(lista_par)
lista_par_2 = [numero for numero in lista_de_numeros if numero % 2 == 0]

#Modificando uma lista ---

nova_lista = [] 
for numero in lista_de_numeros:
    nova_lista.append(numero * 2)

print("Lista original:", lista_de_numeros)
print("Lista modificada:", nova_lista)

nova_lista2 = [numero * 2 for numero in lista_de_numeros]
print("Lista modificada 2:", nova_lista2)

#MEtodos de listas ---

#Append - adiciona um elemento ao final da lista ---
lista2.append("uva")
print("Após append:", lista2)

#Clear - remove todos os elementos da lista ---

lista1.clear()
print("Após clear:", lista1)

#copy - cria uma cópia da lista ---
copia_lista2 = lista2.copy()
print("Cópia da lista2:", copia_lista2)
#usado para evitar que alterações na cópia afetem a lista original

#Juntar duas listas - extend ---
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)
print("Após extend:", lista_a)

#index - retorna o índice do primeiro elemento com o valor especificado ---
indice_laranja = lista2.index("laranja")
print("Índice de laranja:", indice_laranja)
print(lista2[2])

#pop - remove e retorna o elemento no índice especificado (ou o último se nenhum índice for fornecido) ---
ultimo_elemento = lista2.pop()
print("Elemento removido com pop:", ultimo_elemento)
print("Após pop:", lista2) #igual uma pilha (FIFO - First In First Out)
#pop pode tirar o indice especifico
segundo_elemento = lista2.pop(1)
print("Segundo elemento removido com pop:", segundo_elemento)
print("Após pop do segundo elemento:", lista2)


#remove - remove a primeira ocorrência do valor especificado ---
lista2.remove("maçã")
print("Após remove maçã:", lista2)

#reverte - inverte a ordem dos elementos na lista ---
lista_b.reverse()
print("Após reverse:", lista_b)

#sort - ordena os elementos da lista em ordem crescente (ou decrescente se especificado) ---
lista_c = [5, 2, 9, 1, 5, 6]
lista_c.sort()
print("Após sort:", lista_c)
lista_c.sort(reverse=True)
print("Após sort decrescente:", lista_c)

lista_e = ["cs", "maçã do amor", "2", "abc", "banana"]
lista_e.sort(key=lambda x: len(x))
print("Após sort por tamanho da string:", lista_e)

lista_e = ["cs", "maçã do amor", "2", "abc", "banana"]
lista_e.sort(key=lambda x: len(x),reverse=True)
print("Após sort por tamanho da string decrescente:", lista_e)

#Len - retorna o número de elementos na lista ---
tamanho_lista2 = len(lista2)
print("Tamanho da lista2:", tamanho_lista2)

#Sorted - retorna uma nova lista ordenada sem modificar a original ---
lista_d = [3, 1, 4, 1, 5, 9]
lista_ordenada = sorted(lista_d)
#Conjuntos em Python
#Conjuntos (sets) são coleções não ordenadas de elementos únicos. 

#elimina elementos duplicados automaticamente

conjunto1 = set([1,2,2,3,4,4,5])  # cria um conjunto a partir de uma lista com elementos duplicados
print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

conjunto2 = set(['maçã', 'banana', 'maçã', 'laranja'])  # cria um conjunto a partir de uma lista de strings com elementos duplicados
print(conjunto2)
#Não se confia na ordem dos elementos
conjunto3 = set([5, 3, 1, 4, 2])
print(conjunto3)  # Saída: {1, 2, 3, 4, 5} (a ordem pode variar)

#Não tem índices, não é possível acessar elementos por posição
#conjunto[0]  # Isso geraria um erro
#precisa trasnformar em lista ou tupla para acessar por índice

#Enumerate

carros = {'fusca', 'gol', 'celta'} #conjutno de carros definido por chaves {}
for indice in enumerate(carros):
    print(indice)  # Imprime tuplas com índice e valor

#Metodos Set    

#union (união) - combina dois conjuntos, removendo duplicatas
A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print("União de A e B:", C)  # Saída: {1, 2, 3, 4, 5}

#intersection (interseção) - retorna elementos comuns a ambos os conjuntos
D = A.intersection(B)
print("Interseção de A e B:", D)  # Saída: {3}

#Diference (diferença) - retorna elementos que estão em um conjunto (nesse caso A), mas não no outro (nesse caso B)
E = A.difference(B) 
print("Diferença de A e B (A - B):", E)  # Saída: {1, 2}

#symmetric_difference (diferença simétrica) - retorna elementos que estão em um dos conjuntos, mas não em ambos
F = A.symmetric_difference(B)
print("Diferença simétrica de A e B:", F)  # Saída: {1, 2, 4, 5}

#issubset (subconjunto) - verifica se todos os elementos de um conjunto estão presentes em outro conjunto
G = {1, 2}
print("G é subconjunto de A:", G.issubset(A))  # Saída: True

#Ao contrario:
#irsuperset (superconjunto) - verifica se um conjunto contém todos os elementos de outro conjunto
print("A é superconjunto de G:", A.issuperset(G))  # Saída: True

#isdisjoint (disjunto) - verifica se dois conjuntos não têm elementos em comum
H = {6, 7}
print("A e H são disjuntos:", A.isdisjoint(H))  # Saída: True - nada é igual

#add - adiciona um elemento ao conjunto
A.add(6)
print("A após adicionar 6:", A)  # Saída: {1, 2, 3, 6}
A.add(6)  # Tentativa de adicionar 6 novamente
print("A após tentar adicionar 6 novamente:", A)  # Saída: {1, 2, 3, 6} - não muda

#clear - remove todos os elementos do conjunto
A.clear()
print("A após clear():", A)  # Saída: set() - conjunto vazio

#copy - cria uma cópia do conjunto
B_copy = B.copy()
print("Cópia de B:", B_copy)  # Saída: {3, 4, 5}

#discard - remove um elemento do conjunto, se estiver presente
B.discard(3)
print("B após descartar 3:", B)  # Saída: {4, 5}

#pop - remove e retorna um elemento arbitrário do conjunto
elemento_removido = B.pop()
print("Elemento removido de B:", elemento_removido)
print("B após pop():", B)  # Saída: conjunto B sem o elemento removido

#remove - remove um elemento do conjunto; gera um erro se o elemento não estiver presente
#B.remove(10)  # Isso geraria um erro, pois 10 não está em B

#discard vs remove
##discard não gera erro se o elemento não existir

#len - retorna o número de elementos no conjunto
tamanho_B = len(B)

#in - verifica se um elemento está presente no conjunto
print("5 está em B:", 5 in B)  # Saída: True
print("10 está em B:", 10 in B)  # Saída: False
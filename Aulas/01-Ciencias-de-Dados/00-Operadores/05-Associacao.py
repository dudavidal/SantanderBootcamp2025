#Oepradores de Associacao são usados para verificar a presença ou ausência de um valor em uma sequência (como listas, tuplas, strings, etc.) e retornam um valor booleano (True ou False).

#Operador in - verifica se um valor está presente em uma sequência
frutas = ["maçã", "banana", "laranja"]
print(f"'banana' in frutas ->", 'banana' in frutas)  # Saída: True
print(f"'uva' in frutas ->", 'uva' in frutas)      # Saída: False

#Operador not in - verifica se um valor não está presente em uma sequência
print(f"'uva' not in frutas ->", 'uva' not in frutas)  # Saída: True
print(f"'maçã' not in frutas ->", 'maçã' not in frutas)  # Saída: False

frase = "Eu gosto de programar em Python"
print(f"'Python' in frase ->", 'Python' in frase)  # Saída: True
print(f"'Java' not in frase ->", 'Java' not in frase)  # Saída: True


#Ou seja verifica se um elemento pertence ou não a uma coleção de elementos.
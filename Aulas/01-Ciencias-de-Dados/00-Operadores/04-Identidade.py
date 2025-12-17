#Operadores de Identidade são usados para comparar objetos e verificar se são o mesmo objeto na memória.
#Operador is - verifica se dois objetos são o mesmo objeto na memória
#Operador is not - verifica se dois objetos são diferentes objetos na memória

a = [1, 2, 3]
b = [1, 2, 3]
c = a
d = "lista"

print(f"a is b: {a is b}")      # False
print(f"a is c: {a is c}")      # True
print(f"a is not b: {a is not b}")  # True
print(f"a is d: {a is d}")  # False
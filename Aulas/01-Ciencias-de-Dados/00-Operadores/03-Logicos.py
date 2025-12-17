#Operadores Logicos são usados para combinar expressões booleanas e retornam um valor booleano (True ou False) com base na lógica aplicada.

#Operador AND (e)
a = True
b = False
print(f"Operador AND: {a} and {b} ->", a and b)  # Saída: False
print(f"Operador AND: {a} and {a} ->", a and a)  # Saída: True

#Operador OR (ou)
print(f"Operador OR: {a} or {b} ->", a or b)  # Saída: True
print(f"Operador OR: {b} or {b} ->", b or b)  # Saída: False

#Operador NOT (não)
print(f"Operador NOT: not {a} ->", not a)  # Saída: False
print(f"Operador NOT: not {b} ->", not b)  # Saída: True   

#Combinação de operadores lógicos
x = 10
y = 5
z = 15

print(f" ({x} > {y}) and ({x} < {z}) ->", (x > y) and (x < z))  # Saída: True
print(f" ({x} < {y}) or ({x} < {z}) ->", (x < y) or (x < z))  # Saída: True

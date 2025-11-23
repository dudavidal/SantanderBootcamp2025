#Conversao de tipos ------------------------

#Numerico para String

preco = 10.50
idade = 25

print(str(preco))
print(str(idade))

#String para Numerico

altura = "1.75"
peso = "70"
print(float(altura))
print(int(peso))

#Numerico para Booleano 

print(bool(1))  #True
print(bool(0))  #False

#inteiro para Float e vice-versa

print(float(idade))  #25.0
print(int(preco))    #10

#A vezes a conversão pode não ser possível
#O numero deve estar em um formato válido

#print(int("Python"))  #Erro

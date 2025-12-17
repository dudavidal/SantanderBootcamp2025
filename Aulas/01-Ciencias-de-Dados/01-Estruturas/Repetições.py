#Repetiçãp em pyhton

a = int(input("Digite um número: "))

#se eu quero ver duas vezes o número
#print(a)
#print(a)

#mas se eu quiser ver 10 vezes?
#print(a)
#print(a)
# ...

#para isso usamos estruturas de repetição

#for - para um número determinado de repetições
n = int(input("Quantas vezes quer ver o número?"))
for i in range(n):
    print(a)

#Exemplo mais complexo

texto = input("Digite um texto: ")
print("quantas vogais tem?")
contador = 0

for letra in texto:
    if letra.lower() in "aeiou":
        print(letra)
        contador += 1
print(f"O texto tem {contador} vogais.")

#range - função que gera uma sequência de números
print("Números de 0 a 9:")
lista = range(10)  #gera números de 0 a 9
print(list(lista))

#range + for 

for numero in range(0,10): 
    print(numero, end=" ")  #imprime números de 0 a 9 na mesma linha

#pulando na sequência 

for numero in range(0,50,5): #de 0 a 50, pulando de 5 em 5
    print(numero,end=" ")

#WHILE - enquanto uma condição for verdadeira, repete o bloco de código

opcao = -1
while opcao != 0:
    opcao = int(input("\nDigite um número (0 para sair): "))
    print(f"Você digitou {opcao}")
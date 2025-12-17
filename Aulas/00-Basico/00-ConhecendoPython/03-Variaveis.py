#Variaveis em Python
#Nomes que gaurdam objetos na memória que podem ser variaveis ou constantes

nome = "Leo"          #String
idade = 20              #Inteiro
altura = 1.75          #Float

print(f"Meu nome é {nome}, Tenho {idade} anos, e {altura} m de altura")


nome = "Amora"          #String
idade = 21              #Inteiro
altura = 1.65         #Float

print(f"Meu nome é {nome}, Tenho {idade} anos, e {altura} m de altura")

#Variaveis são mutáveis, ou seja, podem mudar de valor e tipo
#Em python não é necessário declarar o tipo da variável
#O tipo é inferido automaticamente pelo valor atribuído

idade = "12"  #Agora idade é uma string
print(f"Idade como string: {idade}")

#BOAS PRATICAS

#snake_case para nomes de variaveis e funções
minha_variavel = 10

#Nomes sugestivos
idade_do_usuario = 25

#Nome de constantes em MAIUSCULO
PI = 3.14159
BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'ES']

#Pode escrever na mesma linha
a, b, c = 1, 2, 3

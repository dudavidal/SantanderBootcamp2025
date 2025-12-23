#Funções
#tem parametros de entrada
#retornam um valor
#podem não retornar nada

def saudacao(nome):  #definindo a função com um parâmetro de entrada
    """Função que recebe um nome e imprime uma saudação."""
    print(f"Olá, {nome}!")  #imprime a saudação
    #não retorna nada

saudacao("Maria")  #chamando a função com o argumento "Maria"

#respeitar ordem dos parametros
def soma(a, b):
    """Função que retorna a soma de dois números."""
    return a + b  #retorna a soma

resultado = soma(3, 5)  #chamando a função e armazenando o resultado

#argumentos nomeados
resultado2 = soma(b=10, a=20)  #chamando a função com argumentos nomeados
print("Resultado da soma:", resultado)
print("Resultado da soma com argumentos nomeados:", resultado2)

#Args e kwargs
def funcao_exemplo(*args, **kwargs):
    """Função que demonstra o uso de *args e **kwargs."""
    print("Argumentos posicionais (args):", args)
    print("Argumentos nomeados (kwargs):", kwargs)

#args tupla de argumentos posicionais
#kwargs dicionario de argumentos nomeados

def exibir_poema(data_extenso,*args, **kwargs):
    print(f"Data: {data_extenso}")
    for verso in args:
        print(verso)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_poema("Sexta dia 16", "Zen of Python",
              "Beautiful is better than ugly.",
              author="Tim Peters", ano=1999)

#ou seja se eui 
#Parametros especiais ---

#POR posição ----
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")
saudacao("Ana", "Olá")

#posicao obrigatoria apenas para os primeiros parametros utilizando /
def funcao_posicional(a, b, /, c, d):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
funcao_posicional(1, 2, c=3, d=4)

#tudo que vem antes da / é posicional obrigatorio
#depois da / pode ser posicional ou nomeado


#POR nome ---
saudacao(mensagem="Bem-vinda", nome="Carlos")

#obrigatorio nomeado utilizando *
def funcao_nomeada(*, x, y):
    print(f"x: {x}, y: {y}")
funcao_nomeada(x=10, y=20)
#tudo que vem depois do * é nomeado obrigatorio
#antes do * pode ser posicional ou nomeado

#obrigatorio nomeado e posicional juntos
def saudacao(nome, /, *, mensagem):
    print(f"{mensagem}, {nome}!")
saudacao("Pedro", mensagem="Olá")
saudacao("Maria", mensagem="Oi")

#Objetos de primeira classe ---

def soma(a, b):
    return a + b

def dobrar(a,b,soma):
    return soma(a,b) * 2

def exibir_resultado_dobrar(valor):
    print(f"Dobrar: {valor}")

def exibir_soma(a,b,soma):
    resultado = soma(a,b)
    print(f"Soma: {resultado}")

resultado = exibir_soma(3, 4, soma)
resultado2 = exibir_resultado_dobrar(dobrar(3, 4, soma))

#funções podem ser passadas como argumentos para outras funções
#podem ser retornadas por outras funções
#podem ser atribuídas a variáveis

#Variaveis Global e Local ---

mensagem = "Olá do escopo global!"  #variável global
def funcao_exemplo():
    mensagem = "Olá do escopo local!"  #variável local
    #so existe dentro da função
    print(mensagem)  #imprime a variável local

funcao_exemplo()  #chama a função
print(mensagem)  #imprime a variável global


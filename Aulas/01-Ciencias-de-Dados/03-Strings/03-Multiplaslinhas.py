#String tripla para múltiplas linhas

nome = "Duda"

mensagem = f''' 
Olá, {nome}!
Seja Bem vindo  
Estou testando uma string de múltiplas linhas.
'''

print(mensagem)

mensagem = f''' 
Olá, {nome}!
    Seja Bem vindo  
Estou testando uma string de múltiplas linhas.
        MUITO LEGAL!!!!!!!!!! a formatacao mantem os espaços e quebras de linha.
        :)
'''
print(mensagem)

#Exemplo de menu em um isstema que pode ajudar na organização do código

menu = '''
==========================
        MENU PRINCIPAL      
==========================
1. Iniciar novo jogo
2. Carregar jogo
3. Configurações
0. Sair
==========================
'''

print(menu)
#Dicionario
#chaves e valores
#estrutura: {chave1: valor1, chave2: valor2, ...}
#chave imutavel (string, numero, tupla)
#valor mutavel (qualquer tipo de dado)

#Criando um dicionário
pessoa = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}
# ou 
pessoa = dict(nome='João', idade=30, cidade='São Paulo')  
print(pessoa)  

#Chaves: nome, idade, cidade
#Valores: João, 30, São Paulo

pessoa["telefone"] = "11999999999"  #Adiciona um novo par chave-valor
print(pessoa)

#Acessando valores
pessoa["nome"]  #Acessa o valor associado à chave 'nome'
print("Nome:", pessoa["nome"])

pessoa["nome"] = "Maria"  #Modifica o valor associado à chave 'nome'
print("Nome modificado:", pessoa["nome"])

#Dicionario aninhado
empresa = {
    'nome': 'Tech Solutions',
    'funcionarios': {
        'desenvolvedor': 'Ana',
        'designer': 'Carlos'
    }
}
print("Empresa:", empresa)
print("Desenvolvedor:", empresa['funcionarios']['desenvolvedor']) 

#Aceessando chaves e valores
#Iterando sobre um dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#Metodos de dicionarios

#copy - cria uma cópia do dicionário
pessoa_copia = pessoa.copy()
print("Cópia de pessoa:", pessoa_copia)

#fromkeys - cria um novo dicionário com chaves especificadas e valores padrão
novo_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print("Novo dicionário de fromkeys:", novo_dict)

#get - acessa o valor de uma chave, retornando None se a chave não existir
idade = pessoa.get('idade')
print("Idade usando get():", idade)

##get vs acesso direto
altura = pessoa.get('altura')  #Chave não existe
print("Altura usando get():", altura)  #Retorna None
#altura = pessoa['altura']  #Chave não existe
#print("Altura usando acesso direto:", altura)  #Gera um erro

#tems - verifica se uma chave existe no dicionário
existe_nome = 'nome' in pessoa
print("Existe a chave 'nome'?", existe_nome)

#keys - retorna uma lista de chaves
chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)

#values - retorna uma lista de valores
valores = pessoa.values()


#pop - remove um par chave-valor e retorna o valor
telefone = pessoa.pop('telefone', 'Chave não encontrada')
print("Telefone removido:", telefone)
print("Dicionário após pop():", pessoa)


#popitem - remove e retorna um par chave-valor arbitrário
chave_valor_removido = pessoa.popitem()
print("Par chave-valor removido com popitem():", chave_valor_removido)
print("Dicionário após popitem():", pessoa)

#setdefault - acessa o valor de uma chave, definindo um valor padrão se a chave não existir
cidade = pessoa.setdefault('cidade', 'Rio de Janeiro')
print("Cidade usando setdefault():", cidade)
#se existe, não altera - se não existe, cria com o valor padrão

#update - atualiza o dicionário com pares chave-valor de outro dicionário
pessoa.update({'idade': 31, 'profissao': 'Engenheiro'})
print("Dicionário após update():", pessoa)

#in operador de associação para dicionários
existe_idade = 'idade' in pessoa
print("Existe a chave 'idade'?", existe_idade)

#del - remove um par chave-valor
print("Dicionário antes do del:", pessoa)
del pessoa['profissao']
print("Dicionário após del:", pessoa)
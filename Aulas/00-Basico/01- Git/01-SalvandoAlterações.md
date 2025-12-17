
## Iniciar um repositório Git
- `git init`  
  Inicializa um novo repositório Git na pasta atual.

##### observação: link que podem ajudar <https://readme.so/pt/editor> e <https://docs.github.com/pt/get-started>
---

## Criando um clone de um repositório
- `git clone <link-do-repositorio> <nome-da-pasta>`  
  Cria uma cópia local de um repositório remoto.  
  O `<nome-da-pasta>` é opcional; se não informado, o Git cria uma pasta com o nome do repositório.

---

## Salvando alterações no repositório local

- **`git status`**  
  Verifica o status do repositório, mostrando:
  - Em qual branch você está
  - Arquivos modificados
  - Arquivos ainda não adicionados ao commit

- **`git add <arquivo>`**  
  Adiciona arquivos modificados para o próximo commit.

- **`git add .`**  
  Adiciona **todos os arquivos modificados** para o próximo commit.

- **`.gitignore`**  
  Arquivo que define **quais arquivos ou pastas o Git deve ignorar**.  
  Exemplo de `.gitignore` para C/C++ com VS Code:

- **`git log`**  
Mostra o **histórico de commits** do repositório, incluindo:
- Hash do commit (identificador único)
- Autor
- Data e hora
- Mensagem do commit
# O Que é uma Branch?

- Uma **ramificação** do projeto que permite trabalhar em **novas funcionalidades** ou testes sem afetar o código principal.
- Útil para **testar ideias** antes de integrá-las ao sistema principal.
- Uma branch é basicamente um **ponteiro móvel** que acompanha o último commit da linha de desenvolvimento.

---

## Comandos básicos

- **Criar e mudar para uma nova branch**:
git checkout -b <nome-da-branch>

---
## Dicas para nomear branches

- Use nomes curtos e descritivos, como feature/login ou bugfix/erro-formulario.

- Evite nomes genéricos como teste ou nova-branch.

- Utilize padrão consistente (por exemplo feature/, bugfix/, hotfix/).
--

## conflitos de merge

- Ocorrem quando duas branches alteram a mesma linha de um arquivo ou arquivos relacionados.

- Conflito concorrente: o Git não sabe qual alteração manter e pede intervenção manual.

## Comandos úteis no dia a dia

- `git fetch`  
  Atualiza as referências do repositório remoto sem alterar os arquivos locais.

- `git diff`  
  Mostra as diferenças entre arquivos/modificações no seu repositório.

- `git merge <nome-da-branch>`  
  Faz a fusão da branch especificada na branch atual.

- `git clone <link-do-repositório> -b <nome-da-branch>`  
  Clona um repositório remoto e já coloca você na branch especificada.

- ` git clone --branch <nome-da-branch> --single-branch `
<link-do-repositório>

## Observação: 
- pode ajudar o link [def]

[def]: https://git-scm.com/book/pt-br/v2/Branches-no-Git-O-b%c3%a1sico-de-Ramifica%c3%a7%c3%a3o-Branch-e-Mesclagem-Merge
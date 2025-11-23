## Desfazer alterações

- **`git restore <arquivo>`**  
  Desfaz alterações em um arquivo específico que ainda não foi commitado.

- **`git commit --amend -m "nova mensagem"`**  
  Altera a mensagem do **último commit** sem criar um novo commit.

- **`git commit --amend`**  
  Abre o editor para alterar a mensagem do **último commit**.

---

## Git Reset

- **`git reset --soft <commit>`**  
  Move o ponteiro do HEAD para `<commit>` mantendo **as alterações na área de staging** (arquivos adicionados com `git add`).

- **`git reset --mixed <commit>`**  
  Move o ponteiro do HEAD para `<commit>` **mantendo as alterações no diretório de trabalho**, mas **remove da área de staging**.  

- **`git reset --hard <commit>`**  
  Move o ponteiro do HEAD para `<commit>` **descartando todas as alterações**, tanto na staging quanto no diretório de trabalho.  
  **Cuidado:** perde informações 
 
 - **`git reset <arquivo>`**  
  Remove um arquivo da **área de staging**, ou seja, ele volta a ficar como modificado, mas **não será incluído no próximo commit**.


- **`git restore <arquivo>`**  
  Desfaz alterações em um arquivo que **ainda não foi commitado**, voltando ao último estado registrado no repositório.  

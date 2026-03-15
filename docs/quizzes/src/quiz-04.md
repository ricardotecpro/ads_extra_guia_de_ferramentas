# Quiz: Aula 04 - Git Fundamentos 🛠️

1.  **O que o Git faz essencialmente?**
    - [ ] Hospeda sites na internet.
    - [x] Gerencia o histórico de alterações de arquivos (versionamento).
    - [ ] Compila código Java em linguagem de máquina.
    - [ ] Edita imagens e vídeos.
    *   *Explicação: O Git permite salvar "fotos" do seu projeto em diferentes momentos do tempo.*

2.  **Qual o primeiro comando que você deve rodar ao iniciar um novo projeto com Git?**
    - [ ] `git commit`
    - [x] `git init`
    - [ ] `git push`
    - [ ] `git add`
    *   *Explicação: `git init` cria o repositório local e a pasta oculta `.git`.*

3.  **Para que serve a "Staging Area" (ou Index)?**
    - [ ] Para deletar arquivos permanentemente.
    - [x] Para selecionar quais arquivos alterados devem ser incluídos no próximo commit.
    - [ ] Para ver o código de outros desenvolvedores.
    - [ ] Para hospedar o site online.
    *   *Explicação: Você usa o `git add` para mover arquivos para esta área de "preparação".*

4.  **Qual comando salva permanentemente as alterações no histórico local?**
    - [ ] `git save`
    - [x] `git commit`
    - [ ] `git snapshot`
    - [ ] `git store`
    *   *Explicação: O `commit` é o salvamento oficial de uma versão do código.*

5.  **O que a mensagem de commit deve descrever?**
    - [ ] O nome do desenvolvedor.
    - [x] O que foi alterado e por que (de forma concisa e clara).
    - [ ] A data e hora exatas do salvamento.
    - [ ] O número de linhas deletadas.
    *   *Explicação: Mensagens boas ajudam a entender a evolução do projeto no futuro.*

6.  **Como você verifica quais arquivos foram modificados mas ainda não foram "comitados"?**
    - [ ] `git check`
    - [x] `git status`
    - [ ] `git verify`
    - [ ] `git show`
    *   *Explicação: O `git status` mostra o estado atual da sua pasta em relação ao último commit.*

7.  **O que acontece se você rodar `git log`?**
    - [ ] O Git apaga o repositório.
    - [x] O Git exibe a lista cronológica de todos os commits realizados.
    - [ ] O Git abre o editor de código.
    - [ ] O Git faz o upload dos arquivos para a nuvem.
    *   *Explicação: O `log` é o livro de história do seu projeto.*

8.  **Qual a diferença entre o Git na sua máquina e o GitHub?**
    - [ ] Não há diferença, são o mesmo software.
    - [x] O Git é a ferramenta local; o GitHub é uma plataforma online que hospeda repositórios Git.
    - [ ] O GitHub é para designers e o Git para programadores.
    - [ ] O Git é pago e o GitHub é sempre gratuito.
    *   *Explicação: O Git funciona offline; o GitHub é o servidor onde você compartilha o código.*

9.  **O que o comando `git add .` faz?**
    - [ ] Deleta todos os arquivos da pasta.
    - [x] Adiciona todos os arquivos novos e modificados da pasta atual para a Staging Area.
    - [ ] Cria um ponto final no histórico.
    - [ ] Envia os arquivos para o servidor remoto.
    *   *Explicação: O ponto `.` representa "tudo o que está no diretório atual".*

10. **Por que o arquivo `.gitignore` é importante?**
    - [ ] Para esconder fotos pessoais do desenvolvedor.
    - [x] Para dizer ao Git quais arquivos e pastas ele deve ignorar (ex: senhas, pasta `node_modules`).
    - [ ] Para deletar arquivos automaticamente do repositório.
    - [ ] Para impedir que outros desenvolvedores editem o código.
    *   *Explicação: Evita que "lixo" ou arquivos sensíveis sejam enviados para o histórico de versão.*

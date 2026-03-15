# Quiz: Aula 10 - Qualidade de Código (ESLint / Prettier) ✨

1.  **O que é análise estática de código?**
    - [ ] Executar o código para ver se ele trava.
    - [x] Analisar o código sem executá-lo para encontrar erros de lógica ou estilo.
    - [ ] Deletar arquivos que não são usados.
    - [ ] Traduzir o código para outra linguagem.
    *   *Explicação: Ferramentas como Linters fazem a análise dos arquivos em busca de padrões.*

2.  **Qual a principal função do Prettier?**
    - [ ] Encontrar bugs de segurança.
    - [x] Formatar o código automaticamente (estilo visual).
    - [ ] Compilar o código para produção.
    - [ ] Gerenciar as versões do projeto no Git.
    *   *Explicação: O Prettier garante que todo o time siga o mesmo padrão visual (aspas, espaços, vírgulas).*

3.  **Qual a diferença entre um Linter e um Formatter?**
    - [ ] São nomes diferentes para a mesma coisa.
    - [x] O Linter verifica a qualidade e lógica (bugs); o Formatter verifica apenas o visual (estilo).
    - [ ] O Formatter é para CSS e o Linter para JavaScript.
    - [ ] O Linter é obrigatório e o Formatter é proibido em empresas.
    *   *Explicação: Linters como o ESLint podem detectar variáveis não usadas ou loops infinitos.*

4.  **Por que é importante padronizar o código em uma equipe?**
    - [ ] Para que o computador não quebre.
    - [x] Para facilitar a leitura, manutenção e evitar discussões desnecessárias sobre estilo.
    - [ ] Porque linguagens como JavaScript só rodam se o código estiver bonito.
    - [ ] Por uma questão de estética pessoal do sênior da equipe.
    *   *Explicação: Código padronizado parece ter sido escrito por uma única pessoa, reduzindo a carga cognitiva.*

5.  **A regra "no-unused-vars" do ESLint faz o quê?**
    - [ ] Permite usar variáveis globais.
    - [x] Avisa ou bloqueia o código se existirem variáveis declaradas que nunca são usadas.
    - [ ] Deleta as variáveis que o desenvolvedor esqueceu.
    - [ ] Muda o nome das variáveis para nomes mais curtos.
    *   *Explicação: Variáveis não usadas poluem o código e podem indicar lógica incompleta.*

6.  **O que significa "Format on Save" (Formatar ao Salvar)?**
    - [ ] Uma regra que impede você de salvar arquivos se houver erro.
    - [x] Um recurso do editor (VS Code) que roda o formatador toda vez que você salva o arquivo.
    - [ ] O ato de formatar o disco rígido após o deploy.
    - [ ] Um comando do terminal que salva o código no GitHub.
    *   *Explicação: É uma das configurações mais produtivas para qualquer desenvolvedor.*

7.  **Qual o papel do arquivo `.eslintrc` ou `.prettierrc`?**
    - [ ] Guardar as senhas do banco de dados.
    - [x] Configurar as regras específicas que o Linter ou Formatter deve seguir no projeto.
    - [ ] Criar o backup do código na nuvem.
    - [ ] Impedir que outros desenvolvedores instalem extensões.
    *   *Explicação: Nesses arquivos você define se quer usar aspas simples, ponto e vírgula, etc.*

8.  **Dizer que um Linter ajuda a evitar "bugs silenciosos" significa que:**
    - [ ] Ele remove o som do computador quando ocorre um erro.
    - [x] Ele encontra erros que passariam despercebidos pelo olho humano mas que causariam falhas em produção.
    - [ ] Ele apaga o código antes do erro acontecer.
    - [ ] Ele impede o desenvolvedor de falar durante o trabalho.
    *   *Explicação: Erros sutis de lógica são capturados pela análise estática automática.*

9.  **O ESLint é exclusivo para JavaScript?**
    - [ ] Sim, não existem linters para outras linguagens.
    - [x] Não, embora seja o mais famoso para JS, existem linters como Flake8 (Python) ou Checkstyle (Java).
    - [ ] Sim, mas ele pode ser usado para formatar fotos também.
    - [ ] Não, ele é um sistema operacional completo.
    *   *Explicação: Quase todas as linguagens modernas possuem seus próprios Linters.*

10. **Qual a maior vantagem de rodar o Linter na pipeline de CI (Aula 11)?**
    - [ ] Deixar a build mais lenta e segura.
    - [x] Impedir que código fora dos padrões seja mesclado ao projeto principal.
    - [ ] Economizar energia nos servidores da empresa.
    - [ ] Mostrar para o chefe quem é o desenvolvedor que erra mais.
    *   *Explicação: Garante que a qualidade do repositório nunca caia, automatizando a revisão.*

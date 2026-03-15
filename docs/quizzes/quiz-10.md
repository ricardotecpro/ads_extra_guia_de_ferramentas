# Quiz 10

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que é análise estática de código?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Executar o código para ver se ele trava.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Analisar o código sem executá-lo para encontrar erros de lógica ou estilo.">Analisar o código sem executá-lo para encontrar erros de lógica ou estilo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deletar arquivos que não são usados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Traduzir o código para outra linguagem.
    *   *Explicação: Ferramentas como Linters fazem a análise dos arquivos em busca de padrões.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual a principal função do Prettier?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Encontrar bugs de segurança.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Formatar o código automaticamente (estilo visual).">Formatar o código automaticamente (estilo visual).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Compilar o código para produção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Gerenciar as versões do projeto no Git.
    *   *Explicação: O Prettier garante que todo o time siga o mesmo padrão visual (aspas, espaços, vírgulas).*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Qual a diferença entre um Linter e um Formatter?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">São nomes diferentes para a mesma coisa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O Linter verifica a qualidade e lógica (bugs); o Formatter verifica apenas o visual (estilo).">O Linter verifica a qualidade e lógica (bugs); o Formatter verifica apenas o visual (estilo).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Formatter é para CSS e o Linter para JavaScript.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Linter é obrigatório e o Formatter é proibido em empresas.
    *   *Explicação: Linters como o ESLint podem detectar variáveis não usadas ou loops infinitos.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **Por que é importante padronizar o código em uma equipe?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para que o computador não quebre.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para facilitar a leitura, manutenção e evitar discussões desnecessárias sobre estilo.">Para facilitar a leitura, manutenção e evitar discussões desnecessárias sobre estilo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Porque linguagens como JavaScript só rodam se o código estiver bonito.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Por uma questão de estética pessoal do sênior da equipe.
    *   *Explicação: Código padronizado parece ter sido escrito por uma única pessoa, reduzindo a carga cognitiva.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **A regra "no-unused-vars" do ESLint faz o quê?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Permite usar variáveis globais.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Avisa ou bloqueia o código se existirem variáveis declaradas que nunca são usadas.">Avisa ou bloqueia o código se existirem variáveis declaradas que nunca são usadas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deleta as variáveis que o desenvolvedor esqueceu.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Muda o nome das variáveis para nomes mais curtos.
    *   *Explicação: Variáveis não usadas poluem o código e podem indicar lógica incompleta.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **O que significa "Format on Save" (Formatar ao Salvar)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma regra que impede você de salvar arquivos se houver erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um recurso do editor (VS Code) que roda o formatador toda vez que você salva o arquivo.">Um recurso do editor (VS Code) que roda o formatador toda vez que você salva o arquivo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O ato de formatar o disco rígido após o deploy.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um comando do terminal que salva o código no GitHub.
    *   *Explicação: É uma das configurações mais produtivas para qualquer desenvolvedor.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **Qual o papel do arquivo `.eslintrc` ou `.prettierrc`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Guardar as senhas do banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Configurar as regras específicas que o Linter ou Formatter deve seguir no projeto.">Configurar as regras específicas que o Linter ou Formatter deve seguir no projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Criar o backup do código na nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Impedir que outros desenvolvedores instalem extensões.
    *   *Explicação: Nesses arquivos você define se quer usar aspas simples, ponto e vírgula, etc.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **Dizer que um Linter ajuda a evitar "bugs silenciosos" significa que:**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele remove o som do computador quando ocorre um erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Ele encontra erros que passariam despercebidos pelo olho humano mas que causariam falhas em produção.">Ele encontra erros que passariam despercebidos pelo olho humano mas que causariam falhas em produção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele apaga o código antes do erro acontecer.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele impede o desenvolvedor de falar durante o trabalho.
    *   *Explicação: Erros sutis de lógica são capturados pela análise estática automática.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **O ESLint é exclusivo para JavaScript?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Sim, não existem linters para outras linguagens.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Não, embora seja o mais famoso para JS, existem linters como Flake8 (Python) ou Checkstyle (Java).">Não, embora seja o mais famoso para JS, existem linters como Flake8 (Python) ou Checkstyle (Java).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Sim, mas ele pode ser usado para formatar fotos também.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não, ele é um sistema operacional completo.
    *   *Explicação: Quase todas as linguagens modernas possuem seus próprios Linters.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Qual a maior vantagem de rodar o Linter na pipeline de CI (Aula 11)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deixar a build mais lenta e segura.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Impedir que código fora dos padrões seja mesclado ao projeto principal.">Impedir que código fora dos padrões seja mesclado ao projeto principal.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Economizar energia nos servidores da empresa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Mostrar para o chefe quem é o desenvolvedor que erra mais.
    *   *Explicação: Garante que a qualidade do repositório nunca caia, automatizando a revisão.*</div>
  <div class="quiz-feedback"></div>
</div>


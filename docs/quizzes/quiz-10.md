# Quiz: Aula 10 - Qualidade de Código (ESLint / Prettier) ✨

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é análise estática de código?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Executar o código para ver se ele trava.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Analisar o código sem executá-lo para encontrar erros de lógica ou estilo.">Analisar o código sem executá-lo para encontrar erros de lógica ou estilo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar arquivos que não são usados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Traduzir o código para outra linguagem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a principal função do Prettier?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Encontrar bugs de segurança.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Formatar o código automaticamente (estilo visual).">Formatar o código automaticamente (estilo visual).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Compilar o código para produção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Gerenciar as versões do projeto no Git.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a diferença entre um Linter e um Formatter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">São nomes diferentes para a mesma coisa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Linter verifica a qualidade e lógica (bugs); o Formatter verifica apenas o visual (estilo).">O Linter verifica a qualidade e lógica (bugs); o Formatter verifica apenas o visual (estilo).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O Formatter é para CSS e o Linter para JavaScript.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O Linter é obrigatório e o Formatter é proibido em empresas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Por que é importante padronizar o código em uma equipe?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para que o computador não quebre.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Para facilitar a leitura, manutenção e evitar discussões desnecessárias sobre estilo.">Para facilitar a leitura, manutenção e evitar discussões desnecessárias sobre estilo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque linguagens como JavaScript só rodam se o código estiver bonito.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Por uma questão de estética pessoal do sênior da equipe.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. A regra "no-unused-vars" do ESLint faz o quê?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Permite usar variáveis globais.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Avisa ou bloqueia o código se existirem variáveis declaradas que nunca são usadas.">Avisa ou bloqueia o código se existirem variáveis declaradas que nunca são usadas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deleta as variáveis que o desenvolvedor esqueceu.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Muda o nome das variáveis para nomes mais curtos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que significa "Format on Save" (Formatar ao Salvar)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma regra que impede você de salvar arquivos se houver erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um recurso do editor (VS Code) que roda o formatador toda vez que você salva o arquivo.">Um recurso do editor (VS Code) que roda o formatador toda vez que você salva o arquivo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O ato de formatar o disco rígido após o deploy.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um comando do terminal que salva o código no GitHub.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual o papel do arquivo `.eslintrc` ou `.prettierrc`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Guardar as senhas do banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Configurar as regras específicas que o Linter ou Formatter deve seguir no projeto.">Configurar as regras específicas que o Linter ou Formatter deve seguir no projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Criar o backup do código na nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Impedir que outros desenvolvedores instalem extensões.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Dizer que um Linter ajuda a evitar "bugs silenciosos" significa que:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele remove o som do computador quando ocorre um erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele encontra erros que passariam despercebidos pelo olho humano mas que causariam falhas em produção.">Ele encontra erros que passariam despercebidos pelo olho humano mas que causariam falhas em produção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele apaga o código antes do erro acontecer.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele impede o desenvolvedor de falar durante o trabalho.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O ESLint é exclusivo para JavaScript?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, não existem linters para outras linguagens.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Não, embora seja o mais famoso para JS, existem linters como Flake8 (Python) ou Checkstyle (Java).">Não, embora seja o mais famoso para JS, existem linters como Flake8 (Python) ou Checkstyle (Java).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, mas ele pode ser usado para formatar fotos também.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, ele é um sistema operacional completo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual a maior vantagem de rodar o Linter na pipeline de CI (Aula 11)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deixar a build mais lenta e segura.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Impedir que código fora dos padrões seja mesclado ao projeto principal.">Impedir que código fora dos padrões seja mesclado ao projeto principal.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Economizar energia nos servidores da empresa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Mostrar para o chefe quem é o desenvolvedor que erra mais.</div>
  <div class="quiz-feedback"></div>
</div>


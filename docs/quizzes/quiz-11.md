# Quiz: Aula 11 - CI/CD Moderno (GitHub Actions) 🚀

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa a sigla CI?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Core Integration.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Continuous Integration (Integração Contínua).">Continuous Integration (Integração Contínua).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Code Identification.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Computer Intelligence.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual o principal benefício do CD (Continuous Delivery/Deployment)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar o código antigo automaticamente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Automatizar a entrega do software para os ambientes de teste ou produção, reduzindo processos manuais.">Automatizar a entrega do software para os ambientes de teste ou produção, reduzindo processos manuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Fazer o backup do banco de dados na máquina do desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Substituir a necessidade de ter um servidor.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. No GitHub Actions, o que é um "Workflow"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O nome do cargo do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um processo automatizado configurável que executará um ou mais jobs.">Um processo automatizado configurável que executará um ou mais jobs.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma pasta onde guardamos imagens.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O layout visual do GitHub.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Em qual formato de arquivo as configurações do GitHub Actions são escritas?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">JSON.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! YAML (.yml ou .yaml).">YAML (.yml ou .yaml).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">HTML.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">XML.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que é um "Trigger" (Gatilho) no Actions?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um erro que para a pipeline.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um evento que inicia a execução do workflow (ex: push, pull_request).">Um evento que inicia a execução do workflow (ex: push, pull_request).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O botão de deletar o repositório.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma senha secreta do desenvolvedor.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Para que serve um "Runner" no contexto de CI/CD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para o desenvolvedor correr atrás dos prazos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o servidor/máquina virtual que realmente executa os comandos do seu workflow.">É o servidor/máquina virtual que realmente executa os comandos do seu workflow.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um tipo de plugin do VS Code.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É o comando para deletar arquivos temporários.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que acontece se um Job da sua pipeline falhar?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O GitHub deleta sua conta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O workflow é interrompido, o GitHub sinaliza com um "X" vermelho e avisa o desenvolvedor.">O workflow é interrompido, o GitHub sinaliza com um "X" vermelho e avisa o desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O código é enviado para o servidor de qualquer forma.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nada, o processo continua sem problemas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que são "GitHub Secrets"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Segredos sobre a história da empresa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Variáveis de ambiente criptografadas (como senhas e chaves de API) que a pipeline usa com segurança.">Variáveis de ambiente criptografadas (como senhas e chaves de API) que a pipeline usa com segurança.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Comentários escondidos no código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Membros ocultos da equipe.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual a vantagem de usar `on: [pull_request]` em vez de apenas `on: [push]`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não há vantagem.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Permite testar o código antes mesmo dele entrar na branch principal, auxiliando no Code Review.">Permite testar o código antes mesmo dele entrar na branch principal, auxiliando no Code Review.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Economiza dinheiro para o GitHub.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Faz o deploy ser mais rápido.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que é um "Step" dentro de um Job do GitHub Actions?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um degrau na escada da empresa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma tarefa individual que executa um comando ou uma ação específica.">Uma tarefa individual que executa um comando ou uma ação específica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O nome do arquivo YAML.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de branch.</div>
  <div class="quiz-feedback"></div>
</div>


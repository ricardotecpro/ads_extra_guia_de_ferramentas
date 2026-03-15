# Quiz 11

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que significa a sigla CI?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Core Integration.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Continuous Integration (Integração Contínua).">Continuous Integration (Integração Contínua).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Code Identification.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Computer Intelligence.
    *   *Explicação: CI foca na integração frequente do código de vários desenvolvedores, validada por testes automáticos.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual o principal benefício do CD (Continuous Delivery/Deployment)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deletar o código antigo automaticamente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Automatizar a entrega do software para os ambientes de teste ou produção, reduzindo processos manuais.">Automatizar a entrega do software para os ambientes de teste ou produção, reduzindo processos manuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Fazer o backup do banco de dados na máquina do desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Substituir a necessidade de ter um servidor.
    *   *Explicação: O CD garante que o deploy seja um processo repetível e seguro.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **No GitHub Actions, o que é um "Workflow"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome do cargo do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um processo automatizado configurável que executará um ou mais jobs.">Um processo automatizado configurável que executará um ou mais jobs.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma pasta onde guardamos imagens.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O layout visual do GitHub.
    *   *Explicação: Workflows são as pipelines descritas em arquivos YAML.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **Em qual formato de arquivo as configurações do GitHub Actions são escritas?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">JSON.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! YAML (.yml ou .yaml).">YAML (.yml ou .yaml).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">HTML.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">XML.
    *   *Explicação: YAML é o padrão da indústria para arquivos de configuração devido à sua legibilidade.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **O que é um "Trigger" (Gatilho) no Actions?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um erro que para a pipeline.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um evento que inicia a execução do workflow (ex: push, pull_request).">Um evento que inicia a execução do workflow (ex: push, pull_request).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O botão de deletar o repositório.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma senha secreta do desenvolvedor.
    *   *Explicação: O trigger define "quando" a automação deve começar.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **Para que serve um "Runner" no contexto de CI/CD?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para o desenvolvedor correr atrás dos prazos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! É o servidor/máquina virtual que realmente executa os comandos do seu workflow.">É o servidor/máquina virtual que realmente executa os comandos do seu workflow.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">É um tipo de plugin do VS Code.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">É o comando para deletar arquivos temporários.
    *   *Explicação: O Runner é o "trabalhador" que roda os testes e faz o build do seu app.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **O que acontece se um Job da sua pipeline falhar?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O GitHub deleta sua conta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O workflow é interrompido, o GitHub sinaliza com um "X" vermelho e avisa o desenvolvedor.">O workflow é interrompido, o GitHub sinaliza com um "X" vermelho e avisa o desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O código é enviado para o servidor de qualquer forma.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Nada, o processo continua sem problemas.
    *   *Explicação: A falha serve para alertar que algo no código novo não está correto.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **O que são "GitHub Secrets"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Segredos sobre a história da empresa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Variáveis de ambiente criptografadas (como senhas e chaves de API) que a pipeline usa com segurança.">Variáveis de ambiente criptografadas (como senhas e chaves de API) que a pipeline usa com segurança.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Comentários escondidos no código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Membros ocultos da equipe.
    *   *Explicação: Secrets permitem usar dados sensíveis na automação sem expô-los no código.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **Qual a vantagem de usar `on: [pull_request]` em vez de apenas `on: [push]`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não há vantagem.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Permite testar o código antes mesmo dele entrar na branch principal, auxiliando no Code Review.">Permite testar o código antes mesmo dele entrar na branch principal, auxiliando no Code Review.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Economiza dinheiro para o GitHub.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Faz o deploy ser mais rápido.
    *   *Explicação: Testar PRs garante que a integração só ocorra se o código estiver estável.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **O que é um "Step" dentro de um Job do GitHub Actions?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um degrau na escada da empresa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Uma tarefa individual que executa um comando ou uma ação específica.">Uma tarefa individual que executa um comando ou uma ação específica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome do arquivo YAML.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um tipo de branch.
    *   *Explicação: Jobs são compostos por vários Steps executados em sequência.*</div>
  <div class="quiz-feedback"></div>
</div>


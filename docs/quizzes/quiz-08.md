# Quiz 08

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **Qual o principal objetivo dos testes automatizados?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Substituir o trabalho do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Garantir que o software continue funcionando corretamente após mudanças (evitar regressão).">Garantir que o software continue funcionando corretamente após mudanças (evitar regressão).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deixar o código mais bonito visualmente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Aumentar o tamanho do arquivo final do projeto.
    *   *Explicação: Testes servem como uma rede de segurança para o programador mexer no código sem medo.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **O que são "Testes Unitários"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testes feitos apenas por uma pessoa da equipe.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Testes que validam pequenas partes isoladas do código (como uma única função).">Testes que validam pequenas partes isoladas do código (como uma única função).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testes feitos apenas uma vez no final do ano.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testes que verificam se o site carrega no celular.
    *   *Explicação: São a base da pirâmide e testam a menor unidade lógica possível.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Qual ferramenta de teste é o padrão para o ecossistema JavaScript/Node.js?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">JUnit.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Jest.">Jest.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">PyTest.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Selenium.
    *   *Explicação: O Jest é amplamente adotado por sua facilidade de uso e recursos integrados.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **O que significa a sigla TDD (Test Driven Development)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testar Depois de Desenvolver.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Desenvolvimento Orientado por Testes (escrever o teste antes do código).">Desenvolvimento Orientado por Testes (escrever o teste antes do código).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Técnicas de Design para Desenvolvedores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Total Data Delivery.
    *   *Explicação: No TDD, o teste "guia" a implementação da funcionalidade.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **A Pirâmide de Testes sugere que devemos ter:**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Mais testes de Interface (E2E) do que Unitários.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Muitos testes Unitários na base e poucos testes E2E/UI no topo.">Muitos testes Unitários na base e poucos testes E2E/UI no topo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Apenas um tipo de teste para economizar tempo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testes apenas na fase de deploy.
    *   *Explicação: Testes unitários são mais rápidos, baratos e fáceis de manter.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **O que é um "Teste de Integração"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um teste de cultura para novos funcionários.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um teste que verifica se dois ou mais módulos do sistema funcionam bem juntos (ex: App + Banco de Dados).">Um teste que verifica se dois ou mais módulos do sistema funcionam bem juntos (ex: App + Banco de Dados).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um teste feito apenas no navegador Chrome.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O ato de baixar o código do GitHub.
    *   *Explicação: Foca na comunicação entre os componentes do sistema.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **Sobre o PyTest, é correto afirmar:**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">É um framework de testes exclusivo para Java.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! É o framework de teste mais popular e poderoso para a linguagem Python.">É o framework de teste mais popular e poderoso para a linguagem Python.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele serve para criar interfaces gráficas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele deleta arquivos com erro automaticamente.
    *   *Explicação: O PyTest é conhecido por sua sintaxe simples e extensibilidade.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **O que é um "Mock" ou "Dublê de Teste"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um erro que aparece no terminal.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um objeto que simula o comportamento de um componente real (ex: simular o envio de um e-mail sem enviá-lo de verdade).">Um objeto que simula o comportamento de um componente real (ex: simular o envio de um e-mail sem enviá-lo de verdade).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma extensão do VS Code para formatar código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome do desenvolvedor que criou o teste.
    *   *Explicação: Mocks permitem testar partes do sistema sem depender de serviços externos lentos ou caros.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **No ciclo TDD, o que significa o passo "Red" (Vermelho)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que o computador travou.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Que o teste foi executado e falhou (pois o código ainda não foi escrito).">Que o teste foi executado e falhou (pois o código ainda não foi escrito).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que o código contém vírus.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que o desenvolvedor está bravo com o projeto.
    *   *Explicação: Ver o teste falhar prova que ele é capaz de detectar erros.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Por que é importante rodar os testes automaticamente no GitHub (CI)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para gastar o dinheiro da empresa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para garantir que nenhum código quebrado entre na branch principal sem que ninguém perceba.">Para garantir que nenhum código quebrado entre na branch principal sem que ninguém perceba.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Porque os testes locais não funcionam na nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para preencher a aba "Actions" com informações inúteis.
    *   *Explicação: A automação garante que o padrão de qualidade seja mantido por todo o time.*</div>
  <div class="quiz-feedback"></div>
</div>


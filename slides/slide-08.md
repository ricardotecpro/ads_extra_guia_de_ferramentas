# Aula 08: Frameworks de Teste e Qualidade 🧪

---

## 🎯 Nossa Missão
*   Entender a importância dos testes automatizados.
*   Conhecer a Pirâmide de Testes.
*   Descobrir frameworks (Jest, PyTest, JUnit).
*   Introdução ao TDD (Test Driven Development).

---

## 😱 O Medo de Mudar o Código
*   "Se eu mexer aqui, o que será que quebra?" <!-- .element: class="fragment" -->
*   "No meu PC funcionava, no servidor parou." <!-- .element: class="fragment" -->
*   "O bug que eu corrigi ontem voltou hoje." <!-- .element: class="fragment" -->
*   **Testes são a sua rede de segurança!** <!-- .element: class="fragment" -->

---

## 🏗️ A Pirâmide de Testes
```mermaid
graph TD
    U[Testes Unitários - MUITOS]
    I[Integração - ALGUNS]
    E[E2E / Interface - POUCOS]
    U ---|Rápido/Barato| I
    I ---|Lento/Caro| E
```

---

## 1. Testes Unitários 🧩
Testam a menor parte possível do código (funções isoladas).
*   **Vantagem**: Execução instantânea. <!-- .element: class="fragment" -->
*   **Foco**: Lógica pura, cálculos, pequenas regras. <!-- .element: class="fragment" -->
*   **Ferramentas**: Jest, PyTest. <!-- .element: class="fragment" -->

---

## 2. Testes de Integração 🔗
Verificam se dois ou mais componentes funcionam bem juntos.
*   Ex: Aplicação + Banco de Dados. <!-- .element: class="fragment" -->
*   Ex: Serviço A + API externa. <!-- .element: class="fragment" -->
*   Buscam erros na comunicação entre partes. <!-- .element: class="fragment" -->

---

## 3. Testes End-to-End (E2E) 🌐
Simulam o usuário real usando o sistema completo.
*   Abre o navegador, clica em botões, preenche forms. <!-- .element: class="fragment" -->
*   **Custo**: São lentos e "frágeis" (quebram se o layout muda). <!-- .element: class="fragment" -->
*   **Ferramentas**: Cypress, Playwright, Selenium. <!-- .element: class="fragment" -->

---

## 🔴 Ciclo TDD (Red, Green, Refactor)
Uma nova forma de pensar o desenvolvimento:
1.  **Red**: Escreva um teste que falha (o código não existe). <!-- .element: class="fragment" -->
2.  **Green**: Escreva o mínimo de código para o teste passar. <!-- .element: class="fragment" -->
3.  **Refactor**: Melhore o código sem quebrar o teste. <!-- .element: class="fragment" -->

---

## 🤡 O que são Mocks?
Simulando o mundo real.
*   Você não quer enviar um e-mail de verdade toda vez que rodar o teste. <!-- .element: class="fragment" -->
*   Você cria um "objeto dublê" que finge ser o serviço de e-mail. <!-- .element: class="fragment" -->
*   Isso isola o teste e o deixa muito mais rápido. <!-- .element: class="fragment" -->

---

## 📦 Framework: Jest (JavaScript)
*   Simples: `expect(soma(2,2)).toBe(4)`. <!-- .element: class="fragment" -->
*   Extremamente rápido (paralelismo). <!-- .element: class="fragment" -->
*   Inclui ferramentas de Cobertura de Código. <!-- .element: class="fragment" -->

---

## 🐍 Framework: PyTest (Python)
*   Sintaxe limpa: `assert soma(2,2) == 4`. <!-- .element: class="fragment" -->
*   Poderoso sistema de Fixtures (preparação de dados). <!-- .element: class="fragment" -->
*   Ecossistema de plugins gigante. <!-- .element: class="fragment" -->

---

## ☕ Framework: JUnit (Java)
*   O avô dos frameworks modernos. <!-- .element: class="fragment" -->
*   Robusto e integrado nativamente com IDEs. <!-- .element: class="fragment" -->
*   Padrão absoluto no mundo corporativo Java. <!-- .element: class="fragment" -->

---

## 📊 Cobertura de Código (Coverage)
"Quanto do meu projeto está sendo testado?"
*   Gera relatórios mostrando quais linhas foram executadas pelos testes. <!-- .element: class="fragment" -->
*   **Meta**: 80% a 90% (100% é quase impossível e caro). <!-- .element: class="fragment" -->

---

## 💎 Qualidade de Código (Linting)
Diferente de testes, o Linter foca na "estética" e "segurança estática".
*   ESLint (JS), Flake8 (Python). <!-- .element: class="fragment" -->
*   Evita variáveis não usadas. <!-- .element: class="fragment" -->
*   Garante estilos uniformes. <!-- .element: class="fragment" -->

---

## 🔄 Testes na Pipeline (CI)
Nunca confie apenas no teste local!
*   A pipeline roda os testes a cada `git push`. <!-- .element: class="fragment" -->
*   Impede que código "quebrado" chegue na produção. <!-- .element: class="fragment" -->
*   Feedback automático para o time. <!-- .element: class="fragment" -->

---

## 🧪 Anatomia de um Teste
```javascript
test('deve somar dois números corretamente', () => {
  // 1. Arrange (Preparar)
  const a = 10;
  const b = 5;

  // 2. Act (Agir)
  const resultado = soma(a, b);

  // 3. Assert (Verificar)
  expect(resultado).toBe(15);
});
```

---

## 🏆 Checklist de Qualidade Pro
*   [ ] Entende os níveis da pirâmide. <!-- .element: class="fragment" -->
*   [ ] Sabe o que é um Mock e por que usar. <!-- .element: class="fragment" -->
*   [ ] Instalou um framework de teste no seu projeto. <!-- .element: class="fragment" -->
*   [ ] Entende o ciclo básico do TDD. <!-- .element: class="fragment" -->

---

## 📝 Prática de Hoje
1.  Criar uma função simples de cálculo.
2.  Escrever um teste unitário para ela usando Jest ou PyTest.
3.  Ver o teste passar e o teste falhar (mudando a expectativa).

---

## 🏁 Dúvidas?
Dormir tranquilo = Ter uma boa suite de testes! 🚀💤
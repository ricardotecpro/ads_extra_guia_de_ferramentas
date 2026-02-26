# Resolução: Aula 08 - Frameworks de Teste 🧪

### 🟢 Básicos (Fixação)

**1. Cultura de Teste**
Bugs sempre existirão devido a natureza volúvel nas construções algorítmicas, todavia "Testar Código" fornece blindagem de legado (Regression Prevent); ao redigir uma função que soma o carrinho de compras do cliente num projeto pequeno e cobri-lhe com baterias Unitárias lógicas, você tem o sinal verde ininterrupto (`PASSED`). Se no ano que vem um colaborador inexperiente quebrar as variáveis que você criou para dar um desconto no carrinho, a bateria apita (não permite o envio da ramagem) alertando uma falta estrutural de confiança. A função primordial dos testes é validar uma operação mecânica contra o medo humano.

**2. Ferramentas**
*   No ecossistema **Java**, historicamente a rainha suprema é a biblioteca unitária chamada **`JUnit`**.
*   Num ecossistema dinâmico moderno pautado pelo **Python**, a ferramenta ágil predominante chama-se **`PyTest`**.

---

### 🟡 Intermediários (Aplicação)

**3. Pirâmide de Testes**
Os testes **End-to-End (E2E)** (na ponta cimeira global da pirâmide) levantam navegadores reais (`webdriver`), manipulam campos de mouse via JavaScript (ex: Cypress) e imitam um humano navegando pelo software. Esse processamento é computacionalmente caro, frágil com mudanças de layout CSS e super demorado. Se você depende apenas deles e um quebra, a ponta de falha fica muito ampla para rastrear ("onde parou exato? no botão ou na API de checkout?"). Por isso os testes unitários constituem a base maciça da pirâmide em centenas, agindo de forma granular no código nativo sem levantar painéis HTTP (milissegundos) enquanto que testes pontuais de E2E ficam confinados na aba limítrofe apenas ratificando o sucesso generalizado da entrega das abas.

**4. Lógica TDD**
1.  **RED**: Escreva um teste automatizado primeiro. Como não existe código efetivamente produzido para supri-lo, ele quebrará e a tela sangrará de erros em "Vermelho".
2.  **GREEN**: Escreva a solução programática crua para aquela funcionalidade. Ela validará as requisições sintáticas com a base avaliativa construída outrora. Ficará em estado "Verde" (Passou).
3.  **REFACTOR**: O passo mandatório; a primeira solução do Dev sempre pode sofrer rearanjos mecânicos (otimizar variáveis, deixar legível). O interessante de modificar uma tese de um código recém-testado é certificar de que qualquer fator destrutor provindo da faxina apitará quebrando as predições unitárias (e voltando para o alerta Red). 

---

### 🔴 Desafio (Exploração)

**5. Mocks e Dublês**
Imagine que seu bloco de teste execute dez mil vezes por noite um laço de envio simulado de correspondências da API Twilio/SendGrid. Na vida real o cartão corporativo sangraria em faturas a cada acionamento dessa automação de checagem ou sobrecarregaria um e-mail com contaminação diária. Quando usamos "Mocks" (os atores e dublês digitais do Jest ou PyTest) dizemos a esse gatilho para isolar a arquitetura nativa exterior de rede (`sendEmail API`), substituí-la internamente e simplesmente chancelar (`return true / Fake Ok`) como operante. Assim simulamos conexões e serviços vitais independentemente de instabilidades de IP sem descontinuar a cadeia lógica de premissas estritas do microserviço testado.

---

[**⬅️ Voltar para o Exercício**](./exercicio-08.md)

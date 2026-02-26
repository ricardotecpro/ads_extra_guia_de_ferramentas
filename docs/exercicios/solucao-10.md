# Resolução: Aula 10 - Qualidade de Código ✨

### 🟢 Básicos (Fixação)

**1. Linter vs Formatter**
*   Para os espaços textuais errados (estética sem erros operacionais): Utiliza-se um **Formatter** (ex: Prettier).
*   Para o esquecimento de declarar a variável (falha lógica perigosa que quebra aplicação): Utiliza-se a leitura de padrões do **Linter** (ex: ESLint ou SonarLint).

**2. Configuração do VS Code**
A configuração `Format on Save` automatiza o acionamento do Formatter do editor no exato milissegundo em que apertamos o `CTRL+S`. Isso alivia o desenvolvedor de pressionar teclas de identação de escopo, ou atalhos quilométricos (`Shift+Alt+F`). O resultado é um ganho inestimável de foco na lógica base. 

---

### 🟡 Intermediários (Aplicação)

**3. Padronização em Equipe**
O Prettier não sofre de "vontades" ou "egos". Basta as instâncias da gerência criarem um mero arquivo padrão na raiz do código (o `.prettierrc`) e definirem nele a regra universal daquele repositório, por exemplo, o ditame de que usa-se `'singleQuote': true`. Toda vez que o dev teimoso da aspas duplas tentar salvar o script com `""`, o motor do VS Code apagará tudo automaticamente pautado no ditame silencioso e impessoal da raiz do projeto, pacificando as tretas de Code Review.

**4. Análise Estática**
Linters mais rígidos têm regras predeterminadas detectando chamas no código, como por exemplo os loops condicionais infinitos ou funções criadas e jamais consumidas internamente. Se a equipe envia para produção à AWS esse aplicativo com as variáveis ociosas e loops mal traçados, quando o código bater em ambiente de execução de máquina as CPUs trabalharão intensamente até atingir lentidão de infraestrutura, encarecendo a conta em dólares do faturamento mensal consideravelmente; prevenidos prematuramente via *Static Analysis*.

---

### 🔴 Desafio (Exploração)

**5. Regras Customizadas (no-console)**
O uso compulsivo de `console.log()` polui terabytes em arquivos de registro (*Logs*) vitais com prints de rastreio inúteis. Mais do que estética, é gravíssimo pelo escopo sensível: deixar um console solto em código que trafegará pro frontend permite aos invasores mal isencionados extraírem *tokens* vazados ou segredos processuais corporativos. A regra `no-console` aciona um farol vermelho de erro de PR logo na raiz de CI do desenvolvedor com vistas a evitar esses lapsos bizarros em massa.

---

[**⬅️ Voltar para o Exercício**](./exercicio-10.md)

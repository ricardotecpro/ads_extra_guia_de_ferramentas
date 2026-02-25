# Resolução: Aula 01 - Introdução ao Ecossistema 📝

### 🟢 Básicos (Fixação)

**1. Diferenciação de Ferramentas**
*   **Git (Controle de Versão)**: Obrigatório para salvar o histórico de código de forma segura e permitir reverter erros sem dor de cabeça.
*   **VS Code (Ambiente de Dev)**: Um editor leve para escrever o código com suporte a linting e formatação, garantindo produtividade e código limpo.
*   **Docker (Infraestrutura)**: Essencial para garantir que o projeto rode na minha máquina e em qualquer servidor do mesmo jeito, eliminando o problema do "só funciona na minha máquina".

**2. Identificação de Erros**
A afirmação do colega está incorreta. A principal diferença técnica é que um **Editor de Código** (como o VS Code) nasce leve, focando apenas na edição de texto, e você precisa instalar extensões para que ele ganhe poder. Em contrapartida, uma **IDE** (como o IntelliJ) é um "Ambiente Integrado de Desenvolvimento" que já vem de fábrica acoplado a compiladores, depuradores avançados e perfiladores (profilers) específicos para uma linguagem, sendo muito mais "pesada" e completa nativamente.

---

### 🟡 Intermediários (Aplicação)

**3. Fluxo de Trabalho**
O caminho clássico de uma nova funcionalidade (Feature) percorre as seguintes categorias:
1.  **Planejamento**: Jira / Trello (Criação do Card/Issue).
2.  **Desenvolvimento**: VS Code + Terminal (Escrever o código).
3.  **Controle de Versão**: Git + GitHub (Salvar e pedir revisão via Pull Request).
4.  **Integração/Testes**: GitHub Actions (Rodar testes automatizados para validar a feature).
5.  **Deploy**: Docker / Nuvem (Entrega do código empacotado para produção).

**4. Automação na Prática**
Um desenvolvedor que precisa renomear 50 imagens (`img_1.jpg`, `img_2.jpg`...) perderia muito tempo fazendo isso pelo mouse (GUI). A automação perfeita seria abrir o **Terminal (CLI)** e usar um comando de repetição (como um laço `for` em Bash ou PowerShell) para renomear todas em fração de segundos, ou um script simples em Python para ler o diretório e modificar os nomes programaticamente.

---

### 🔴 Desafio (Exploração)

**5. Análise de Mercado (Exemplo: Netflix)**
Acessando o StackShare ou Blog de Engenharia da Netflix, encontramos ferramentas como:
1.  **GitHub** (Controle de Versão): Para armazenar o código de seus microsserviços.
2.  **Jenkins / GitHub Actions** (Infra/CI-CD): Para automação das pipelines de deploy.
3.  **Docker / Kubernetes** (Infraestrutura/Orquestração): Para levantar os milhões de contêineres que servem os vídeos.
4.  **Jira** (Gestão de Projetos): Para coordenar as centenas de equipes em sprints ágeis.
5.  **Slack** (Comunicação): Para notificar incidentes no servidor via integrações (ChatOps).

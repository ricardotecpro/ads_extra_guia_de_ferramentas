# Projeto 04 - Inicializando a Máquina do Tempo 🛠️

### 🎯 Objetivo
Praticar o fluxo local do Git, desde a inicialização de um repositório até o salvamento permanente das alterações.

### 📋 Passo a Passo

1.  **Pasta do Projeto**: Crie uma pasta chamada `meu-legacy-projeto`.
2.  **Início do Git**: Via terminal, dentro da pasta, execute:
    ```bash
    git init
    ```
3.  **Configuração de Identidade**: Garanta que seu nome e e-mail estão configurados (`git config --list`).
4.  **Primeiro Arquivo**: Crie um arquivo `index.html` básico.
5.  **Commit Inicial**: Adicione o arquivo à Staging Area e faça o commit:
    ```bash
    git add index.html
    git commit -m "feat: adicionar estrutura inicial dr index.html"
    ```
6.  **Verificação de Histórico**: Execute `git log` e verifique se o seu commit aparece com o código (hash) único.

---
**Entrega**: Um print da tela do terminal mostrando o resultado do comando `git log`.
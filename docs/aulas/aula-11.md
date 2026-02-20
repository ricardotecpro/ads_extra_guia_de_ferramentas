# Aula 11 - CI/CD Moderno (GitHub Actions) 🚀

!!! tip "Objetivo"
    **Objetivo**: Compreender o ciclo de integração e entrega contínua (CI/CD), aprender a criar workflows automatizados no GitHub e garantir que o código seja testado automaticamente a cada push.

---

## 1. O que é CI/CD? 🔄

Em vez de rodar testes e linters manualmente na sua máquina, deixamos que um servidor faça isso por nós sempre que enviamos uma mudança.

*   **CI (Continuous Integration)**: Integrar código de vários devs com frequência, rodando testes automáticos para garantir que nada "quebrou".
*   **CD (Continuous Deployment)**: Se os testes passaram, enviar o código automaticamente para o servidor de produção ou homologação.

---

## 2. GitHub Actions: Automação na Nuvem 🤖

O GitHub Actions é a ferramenta de CI/CD integrada ao GitHub. Ele funciona através de arquivos de configuração no formato **YAML**.

### Componentes do Actions:
1.  **Workflow**: O processo completo (ex: "Build e Teste").
2.  **Event**: O que dispara o processo (ex: um `push` ou um `pull_request`).
3.  **Job**: Uma tarefa específica dentro do workflow (ex: "rodar testes unitários").
4.  **Steps**: Os comandos passo a passo dentro de um Job.

---

## 3. Visualização da Pipeline (Mermaid)

```mermaid
graph LR
    Push[Git Push] --> Trigger{GitHub Event}
    Trigger --> VM[Spin up Virtual Machine]
    VM --> Install[npm install]
    Install --> Lint[npx eslint .]
    Lint --> Test[npm test]
    Test -- Success --> Deploy[Auto Deploy]
    Test -- Failure --> Notify[Notificar Developer]
```

---

## 4. O Arquivo de Configuração (.yml) 📄

Abaixo, um exemplo de como é um arquivo de workflow real:

```yaml
name: Node.js CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
```

---

## 5. Praticando no Terminal (Simulação) 💻

Imagine o terminal do servidor do GitHub executando seu workflow:

```termynal
$ runner-ci --start
Starting Workflow: Node.js CI
Step 1: Checking out code... OK
Step 2: Installing Node 18... OK
Step 3: Running npm install... OK
Step 4: Running npm test... 
 PASS  test/auth.test.js
 PASS  test/db.test.js
Step 5: All tests passed! Pipeline completed.
```

---

## 6. Mini-Projeto: Monitorando um Workflow 🚀

1.  Vá até um repositório seu no GitHub.
2.  Clique na aba **Actions**.
3.  O GitHub sugerirá "Workflows" baseados na sua linguagem.
4.  Escolha um simples (como Node.js ou Python) e clique em **Set up this workflow**.
5.  Clique em **Commit changes**.
6.  Veja o workflow rodar em tempo real e verifique se ele fica "Verde" (Sucesso).

---

## 7. Exercício de Fixação 📝

1.  **Básico**: Qual a principal diferença entre Integração Contínua (CI) e Entrega Contínua (CD)?
2.  **Básico**: Para que serve o evento `on: [pull_request]` em um workflow?
3.  **Intermediário**: Por que é perigoso fazer o Deploy (CD) sem ter uma etapa de Testes (CI) antes?
4.  **Intermediário**: O que acontece com um Pull Request se o workflow de testes falhar?
5.  **Desafio**: Pesquise o que são "GitHub Secrets" e por que nunca devemos colocar senhas diretamente no arquivo `.yml`.

---

**Próxima Aula**: Vamos falar de infraestrutura com [Automação e IaC (Ansible/Terraform)](./aula-12.md)! ⚙️
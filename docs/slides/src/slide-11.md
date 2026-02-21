# Aula 11: CI/CD Moderno (GitHub Actions) 🚀

---

## 🎯 Nossa Missão
*   Entender o que é CI e CD.
*   Conhecer o GitHub Actions.
*   Aprender a sintaxe YAML de workflows.
*   Automatizar o ciclo de vida do código.

---

## 🏗️ O que é CI (Continuous Integration)?
Integrar o código com frequência.
*   Testes automáticos rodam a cada push. { .fragment }
*   Erros de integração são pegos cedo. { .fragment }
*   Garante que a `main` nunca quebre. { .fragment }

---

## 🚚 O que é CD (Continuous Delivery/Deployment)?
Entregar o código pronto para o usuário.
*   **Delivery**: Build pronto para ser lançado (clique manual). { .fragment }
*   **Deployment**: Lançamento 100% automático em produção. { .fragment }

---

## ♾️ O Infinito do DevOps
```mermaid
graph TD
    Plan --> Code --> Build --> Test
    Test --> Release --> Deploy --> Operate
    Operate --> Monitor --> Plan
```

---

## 🐙 Por que GitHub Actions?
*   Integrado ao repositório. { .fragment }
*   Nativamente grátis para repos públicos. { .fragment }
*   Ecossistema gigante de ações prontas. { .fragment }
*   Suporta Linux, Mac e Windows. { .fragment }

---

## 🗂️ A Anatomia do GitHub Actions
1.  **Workflow**: O processo completo (arquivo `.yml`). { .fragment }
2.  **Event (Trigger)**: O que dispara o processo (push, pr). { .fragment }
3.  **Job**: Um conjunto de tarefas em um servidor. { .fragment }
4.  **Step**: Uma tarefa individual (comando ou script). { .fragment }
5.  **Runner**: O servidor virtual que executa tudo. { .fragment }

---

## 📄 O Formato YAML
Yet Another Markup Language.
*   Baseado em indentação (espaços). { .fragment }
*   Muito fácil de ler para humanos. { .fragment }
*   Padrão para ferramentas de DevOps. { .fragment }

---

## 🎯 Gatilhos (Triggers)
Quando a mágica acontece?
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

---

## 🏗️ Definindo o Ambiente (Runner)
Onde seu código vai rodar?
```yaml
jobs:
  meu-teste:
    runs-on: ubuntu-latest
```
*   O GitHub cria uma máquina virtual limpa para você. { .fragment }

---

## 🔨 Passos (Steps)
A lista de tarefas.
```yaml
    steps:
      - uses: actions/checkout@v4
      - name: Rodar Testes
        run: npm test
```
*   `uses`: Usa uma ação pronta da comunidade. { .fragment }
*   `run`: Roda um comando de terminal. { .fragment }

---

## 🤫 Gerenciando Segredos (Secrets)
**NUNCA** escreva senhas no arquivo YAML.
*   Use as **Settings > Secrets** do GitHub. { .fragment }
*   Acesse via: `{% raw %}${{ secrets.MINHA_SENHA }}{% endraw %}`. { .fragment }
*   O log do GitHub esconde o valor automaticamente! { .fragment }

---

## 📉 Visualizando a Pipeline
```mermaid
sequenceDiagram
    participant D as Dev
    participant G as GitHub
    participant R as Runner (Ubuntu)

    D->>G: git push
    G->>G: Detecta Push na main
    G->>R: Inicia Workflow
    R->>R: Checkout Código
    R->>R: Instala Dependências
    R->>R: Roda Testes
    R->>G: Relata Sucesso (CHECK VERDE)
```

---

## 🧩 Actions Marketplace
Não reinvente a roda! Existem ações prontas para:
*   Enviar mensagem no Slack. { .fragment }
*   Fazer deploy na Amazon (AWS). { .fragment }
*   Escritar código no Docker Hub. { .fragment }
*   Login no Firebase. { .fragment }

---

## 🔄 Cache em Pipelines
Economizando tempo (e dinheiro).
*   Você não precisa baixar as bibliotecas (`node_modules`) do zero a cada vez. { .fragment }
*   O Actions pode guardar o cache e acelerar a build em 50%! { .fragment }

---

## 🛡️ Proteção de Branch
Combine Actions com regras de repositório.
*   Impeça o `merge` se a pipeline falhar. { .fragment }
*   Exija pelo menos 1 aprovação de colega (Code Review). { .fragment }

---

## 📉 Artefatos
Onde fica o arquivo final?
*   Você pode salvar o resultado da build (ex: um `.zip` ou um `.apk`) como artefato para download no final do workflow. { .fragment }

---

## 💰 Custos e Limites
*   Gratuito para Open Source. { .fragment }
*   Minutos limitados para repos privados (2000 min/mês no plano free). { .fragment }

---

## 🏆 Checklist de CI/CD Pro
*   [ ] Entende a diferença entre Workflow, Job e Step. { .fragment }
*   [ ] Sabe criar um arquivo `.yml` básico. { .fragment }
*   [ ] Entende o conceito de Secrets. { .fragment }
*   [ ] Consegue visualizar o log de erro no GitHub. { .fragment }

---

## 📝 Prática de Hoje
1.  Criar a pasta `.github/workflows`.
2.  Criar um workflow de "Hello World".
3.  Ver ele rodar na aba "Actions" após o push.

---

## 🏁 Dúvidas?
Automação é o que separa amadores de profissionais! 🚀🚀
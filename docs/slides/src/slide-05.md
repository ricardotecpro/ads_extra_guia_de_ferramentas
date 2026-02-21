# Aula 05: Plataformas de Colaboração 🤝

---

## 🎯 Nossa Missão
*   Levar o código local para a nuvem.
*   Trabalhar em equipe sem sobrescrever o colega.
*   Dominar Pull Requests e Code Review.
*   Conhecer GitHub, GitLab e Bitbucket.

---

## ☁️ Por que usar repositórios remotos?
*   **Backup Seguro**: Se o PC pifar, o código está na nuvem. { .fragment }
*   **Colaboração**: Várias pessoas no mesmo projeto. { .fragment }
*   **Deploy**: Servidores buscam o código de lá. { .fragment }
*   **Portfólio**: Mostrar seu trabalho para o mundo. { .fragment }

---

## 🏢 O Big Three das Plataformas
1.  **GitHub**: A maior e mais social. { .fragment }
2.  **GitLab**: Foco em empresas e CI/CD integrado. { .fragment }
3.  **Bitbucket**: Integração nativa com Jira. { .fragment }

---

## 🔗 Conectando Local com Remoto
`git remote add origin <url-do-servidor>`
*   **origin**: É o apelido padrão do seu servidor remoto. { .fragment }
*   Você pode ter mais de um remoto (ex: `upstream`). { .fragment }

---

## 🚀 Enviando Código: `git push`
O ato de "empurrar" seus commits para a nuvem.
```bash
git push -u origin main
```
*   `-u`: Salva a preferência (upstream), depois basta usar `git push`. { .fragment }

---

## 📥 Trazendo Código: `git pull`
Sincronizando as mudanças que outros fizeram.
*   Executa um `fetch` (busca) + `merge` (une). { .fragment }
*   Mantenha seu código local sempre atualizado! { .fragment }

---

## 👯‍♀️ Clonando um Projeto: `git clone`
Baixando um repositório que já existe online.
*   Cria a pasta, inicia o git e baixa todos os arquivos. { .fragment }
*   Baixa todo o histórico de commits. { .fragment }

---

## 🌳 Trabalhando com Branches
O segredo da colaboração segura.
```mermaid
graph LR
    M((Main)) --- A((Fix A))
    M --- B((Feature B))
    A -.-> M
    B -.-> M
```
*   **Main**: Sempre código funcional e testado. { .fragment }
*   **Features**: Branches para cada tarefa nova. { .fragment }

---

## 🏗️ O Ciclo de Vida de uma Alteração
```mermaid
sequenceDiagram
    participant D as Desenvolvedor
    participant G as GitHub (Cloud)
    participant T as Time (Equipe)

    D->>D: Cria Branch & Commits
    D->>G: git push branch
    D->>G: Abre Pull Request (PR)
    G->>T: Notifica Time
    T->>G: Faz Code Review & Sugestões
    D->>G: Ajusta Código
    G->>G: Merge para Main
```

---

## 📝 O Pull Request (PR)
Não é apenas código, é uma conversa.
*   **Título Claro**: O que isso resolve? { .fragment }
*   **Descrição**: Explique as mudanças complexas. { .fragment }
*   **Prints/Vídeos**: Se houver mudança visual. { .fragment }

---

## 🔍 Code Review: A Etapa de Ouro
Por que revisar código alheio?
*   Encontrar bugs que o autor não viu. { .fragment }
*   Aprender novas técnicas. { .fragment }
*   Garantir a padronização do time. { .fragment }
*   **Seja gentil nas críticas!** { .fragment }

---

## 👯‍♂️ Fork: Colaboração Externa
Muito comum em Open Source.
*   Você cria uma cópia do projeto de outra pessoa na sua conta. { .fragment }
*   Faz as mudanças e envia um PR de volta para o autor original. { .fragment }

---

## 🐙 GitHub: Recursos Sociais
*   **Stars**: Curtir um projeto. { .fragment }
*   **Watch**: Receber notificações de mudanças. { .fragment }
*   **Profile**: Seu currículo visual como dev. { .fragment }

---

## 🛑 Cuidados com a Segurança
*   **NUNCA** envie senhas (`.env`) para o GitHub. { .fragment }
*   Use Chaves SSH para conexão segura sem senha. { .fragment }
*   Ative o Double Factor Authentication (2FA). { .fragment }

---

## ⚠️ Lidando com Conflitos (Remoto)
Se você e um colega mudam a mesma linha:
1.  O `push` será rejeitado. { .fragment }
2.  Você deve fazer `git pull`. { .fragment }
3.  Resolver o conflito localmente. { .fragment }
4.  Fazer novo `add/commit/push`. { .fragment }

---

## 📊 Insights do GitHub
*   **Network Graph**: Visualizar as branches. { .fragment }
*   **Contributors**: Quem mais trabalhou no projeto? { .fragment }
*   **Dependency Graph**: Quais bibliotecas seu código usa? { .fragment }

---

## 🏆 Checklist Pro do Dia
*   [ ] Repositório remoto configurado. { .fragment }
*   [ ] `git push` realizado com sucesso. { .fragment }
*   [ ] Entende o papel de uma Branch de Feature. { .fragment }
*   [ ] Sabe abrir um Pull Request descritivo. { .fragment }

---

## 📝 Prática de Hoje
1.  Criar um Repo Público no GitHub.
2.  Conectar seu projeto local e fazer Push.
3.  Editar online, fazer Pull local.
4.  Simular um PR com um colega.

---

## 🏁 Dúvidas?
O código agora é global! 🌎🚀

# Resolução: Aula 02 - Gestão de Projetos 📊

### 🟢 Básicos (Fixação)

**1. Kanban vs Lista**
O quadro Kanban é visual e espacial. Em uma lista de Word/Excel, é difícil ver instantaneamente em que etapa cada desenvolvedor está trabalhando e onde estão os "gargalos" do projeto. O Kanban traz transparência: todo o time olha para as colunas e sabe exatamente o status do fluxo de trabalho sem precisar perguntar, o que é vital para a comunicação em métodos ágeis (Agile).

**2. Status de Tarefa (Colunas)**
1.  **To Do (A Fazer)**: Onde a tarefa nasce (Backlog). Ninguém está trabalhando nela ainda.
2.  **In Progress (Em Execução)**: O desenvolvedor pega a tarefa para si ("Assigned") e começa a programar.
3.  **Code Review (Revisão)**: O código foi feito, mas outro dev da equipe precisa revisar a lógica para garantir a qualidade antes de aprovar.
4.  **Done (Concluído)**: O código foi revisado, aprovado e entregue para produção.

---

### 🟡 Intermediários (Aplicação)

**3. Priorização**
A regra de ouro é avaliar **Valor para o Cliente** versus **Urgência (Criticidade)**.
*   Bugs que quebram o sistema (ex: tela de login não funciona ou pagamento falhando) têm prioridade absoluta (Prioridade Alta/Blocker).
*   Se os bugs forem apenas visuais (ex: cor de um botão errada), eles devem ficar no "To Do" enquanto as funcionalidades principais ou correções críticas são puxadas para execução.

**4. Integração de Ferramentas**
Usar GitHub Issues permite que a gestão do projeto fique "amarrada" ao código. O desenvolvedor não precisa sair do GitHub (ou do seu terminal) para abrir o Trello em outra aba. Além disso, ao fazer um "Commit" com a mensagem `Fixes #42`, o próprio GitHub fecha o Issue 42 automaticamente quando o código for aceito, criando uma rastreabilidade perfeita entre "o que foi pedido" e "o código que resolveu".

---

### 🔴 Desafio (Exploração)

**5. Simulação de Conflito (Jira/Kanban)**
Ferramentas profissionais de gestão como o Jira operam em tempo real. Se dois devs tentarem puxar o mesmo card, a plataforma atualizará o "Assignee" (Responsável) para o primeiro que clicou, e a foto dele aparecerá no card na tela de todos. Além disso, a gestão ágil prega a "Daily Meeting" (reunião diária), onde os devs se comunicam e declaram: "Hoje vou puxar a tarefa X", evitando retrabalho logo no planejamento da manhã.

---

[**⬅️ Voltar para o Exercício**](./exercicio-02.md)

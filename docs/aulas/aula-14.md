# Aula 14 - Orquestração com Kubernetes e Runners ☸️

!!! tip "Objetivo"
    **Objetivo**: Compreender a necessidade de orquestração de contêineres, conhecer os conceitos básicos de Kubernetes (K8s) e entender como os Runners executam nossas tarefas de automação em larga escala.

---

## 1. O que fazer com 1000 Contêineres? 🤯

O Docker é ótimo para rodar um ou dez contêineres. Mas e se você tiver um sistema gigante com milhares de contêineres que precisam escalar conforme o número de usuários sobe e desce?

### 🧠 Conceito: Orquestração

=== "O Caos Manual"
    Sem orquestração, se um dos 1000 contêineres Docker travar, um humano precisaria rodar `docker restart`. Se o servidor ficar sem memória no meio da madrugada, alguém precisaria comprar outro servidor.
    
=== "O Maestro Kubernetes"
    A Orquestração automatiza o gerenciamento. O **K8s** (Kubernetes) atua como um maestro: ele monitora a saúde das aplicações, reinicia as que falharam ou travaram e aumenta os servidores (Scale Out) quando identificam picos de acessos.

---

## 2. Conceitos Chave do Kubernetes 🏗️

O K8s não fala "contêiner", ele fala **Pod**.

1.  **Pod**: A menor unidade (pode conter um ou mais contêineres).
2.  **Node**: Uma máquina física ou virtual (o "trabalhador") onde os Pods rodam.
3.  **Cluster**: O conjunto de todos os Nodes gerenciados pelo Kubernetes.
4.  **Deployment**: A definição de como o seu app deve rodar (ex: "quero sempre 3 cópias deste Pod ligadas").

### Visualização de um Cluster

```mermaid
graph TD
    Control([Control Plane - O Cérebro]) --> Node1([Node 1])
    Control --> Node2([Node 2])
    subgraph "Node 1"
        Pod1([Pod A])
        Pod2([Pod B])
    end
    subgraph "Node 2"
        Pod3([Pod A])
        Pod4([Pod C])
    end
```

---

## 3. Auto-Cura e Escala Automática 🦾

A grande mágica do Kubernetes é a **Auto-Cura**: se um contêiner travar ou um servidor desligar, o K8s percebe e sobe um novo contêiner em outra máquina automaticamente.

!!! note "Conceito"
    **Horizontal Pod Autoscaler (HPA)**: O K8s pode aumentar o número de Pods se o CPU da sua aplicação estiver muito alto e diminuir quando o tráfego baixar.

---

## 4. O Papel dos Runners 🏃‍♂️

No mundo do CI/CD (que vimos na Aula 11), os **Runners** são os contêineres que "correm" para executar o seu código. No GitHub Actions, o GitHub fornece runners, mas grandes empresas criam seus próprios **Self-hosted Runners** em clusters Kubernetes para ter mais controle e velocidade.

---

## 5. Prática: Lógica de Orquestração 🚀

1.  Imagine que você tem uma loja virtual.
2.  Normalmente, 3 servidores dão conta do recado.
3.  Chega a **Black Friday** e os acessos aumentam 10x.
4.  No seu bloco de notas, desenhe como o Kubernetes deveria agir:
    *   **Passo 1**: Perceber aumento de tráfego.
    *   **Passo 2**: Criar mais 27 cópias dos servidores (totalizando 30).
    *   **Passo 3**: Quando a Black Friday acabar, destruir 27 cópias para economizar dinheiro.

---

## 📝 Prática Sugerida

Para consolidar o conhecimento desta aula, realize os exercícios propostos:

👉 **[Ver Exercícios da Aula 14](../exercicios/exercicio-14.md)**
👉 **[Ver Projeto da Aula 14](../projetos/projeto-14.md)**

---

**Próxima Aula**: Vamos falar sobre como as pessoas se organizam com o [Módulo 4 - Aula 15 - Comunicação e Colaboração em Equipe (Slack/Teams)](./aula-15.md)! 💬


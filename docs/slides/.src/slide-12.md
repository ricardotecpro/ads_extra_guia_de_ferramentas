# Aula 12: Automação e IaC (Ansible e Terraform) ⚙️

---

## 🎯 Nossa Missão
*   Entender o conceito de Infraestrutura como Código (IaC).
*   Provisionamento vs Configuração.
*   Conhecer o Terraform (Estatura).
*   Conhecer o Ansible (Recheio).

---

## 😫 O Mundo Antes do IaC
*   Configuração manual de servidores via SSH. { .fragment }
*   "Qual era a senha mesmo?" { .fragment }
*   "Por que o servidor 1 está diferente do servidor 2?" { .fragment }
*   Impossível de escalar ou repetir com precisão. { .fragment }

---

## 🧠 O que é IaC?
Infraestrutura tratada como software.
*   Versionada no Git. { .fragment }
*   Testável. { .fragment }
*   Repetível (Idempotência). { .fragment }
*   Documentação viva do ambiente. { .fragment }

---

## 🏗️ Provisionar vs Configurar
Uma analogia com culinária:
*   **Provisionar (Terraform)**: É comprar a cozinha, o fogão e as panelas. { .fragment }
*   **Configurar (Ansible)**: É ligar o fogo, colocar os ingredientes e cozinhar. { .fragment }

---

## 🌍 Terraform: O Orquestrador de Nuvem
*   Focado em criar os recursos (VMs, Redes, Bancos). { .fragment }
*   Declarativo: Você diz "O que" quer, não "Como" fazer. { .fragment }
*   Multicloud: AWS, Azure, Google Cloud, DigitalOcean. { .fragment }

---

## 📄 Sintaxe HCL (Terraform)
```hcl
resource "aws_instance" "web_server" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
}
```
*   Fácil de ler e gerenciar. { .fragment }

---

## 🔄 O Ciclo do Terraform
1.  **Write**: Escreve o arquivo `.tf`. { .fragment }
2.  **Plan**: Vê o que vai mudar antes de aplicar. { .fragment }
3.  **Apply**: Executa as mudanças na nuvem. { .fragment }
4.  **Destroy**: Remove tudo de uma vez. { .fragment }

---

## 🍳 Ansible: Automação Simples
*   Agentless: Não precisa instalar nada no servidor alvo (usa SSH). { .fragment }
*   Focado em instalar apps e configurar arquivos. { .fragment }
*   Usa Playbooks em YAML. { .fragment }

---

## 📜 Exemplo de Playbook (Ansible)
```yaml
- name: Instalar Nginx
  hosts: servidores_web
  tasks:
    - name: Garantir que Nginx está instalado
      apt:
        name: nginx
        state: present
```

---

## 🔄 Idempotência: A Regra de Ouro
"Se eu rodar 10 vezes, o resultado final é o mesmo."
*   Se o software já está instalado, o Ansible não faz nada. { .fragment }
*   Garante consistência e evita duplicidade de erros. { .fragment }

---

## 🏗️ Estrutura de Infraestrutura Moderna
```mermaid
graph TD
    Code[Codigo no Git] --> Pipeline[GitHub Actions]
    Pipeline --> TF[Terraform: Cria VM]
    TF --> ANS[Ansible: Instala App]
    ANS --> App[Servidor pronto para uso]
```

---

## 🛡️ Benefícios da Automação
*   **Velocidade**: Criar 100 servidores em minutos. { .fragment }
*   **Consistência**: Todos os ambientes (Dev/Prod) são idênticos. { .fragment }
*   **Disaster Recovery**: Recriar tudo do zero após um erro grave. { .fragment }

---

## 🐚 O Papel do YAML e SSH
*   **YAML**: A língua franca da configuração. { .fragment }
*   **SSH**: A porta de entrada segura para a automação. { .fragment }

---

## 📈 Automação além da Infra
*   Backup de bancos de dados. { .fragment }
*   Limpeza de logs. { .fragment }
*   Atualização de patches de segurança de uma só vez. { .fragment }

---

## 💰 Cloud Computing e IaC
*   **Pay-as-you-go**: Pague só pelo que usa. { .fragment }
*   O IaC ajuda a desligar recursos que não estão sendo usados e economizar dinheiro! { .fragment }

---

## 🕵️‍♂️ Verificação de Conformidade
*   Ferramentas que verificam se a infraestrutura real é igual ao que está no código. { .fragment }
*   Evita o "Desvio de Configuração" (Config Drift). { .fragment }

---

## 🏆 Checklist de Automação Pro
*   [ ] Entende a diferença entre Terraform e Ansible. { .fragment }
*   [ ] Sabe que IaC deve estar no Git. { .fragment }
*   [ ] Entende o conceito de Idempotência. { .fragment }
*   [ ] Conhece o básico da sintaxe YAML. { .fragment }

---

## 📝 Prática de Hoje
1.  Escrever um Playbook Ansible fictício.
2.  Analisar um arquivo de configuração Terraform.
3.  Desenhar o fluxo de criação de um servidor.

---

## 🏁 Dúvidas?
A infraestrutura agora é código! 🚀⚙️
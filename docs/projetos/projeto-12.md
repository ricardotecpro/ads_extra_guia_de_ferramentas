# Projeto 12 - Infraestrutura no Papel ⚙️

### 🎯 Objetivo
Praticar a escrita de arquivos de configuração YAML para automação de servidores, focando na lógica de Infraestrutura como Código.

### 📋 Passo a Passo

1.  **Novo Arquivo**: No VS Code, crie um arquivo chamado `instalar_servidor.yml`.
2.  **Lógica do Ansible**: Escreva um Playbook simples que descreva a instalação de um servidor web. O arquivo deve conter:
    *   Um nome para a jogada (`name`).
    *   Onde será executado (`hosts: localhost`).
    *   Uma lista de tarefas (`tasks`).
3.  **Tarefas Necessárias**:
    *   Instalar o pacote `nginx`.
    *   Copiar um arquivo `index.html`.
    *   Garantir que o `nginx` esteja iniciado.
4.  **Exemplo de Sintaxe**:
    ```yaml
    - name: Configurar WebServer
      hosts: localhost
      tasks:
        - name: Instalar Nginx
          apt: name=nginx state=present
    ```
5.  **Verificação**: Use o VS Code para garantir que não há erros de indentação no seu arquivo YAML.

---
**Entrega**: O conteúdo do seu arquivo `instalar_servidor.yml`.
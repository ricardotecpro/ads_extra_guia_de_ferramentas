# Projeto 06 - Minha Primeira Tabela SQL 💾

### 🎯 Objetivo
Aprender a criar e gerenciar um banco de dados relacional (SQL) usando uma interface universal e comandos básicos.

### 📋 Passo a Passo

1.  **DBeaver Setup**: Abra o **DBeaver** (instalado na Aula 06).
2.  **Conexão SQLite**: Clique em "New Database Connection" e escolha **SQLite**. Crie um arquivo de banco chamado `meu_banco_ads.db`.
3.  **Criação de Tabela**: Abra o Editor SQL e execute o comando:
    ```sql
    CREATE TABLE Ferramentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT
    );
    ```
4.  **Inserção de Dados**: Use a interface visual (Grid) para adicionar 3 ferramentas que você aprendeu até agora (ex: VS Code, Git, Jira).
5.  **Consulta Final**: Execute `SELECT * FROM Ferramentas;` e verifique se as 3 linhas aparecem corretamente.

---
**Entrega**: Um print do DBeaver mostrando a tabela `Ferramentas` preenchida com os 3 dados.
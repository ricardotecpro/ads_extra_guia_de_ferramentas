# Projeto 07 - Modelagem de Documentos JSON ⚡

### 🎯 Objetivo
Entender como os dados são estruturados no mundo NoSQL, utilizando o formato JSON para representar informações complexas de forma flexível.

### 📋 Passo a Passo

1.  **Novo Arquivo JSON**: No VS Code, crie um arquivo chamado `portfolio.json`.
2.  **Estrutura de Dados**: Crie um objeto JSON que contenha:
    *   Seu nome e curso.
    *   Uma lista (`array`) de projetos.
    *   Dentro de cada projeto, uma lista das ferramentas utilizadas.
3.  **Exemplo de Formato**:
    ```json
    {
      "aluno": "Seu Nome",
      "projetos": [
        {
          "titulo": "Calculadora",
          "ferramentas": ["VS Code", "Git", "IntelliJ"]
        }
      ]
    }
    ```
4.  **Validação**: Verifique se todas as chaves estão entre aspas duplas e se não faltam vírgulas.
5.  **Mini-Desafio**: Adicione um campo de data no formato ISO (ex: `"2025-02-19"`) para cada projeto.

---
**Entrega**: O conteúdo do seu arquivo `portfolio.json`.
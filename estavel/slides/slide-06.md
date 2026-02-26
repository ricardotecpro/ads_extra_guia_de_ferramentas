# Aula 06: Bancos de Dados Relacionais 💾

---

## 🎯 Nossa Missão
*   Entender o modelo relacional.
*   Dominar a linguagem SQL básica.
*   Conhecer os principais SGBDs (Postgres, MySQL).
*   Usar ferramentas visuais (DBeaver).

---

## 🤔 O que é um Banco de Dados?
É um sistema organizado para armazenar, gerenciar e recuperar informações.
*   **Persistent**: Os dados ficam lá mesmo se desligar. <!-- .element: class="fragment" -->
*   **Seguro**: Controle de quem pode ver ou mudar. <!-- .element: class="fragment" -->
*   **Escalável**: Suporta de 10 a milhões de linhas. <!-- .element: class="fragment" -->

---

## 🧩 O Modelo Relacional
Imagine uma coleção de planilhas Excel que se conversam.
*   **Tabelas**: Categorias de dados (ex: Usuarios). <!-- .element: class="fragment" -->
*   **Colunas**: Atributos (ex: Nome, Email). <!-- .element: class="fragment" -->
*   **Linhas**: Registros individuais (ex: O usuário João). <!-- .element: class="fragment" -->

---

## 🏗️ Conceitos: Chaves
O segredo da organização.
*   **Primary Key (PK)**: O RG da linha. Único e obrigatório. <!-- .element: class="fragment" -->
*   **Foreign Key (FK)**: O link para outra tabela. Cria a relação. <!-- .element: class="fragment" -->

---

## 🗺️ Exemplo de Tabela
**Tabela: Ferramentas**
| id (PK) | nome | categoria |
| :--- | :--- | :--- |
| 1 | VS Code | Editor |
| 2 | Git | Versionador |
| 3 | Postgres | Banco |

---

## 🗣️ SQL: Structured Query Language
A língua oficial dos bancos relacionais.
*   Não é uma linguagem de programação, é uma linguagem de consulta.
*   Padronizada, mas cada banco tem seu "sotaque".

---

## 🔍 SELECT: Buscando Dados
```sql
SELECT nome, email FROM usuarios;
```
*   O `*` (asterisco) busca todas as colunas. <!-- .element: class="fragment" -->
*   Sempre filtre o que você precisa para não pesar o banco! <!-- .element: class="fragment" -->

---

## 🎯 WHERE: Filtrando Resultados
```sql
SELECT * FROM produtos 
WHERE preco > 100 AND categoria = 'Eletrônicos';
```
*   Operadores: `=`, `>`, `<`, `<>`, `LIKE`, `IN`. <!-- .element: class="fragment" -->

---

## ➕ INSERT: Inserindo Dados
```sql
INSERT INTO categorias (nome) 
VALUES ('Desenvolvimento');
```
*   Lembre-se de respeitar os tipos de dados (Texto vs Número). <!-- .element: class="fragment" -->

---

## 🔄 UPDATE: Alterando Dados
```sql
UPDATE usuarios 
SET nivel = 'Senior' 
WHERE id = 42;
```
*   **Atenção**: Sempre use o `WHERE` ou você vai alterar a tabela inteira! 😱 <!-- .element: class="fragment" -->

---

## ❌ DELETE: Removendo Dados
```sql
DELETE FROM logs 
WHERE data < '2024-01-01';
```
*   **Atenção**: Sem `WHERE`, você apaga tudo! Cuidado redobrado. <!-- .element: class="fragment" -->

---

## 🐘 PostgreSQL: O Elefante Poderoso
*   Open Source e extremamente robusto. <!-- .element: class="fragment" -->
*   Foco em conformidade com padrões e integridade. <!-- .element: class="fragment" -->
*   Suporta tipos complexos (JSON, Geometria). <!-- .element: class="fragment" -->
*   **Queridinho das grandes empresas.** <!-- .element: class="fragment" -->

---

## 🐬 MySQL: A Rapidez da Web
*   Muito popular em sites e blogs (WordPress). <!-- .element: class="fragment" -->
*   Simples de usar e configurar. <!-- .element: class="fragment" -->
*   Atualmente pertence à Oracle, mas tem o fork livre MariaDB. <!-- .element: class="fragment" -->

---

## 🦫 DBeaver: A Interface Universal
Por que usar um GUI Client?
*   Visualizar tabelas como se fossem planilhas. <!-- .element: class="fragment" -->
*   Autocompletar comandos SQL. <!-- .element: class="fragment" -->
*   Gerar diagramas (DER) automaticamente. <!-- .element: class="fragment" -->
*   Exportar dados para Excel/CSV facilmente. <!-- .element: class="fragment" -->

---

## 📐 Modelagem: Normalização
Organizar para não repetir.
*   Evite salvar o nome do país em cada usuário. <!-- .element: class="fragment" -->
*   Crie uma tabela `Paises` e use uma `ID` (FK). <!-- .element: class="fragment" -->
*   Isso economiza espaço e evita erros de digitação. <!-- .element: class="fragment" -->

---

## 📉 Índices: Velocidade de Busca
*   Como o índice de um livro. <!-- .element: class="fragment" -->
*   Acelera muito a busca em tabelas com milhões de linhas. <!-- .element: class="fragment" -->
*   **Custo**: Deixa a inserção um pouco mais lenta. <!-- .element: class="fragment" -->

---

## 🛡️ Transações: Tudo ou Nada (ACID)
Imagine uma transferência bancária:
1.  Tira dinheiro da conta A. <!-- .element: class="fragment" -->
2.  Coloca dinheiro na conta B. <!-- .element: class="fragment" -->
*   Se o passo 2 falhar, o passo 1 deve ser desfeito automaticamente. <!-- .element: class="fragment" -->

---

## 🏆 Checklist de Banco Pro
*   [ ] Entende a diferença entre PK e FK. <!-- .element: class="fragment" -->
*   [ ] Consegue fazer um SELECT com filtro. <!-- .element: class="fragment" -->
*   [ ] Instalou e conectou o DBeaver. <!-- .element: class="fragment" -->
*   [ ] Sabe que rodar DELETE sem WHERE é perigoso. <!-- .element: class="fragment" -->

---

## 📝 Prática de Hoje
1.  Conectar ao banco via DBeaver.
2.  Criar uma tabela `Ferramentas`.
3.  Inserir 3 linhas e fazer um SELECT filtrado.

---

## 🏁 Dúvidas?
O banco de dados é o coração da aplicação! ❤️🚀

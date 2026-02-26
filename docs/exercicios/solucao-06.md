# Resolução: Aula 06 - DB Relacional 💾

### 🟢 Básicos (Fixação)

**1. Criação de Tabelas**
Para modelar uma tabela SQL clássica que receberá novos alunos, o comando seria:
```sql
CREATE TABLE Alunos (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(150),
    Curso VARCHAR(100)
);
```

**2. Consulta Simples**
O comando SQL de "busca" se faz com o operador SELECT, filtrando com a cláusula WHERE:
```sql
SELECT Nome FROM Alunos WHERE Curso = 'ADS';
```

---

### 🟡 Intermediários (Aplicação)

**3. Relacionamentos (Foreign Key)**
Eu não criaria colunas do autor dentro da tabela `Livros` para não repetir os dados dele em todos os livros que escreve. O correto seria colocar na tabela `Livros` apenas o `ID` do autor (ex: coluna `Autor_ID`). Esse `Autor_ID` deve ser obrigatoriamente um valor válido que espelhe a chave primária (`ID`) da tabela de `Autores`. Esse link mágico — a chave que aparente outra tabela — é o que chamamos de **Foreign Key (Chave Estrangeira)**.

**4. DBeaver Workflow**
Acessando o DBeaver: 
1. Clicar com o botão direito na tabela pretendida ("Ex: `Vendas`").
2. "Export Data" (Exportar Dados).
3. Selecionar o destino como "CSV".
Isso é extremamente útil para um desenvolvedor, pois ele pode retirar amostras formatadas de uma base inacessível aos executivos não-técnicos e passar para a equipe de negócios ler e gerar gráficos usando planilhas como Excel ou Power BI.

---

### 🔴 Desafio (Exploração)

**5. Performance de Consulta (Index)**
Um **Índice (Index)** de banco de dados funciona exatamente como o índice no final de uma enciclopédia grossa. Sem ele, para achar informações sobre o mês de Janeiro (`'2023-01-01'`) numa tabela de 10 milhões de linhas, o banco escaneia a tabela de capa a capa de forma exaustiva (*Full Table Scan*). Se eu criar um "Índice", o SQL organiza datas em uma árvore oculta ordenada e salta diretamente para a gaveta onde as de janeiro ficam, transformando uma consulta que levava 1 minuto para meros milissegundos.

---

[**⬅️ Voltar para o Exercício**](./exercicio-06.md)

# Quiz 06

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que significa a sigla SQL?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Simple Query Language.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Structured Query Language (Linguagem de Consulta Estruturada).">Structured Query Language (Linguagem de Consulta Estruturada).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">System Quality Logic.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Standard Quantum List.
    *   *Explicação: SQL é a linguagem padrão para interagir com bancos de dados relacionais.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual o papel de uma "Primary Key" (Chave Primária)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Abrir o banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Identificar de forma única e exclusiva cada registro (linha) em uma tabela.">Identificar de forma única e exclusiva cada registro (linha) em uma tabela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Salvar a senha dos usuários.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Listar os nomes em ordem alfabética.
    *   *Explicação: Não podem existir dois registros com a mesma Chave Primária na mesma tabela.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Qual comando SQL é usado para buscar dados em uma tabela?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`FIND`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! `SELECT`">`SELECT`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`GET`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`SEARCH`
    *   *Explicação: O `SELECT` é a base de todas as consultas em bancos relacionais.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **Sobre o PostgreSQL, é correto afirmar:**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">É uma ferramenta paga de design.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! É um dos SGBDs relacionais mais poderosos, gratuitos e utilizados no mundo.">É um dos SGBDs relacionais mais poderosos, gratuitos e utilizados no mundo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Só funciona em sistemas Windows.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Serve apenas para guardar arquivos de imagem.
    *   *Explicação: O "Postgres" é amplamente respeitado por sua robustez e conformidade com padrões.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **O que é o DBeaver?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um tipo de banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Uma ferramenta visual (Client GUI) que se conecta a vários tipos de bancos de dados.">Uma ferramenta visual (Client GUI) que se conecta a vários tipos de bancos de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma linguagem de programação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um antivírus para servidores.
    *   *Explicação: O DBeaver facilita a vida do dev ao permitir gerenciar bancos graficamente.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **O que faz a cláusula `WHERE` em um comando SQL?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Diz onde o banco de dados deve ser salvo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Filtra os resultados da consulta com base em uma condição.">Filtra os resultados da consulta com base em uma condição.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deleta a tabela inteira.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Muda o nome das colunas.
    *   *Explicação: Ex: `SELECT * FROM usuarios WHERE idade > 18;`*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **Qual a diferença entre SQL e SGBD?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">São sinônimos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! SQL é a linguagem; SGBD é o software que gerencia o banco (ex: MySQL, Postgres).">SQL é a linguagem; SGBD é o software que gerencia o banco (ex: MySQL, Postgres).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">SGBD é o código; SQL é o hardware.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">SQL é para a web; SGBD é para o desktop.
    *   *Explicação: Você usa a linguagem SQL para dar ordens ao software SGBD.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **Para que serve uma "Foreign Key" (Chave Estrangeira)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para permitir o acesso de usuários de outros países.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para criar um relacionamento entre duas tabelas diferentes.">Para criar um relacionamento entre duas tabelas diferentes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para criptografar os dados do banco.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para traduzir o nome das tabelas para inglês.
    *   *Explicação: Ela "liga" um registro de uma tabela a um registro de outra (ex: Pedido ligado a um Cliente).*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **Qual comando é usado para adicionar novos dados a uma tabela?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`ADD`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! `INSERT`">`INSERT`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`SAVE`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`CREATE`
    *   *Explicação: O `INSERT INTO` é usado para criar novas linhas com informações.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Por que usar um Client GUI como o DBeaver em vez de apenas o terminal?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Porque desenvolvedores profissionais não usam terminal.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para visualizar tabelas, diagramas e dados de forma mais rápida e intuitiva.">Para visualizar tabelas, diagramas e dados de forma mais rápida e intuitiva.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Porque o terminal estraga o banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Porque o DBeaver é obrigatório para rodar o SQL.
    *   *Explicação: Ferramentas visuais aumentam a produtividade em tarefas de inspeção e modelagem.*</div>
  <div class="quiz-feedback"></div>
</div>


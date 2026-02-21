# Quiz: Aula 07 - NoSQL e Cache ⚡

1.  **O que significa o termo NoSQL?**
    *   ( ) No (Não) SQL.
    *   (x) Not Only SQL (Não Apenas SQL).
    *   ( ) No Speed Quality Logic.
    *   ( ) New Object Standard Language.
    *   *Explicação: Indica bancos que não seguem o modelo rígido de tabelas e relações do SQL tradicional.*

2.  **Qual a principal característica do MongoDB?**
    *   ( ) Usa apenas tabelas e colunas fixas.
    *   (x) Armazena dados em documentos flexíveis (tipo JSON/BSON).
    *   ( ) Só funciona em servidores de arquivos pequenos.
    *   ( ) É um software pago da Microsoft.
    *   *Explicação: No MongoDB, cada documento pode ter campos diferentes, o que dá muita flexibilidade.*

3.  **Qual a principal vantagem do Redis?**
    *   ( ) É excelente para guardar terabytes de fotos pesadas.
    *   (x) Sua velocidade extrema, pois armazena os dados na Memória RAM.
    *   ( ) Ele substitui a necessidade de usar o Git.
    *   ( ) Ele funciona apenas como um editor de texto.
    *   *Explicação: O Redis é usado para dados que precisam ser acessados em milissegundos.*

4.  **O que é o "Cache" em uma aplicação web?**
    *   ( ) Uma forma de esconder o código do concorrente.
    *   (x) Uma camada de armazenamento temporário rápido para evitar consultas lentas ao banco principal.
    *   ( ) O ato de apagar os cookies do navegador.
    *   ( ) Um comando para acelerar o processador do computador.
    *   *Explicação: O cache "guarda" resultados frequentes para responder o usuário mais rápido.*

5.  **Qual destes bancos é considerado NoSQL do tipo "Chave-Valor"?**
    *   ( ) PostgreSQL.
    *   ( ) MySQL.
    *   (x) Redis.
    *   ( ) MongoDB.
    *   *Explicação: O Redis trabalha essencialmente ligando uma chave única a um valor específico.*

6.  **Sobre a escalabilidade do NoSQL, é correto afirmar:**
    *   ( ) Ele não escala.
    *   (x) Ele é desenhado para escalar horizontalmente (distribuir dados entre vários servidores) facilmente.
    *   ( ) Ele só escala se o servidor for muito caro.
    *   ( ) Ele escala apenas se as tabelas forem pequenas.
    *   *Explicação: NoSQL é o padrão ouro para sistemas que lidam com bilhões de registros (ex: redes sociais).*

7.  **O formato JSON é muito usado no NoSQL porque:**
    *   ( ) É criptografado por padrão.
    *   (x) É leve, fácil de ler para humanos e fácil de processar para máquinas.
    *   ( ) Ele substitui a necessidade de programar.
    *   ( ) É um formato proprietário do Google.
    *   *Explicação: JSON (JavaScript Object Notation) se tornou o padrão de troca de dados na web.*

8.  **Quando você escolheria o MongoDB em vez de um banco SQL (Postgres)?**
    *   ( ) Quando o projeto é muito simples e sem usuários.
    *   (x) Quando a estrutura dos dados muda com frequência ou não é bem definida.
    *   ( ) Quando você precisa de máxima segurança financeira e transacional.
    *   ( ) Quando você não sabe usar SQL.
    *   *Explicação: Para dados desestruturados (logs, perfis sociais), o MongoDB brilha pela flexibilidade.*

9.  **O termo "In-Memory Database" se aplica a qual ferramenta?**
    *   ( ) Docker.
    *   ( ) Git.
    *   (x) Redis.
    *   ( ) Jira.
    *   *Explicação: Significa que os dados ficam na memória volátil (RAM) para acesso ultra rápido.*

10. **O que acontece com os dados no Redis se não houver persistência configurada e o servidor for desligado?**
    *   ( ) Eles continuam lá normalmente.
    *   (x) Eles são perdidos (por estarem na memória RAM).
    *   ( ) Eles são enviados automaticamente para o GitHub.
    *   ( ) O Redis cria uma cópia física em papel.
    *   *Explicação: Sem configuração de "Snapshot" ou "AOF", o Redis limpa ao desligar.*
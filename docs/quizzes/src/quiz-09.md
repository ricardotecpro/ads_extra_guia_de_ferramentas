# Quiz: Aula 09 - Ferramentas de API (Postman / Insomnia) 📡

1.  **Qual o principal objetivo do Postman ou Insomnia?**
    *   ( ) Editar o código fonte do servidor.
    *   (x) Testar e documentar o comportamento de APIs (solicitar e receber dados).
    *   ( ) Criar o design das telas do aplicativo.
    *   ( ) Acelerar a conexão de internet do computador.
    *   *Explicação: São clientes HTTP que permitem simular requisições de frontend sem precisar de uma interface gráfica final.*

2.  **Qual o método HTTP usado para buscar uma lista de dados no servidor?**
    *   ( ) POST.
    *   (x) GET.
    *   ( ) DELETE.
    *   ( ) PATCH.
    *   *Explicação: O GET é o método padrão de consulta de informações.*

3.  **Para que serve o método HTTP `POST`?**
    *   ( ) Para apagar um registro.
    *   (x) Para enviar novos dados e criar um recurso no servidor (ex: cadastrar usuário).
    *   ( ) Para atualizar uma informação parcial.
    *   ( ) Para baixar um arquivo PDF.
    *   *Explicação: O POST envia informações no "Corpo" (Body) da requisição para criação.*

4.  **O que significa um Status Code iniciado em 2xx (ex: 200, 201)?**
    *   ( ) Erro do Servidor.
    *   (x) Sucesso! A requisição foi processada corretamente.
    *   ( ) Erro do Usuário (ex: senha errada).
    *   ( ) O site está em manutenção.
    *   *Explicação: A família 200 indica que a comunicação correu conforme o esperado.*

5.  **Qual Status Code o servidor retorna quando você tenta acessar algo que não existe?**
    *   ( ) 200 OK.
    *   ( ) 500 Internal Error.
    *   (x) 404 Not Found.
    *   ( ) 403 Forbidden.
    *   *Explicação: O 404 é o erro clássico de "página ou recurso não encontrado".*

6.  **O que é o "Request Body" (Corpo da Requisição)?**
    *   ( ) O título do site.
    *   (x) O local onde enviamos os dados complexos (geralmente JSON) em métodos como POST e PUT.
    *   ( ) A lista de erros do desenvolvedor.
    *   ( ) O link do repositório no GitHub.
    *   *Explicação: É no Body que os dados do formulário ou objeto viajam até o servidor.*

7.  **Sobre o método `DELETE`, é correto afirmar:**
    *   ( ) Ele limpa o histórico do navegador.
    *   (x) Ele solicita a remoção de um recurso específico do servidor.
    *   ( ) Ele deve ser usado para buscar dados de usuários.
    *   ( ) Ele é o método mais seguro para enviar senhas.
    *   *Explicação: O DELETE tem a intenção semântica de excluir um dado.*

8.  **Qual a diferença entre erro 401 e 403?**
    *   ( ) Não há diferença.
    *   (x) 401 significa que você não está autenticado (logado); 403 significa que você não tem permissão para aquele recurso específico.
    *   ( ) 401 é erro de rede; 403 é erro de banco de dados.
    *   ( ) 401 é para sites; 403 é para apps mobile.
    *   *Explicação: 401 é "quem é você?"; 403 é "você não pode entrar aqui".*

9.  **O que são os "Headers" (Cabeçalhos) em uma requisição?**
    *   ( ) O título do documento HTML.
    *   (x) Metadados que enviam informações extras (como tipo do conteúdo ou tokens de autenticação).
    *   ( ) O rodapé da página.
    *   ( ) O nome das variáveis do banco de dados.
    *   *Explicação: Headers dizem ao servidor como interpretar os dados que estão chegando.*

10. **Por que usar "Collections" (Coleções) no Postman?**
    *   ( ) Para economizar espaço no computador.
    *   (x) Para organizar e salvar todas as rotas de um projeto, facilitando o teste repetitivo e o trabalho em equipe.
    *   ( ) Para mudar a cor da interface da ferramenta.
    *   ( ) Para substituir a documentação do código.
    *   *Explicação: Collections permitem agrupar requisições por contexto ou projeto.*
# Quiz 09

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **Qual o principal objetivo do Postman ou Insomnia?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Editar o código fonte do servidor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Testar e documentar o comportamento de APIs (solicitar e receber dados).">Testar e documentar o comportamento de APIs (solicitar e receber dados).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Criar o design das telas do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Acelerar a conexão de internet do computador.
    *   *Explicação: São clientes HTTP que permitem simular requisições de frontend sem precisar de uma interface gráfica final.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual o método HTTP usado para buscar uma lista de dados no servidor?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">POST.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! GET.">GET.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">DELETE.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">PATCH.
    *   *Explicação: O GET é o método padrão de consulta de informações.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Para que serve o método HTTP `POST`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para apagar um registro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para enviar novos dados e criar um recurso no servidor (ex: cadastrar usuário).">Para enviar novos dados e criar um recurso no servidor (ex: cadastrar usuário).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para atualizar uma informação parcial.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para baixar um arquivo PDF.
    *   *Explicação: O POST envia informações no "Corpo" (Body) da requisição para criação.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **O que significa um Status Code iniciado em 2xx (ex: 200, 201)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Erro do Servidor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Sucesso! A requisição foi processada corretamente.">Sucesso! A requisição foi processada corretamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Erro do Usuário (ex: senha errada).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O site está em manutenção.
    *   *Explicação: A família 200 indica que a comunicação correu conforme o esperado.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **Qual Status Code o servidor retorna quando você tenta acessar algo que não existe?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">200 OK.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">500 Internal Error.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! 404 Not Found.">404 Not Found.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">403 Forbidden.
    *   *Explicação: O 404 é o erro clássico de "página ou recurso não encontrado".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **O que é o "Request Body" (Corpo da Requisição)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O título do site.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O local onde enviamos os dados complexos (geralmente JSON) em métodos como POST e PUT.">O local onde enviamos os dados complexos (geralmente JSON) em métodos como POST e PUT.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">A lista de erros do desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O link do repositório no GitHub.
    *   *Explicação: É no Body que os dados do formulário ou objeto viajam até o servidor.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **Sobre o método `DELETE`, é correto afirmar:**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele limpa o histórico do navegador.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Ele solicita a remoção de um recurso específico do servidor.">Ele solicita a remoção de um recurso específico do servidor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele deve ser usado para buscar dados de usuários.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele é o método mais seguro para enviar senhas.
    *   *Explicação: O DELETE tem a intenção semântica de excluir um dado.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **Qual a diferença entre erro 401 e 403?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não há diferença.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! 401 significa que você não está autenticado (logado); 403 significa que você não tem permissão para aquele recurso específico.">401 significa que você não está autenticado (logado); 403 significa que você não tem permissão para aquele recurso específico.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">401 é erro de rede; 403 é erro de banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">401 é para sites; 403 é para apps mobile.
    *   *Explicação: 401 é "quem é você?"; 403 é "você não pode entrar aqui".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **O que são os "Headers" (Cabeçalhos) em uma requisição?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O título do documento HTML.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Metadados que enviam informações extras (como tipo do conteúdo ou tokens de autenticação).">Metadados que enviam informações extras (como tipo do conteúdo ou tokens de autenticação).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O rodapé da página.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome das variáveis do banco de dados.
    *   *Explicação: Headers dizem ao servidor como interpretar os dados que estão chegando.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Por que usar "Collections" (Coleções) no Postman?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para economizar espaço no computador.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para organizar e salvar todas as rotas de um projeto, facilitando o teste repetitivo e o trabalho em equipe.">Para organizar e salvar todas as rotas de um projeto, facilitando o teste repetitivo e o trabalho em equipe.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para mudar a cor da interface da ferramenta.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para substituir a documentação do código.
    *   *Explicação: Collections permitem agrupar requisições por contexto ou projeto.*</div>
  <div class="quiz-feedback"></div>
</div>


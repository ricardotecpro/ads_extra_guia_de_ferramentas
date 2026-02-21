# Aula 09: Ferramentas de API (Postman / Insomnia) 📡

---

## 🎯 Nossa Missão
*   Entender o que é uma API e como ela se comunica.
*   Dominar os métodos HTTP (GET, POST, etc.).
*   Decifrar os códigos de status (200, 404, 500).
*   Usar Clients HTTP como Postman e Insomnia.

---

## 🔌 O que é uma API?
Application Programming Interface.
*   O "garçom" que leva seu pedido ao servidor e traz a resposta. <!-- .element: class="fragment" -->
*   Permite que sistemas diferentes falem a mesma língua. <!-- .element: class="fragment" -->
*   **Exemplo**: Seu app de clima buscando dados do satélite. <!-- .element: class="fragment" -->

---

## 🏗️ Anatomia de uma Requisição
```mermaid
graph LR
    U[URL / EndPoint] --- M[Metodo HTTP]
    M --- H[Headers]
    H --- B[Body / JSON]
```

---

## 🛤️ Endpoints: O Caminho
*   `https://api.loja.com/v1/produtos` <!-- .element: class="fragment" -->
*   `https://api.loja.com/v1/usuarios/123` <!-- .element: class="fragment" -->
*   É o endereço específico onde o recurso mora. <!-- .element: class="fragment" -->

---

## 🛠️ Métodos HTTP: Os Verbos
O que você quer fazer com o dado?
*   **GET**: Buscar informações. <!-- .element: class="fragment" -->
*   **POST**: Criar algo novo. <!-- .element: class="fragment" -->
*   **PUT**: Atualizar algo existente (completo). <!-- .element: class="fragment" -->
*   **PATCH**: Atualizar algo existente (parcial). <!-- .element: class="fragment" -->
*   **DELETE**: Remover algo. <!-- .element: class="fragment" -->

---

## 📦 O Request Body (JSON)
Em métodos como POST e PUT, enviamos dados.
```json
{
  "nome": "Smartphone X",
  "preco": 1500.00,
  "cor": "Preto"
}
```
*   **JSON** é o padrão de ouro da web moderna. <!-- .element: class="fragment" -->

---

## 🆔 Headers: Informações Extras
*   `Content-Type: application/json` <!-- .element: class="fragment" -->
*   `Authorization: Bearer <TOKEN>` <!-- .element: class="fragment" -->
*   Dizem ao servidor quem você é e o que está enviando. <!-- .element: class="fragment" -->

---

## 🚦 Status Codes: A Resposta
Como saber se deu certo?
*   **2xx (Sucesso)**: 200 OK, 201 Created. <!-- .element: class="fragment" -->
*   **3xx (Redirecionamento)**: 301 Moved. <!-- .element: class="fragment" -->
*   **4xx (Erro do Cliente)**: 404 Not Found, 401 Unauthorized. <!-- .element: class="fragment" -->
*   **5xx (Erro do Servidor)**: 500 Internal Error. <!-- .element: class="fragment" -->

---

## 🟠 Postman / 🟣 Insomnia
Clients HTTP que facilitam a vida.
*   Não precisa de frontend para testar o backend. <!-- .element: class="fragment" -->
*   Organize requisições em **Collections**. <!-- .element: class="fragment" -->
*   Automatize testes de resposta. <!-- .element: class="fragment" -->
*   Gere documentação automática. <!-- .element: class="fragment" -->

---

## 🌍 O Fluxo da Requisição
```mermaid
sequenceDiagram
    participant C as Cliente (Postman)
    participant S as Servidor (API)
    participant B as Banco de Dados

    C->>S: GET /produtos (Request)
    S->>B: SELECT * FROM produtos
    B->>S: Dados dos produtos
    S->>C: 200 OK + JSON (Response)
```

---

## 🛡️ Autenticação em APIs
Sua API não pode ser aberta para qualquer um!
*   **API Keys**: Chaves simples. <!-- .element: class="fragment" -->
*   **OAuth2**: Padrão de apps grandes (Google/GitHub). <!-- .element: class="fragment" -->
*   **JWT (JSON Web Token)**: O token que viaja no Header. <!-- .element: class="fragment" -->

---

## 📂 Organização em Coleções
*   Agrupe por projeto ou por funcionalidade. <!-- .element: class="fragment" -->
*   Use **Variáveis de Ambiente** (`{{url}}`). <!-- .element: class="fragment" -->
*   Mude de "Localhost" para "Produção" com um clique! <!-- .element: class="fragment" -->

---

## 📝 Documentação: Swagger e Open API
*   Seu colega de frontend precisa saber como usar sua API. <!-- .element: class="fragment" -->
*   O Swagger gera uma página interativa para testes. <!-- .element: class="fragment" -->
*   O Postman também permite publicar documentação. <!-- .element: class="fragment" -->

---

## 🔍 Query Parameters
Filtrando o que você busca via URL.
*   `api.com/v1/produtos?categoria=livros&ordem=preco` <!-- .element: class="fragment" -->
*   Tudo após o `?` são parâmetros de consulta. <!-- .element: class="fragment" -->

---

## 🗃️ Path Parameters
Identificando um recurso específico.
*   `api.com/v1/usuarios/42` <!-- .element: class="fragment" -->
*   O `42` é o ID dinâmico do usuário buscado. <!-- .element: class="fragment" -->

---

## 🦁 Scripts e Testes no Postman
Você pode validar se o retorno foi correto automaticamente!
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Resposta deve ser JSON", function () {
    pm.response.to.be.json;
});
```

---

## 📉 Mock Servers: Agilidade
*   O backend ainda não está pronto? <!-- .element: class="fragment" -->
*   O Postman cria um servidor "mentira" (Mock). <!-- .element: class="fragment" -->
*   O frontend já pode começar a trabalhar com dados fakes! <!-- .element: class="fragment" -->

---

## 🏆 Checklist de API Pro
*   [ ] Conhece os significados de 200, 201, 400, 404 e 500. <!-- .element: class="fragment" -->
*   [ ] Sabe a diferença entre GET, POST, PUT e DELETE. <!-- .element: class="fragment" -->
*   [ ] Criou sua primeira Collection no Postman/Insomnia. <!-- .element: class="fragment" -->
*   [ ] Entende o papel do JSON no Request Body. <!-- .element: class="fragment" -->

---

## 📝 Prática de Hoje
1.  Abrir o Postman ou Insomnia.
2.  Testar o endpoint da PokeAPI ou JSONPlaceholder.
3.  Analisar o JSON retornado e o Status Code.

---

## 🏁 Dúvidas?
Conectar sistemas é o que move a internet! 🚀📡

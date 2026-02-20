# Projeto 09 - Testando uma API Pública 📡

### 🎯 Objetivo
Praticar o uso de clients HTTP para fazer requisições a uma API real, entender os Status Codes e analisar a estrutura de resposta JSON.

### 📋 Passo a Passo

1.  **Ferramenta**: Abra o **Postman** ou **Insomnia**.
2.  **Requisição GET**: Configure uma requisição para a URL: `https://jsonplaceholder.typicode.com/posts/1`.
3.  **Análise de Resposta**:
    *   Verifique se o Status Code foi `200 OK`.
    *   Identifique os campos `userId`, `id`, `title` e `body`.
4.  **Parâmetros de Query**: Tente filtrar os posts por usuário adicionando um parâmetro: `https://jsonplaceholder.typicode.com/posts?userId=1`. Quantos posts retornaram?
5.  **Requisição POST**: Tente criar um post fictício enviando um JSON no **Body** (formato raw > JSON) com um título e um corpo. Verifique se o retorno é `201 Created`.

---
**Entrega**: Um print do Postman mostrando o resultado da sua requisição POST com sucesso.
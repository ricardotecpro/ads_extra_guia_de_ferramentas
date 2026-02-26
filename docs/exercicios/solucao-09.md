# Resolução: Aula 09 - Ferramentas de API 📡

### 🟢 Básicos (Fixação)

**1. Status Codes**
Receber um **201 Created** é tecnicamente *melhor*, ou seja, mais útil pelo aspecto semântico. Ambos atestam que o servidor processou sem falhar a sua requisição (família 200 de sucesso). A especificidade do 201 informa precisamente ao cliente que o recurso desejado (o usuário) foi efetivamente salvo e inserido no banco de dados, enriquecendo o diálogo do protocolo HTTP.

**2. Mapeamento de Verbos**
*   **a) Mudar preço**: `PATCH` (modifica apenas um campo do produto) ou `PUT` (sobrescreve o produto inteiro).
*   **b) Lista de categorias**: `GET` (busca dados para leitura sem efeitos ou manipulações).
*   **c) Apagar um comentário**: `DELETE` (verbo de deleção direta em um ID).

---

### 🟡 Intermediários (Aplicação)

**3. JSON no Body**
```json
{
  "titulo": "Comprar pão",
  "descricao": "Ir na padaria e comprar 5 pães franceses quentinhos.",
  "prioridade": "Alta"
}
```

**4. Integração Postman**
Quando um projeto atinge o nível de 50 rotas (endpoints), montar os formulários de autenticação, corpo JSON e URL na mão é exaustivo. Uma **Collection** agrupa e organiza, num sistema de pastas, todos esses 50 testes salvos. Se você repassar a collection para o novo recruta da equipe, o Postman de desktop dele terá o ambiente devidamente parametrizado no minuto seguinte, sem refações de trabalho.

---

### 🔴 Desafio (Exploração)

**5. Autenticação e Headers**
O *Header Authorization* é um metadado mandatório, invisível ao layout gráfico comum, levado na "cabeça" do protocolo de internet da sua tela até o servidor. O Postman o anexa ativamente em variáveis como o *Bearer Token*. Evitamos mandar senhas textuais em corpos de formulário nas milhares de idas e vindas de requisição pois: 1. O Token expira logo se for roubado. 2. A senha viajando legível infinitamente expõe os ecossistemas num sniffer virtual. 3. O Token concede delimitação de domínios (*Access Scopes*).

---

[**⬅️ Voltar para o Exercício**](./exercicio-09.md)

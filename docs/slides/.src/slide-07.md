# Aula 07: NoSQL e Cache ⚡

---

## 🎯 Nossa Missão
*   Entender quando o SQL não é suficiente.
*   Conhecer o modelo de Documentos (MongoDB).
*   Dominar o conceito de Cache (Redis).
*   Escalabilidade Horizontal: Pensando grande.

---

## 🦖 O limite do Relacional
Bancos SQL são incríveis, mas:
*   Esquema rígido (alterar tabela é lento). { .fragment }
*   Dificuldade em escalar para bilhões de linhas. { .fragment }
*   Lentidão em requisições repetitivas. { .fragment }
*   **O NoSQL resolve esses gargalos.** { .fragment }

---

## 🧠 O que é NoSQL?
*   **Not Only SQL**. { .fragment }
*   Não usa obrigatoriamente tabelas e colunas. { .fragment }
*   Foco em performance e flexibilidade. { .fragment }
*   Padrão para Big Data e Redes Sociais. { .fragment }

---

## 📂 Tipos de NoSQL
1.  **Documentos**: MongoDB (tipo JSON). { .fragment }
2.  **Chave-Valor**: Redis (ultra rápido). { .fragment }
3.  **Grafos**: Neo4j (relacionamentos complexos). { .fragment }
4.  **Colunares**: Cassandra (dados massivos). { .fragment }

---

## 🍃 MongoDB: O Rei dos Documentos
Em vez de Linhas, usamos **Documentos**.
Em vez de Tabelas, usamos **Collections**.
```json
{
  "_id": "abc123",
  "nome": "João",
  "habilidades": ["Git", "Docker"],
  "ativo": true
}
```

---

## 📐 Por que usar Documentos?
*   **Flexibilidade**: Um documento pode ser diferente do outro. { .fragment }
*   **Agilidade**: Ótimo para MVPs e dados desestruturados. { .fragment }
*   **Hierarquia**: Você pode anular objetos dentro de objetos. { .fragment }

---

## ⚡ Redis: Velocidade Extrema
*   **In-Memory**: Os dados ficam na RAM, não no HD. { .fragment }
*   **Latência**: Respostas em milissegundos. { .fragment }
*   **Estrutura**: Chave-Valor simples. { .fragment }

---

## 🧊 O Conceito de Cache
```mermaid
graph TD
    User[Usuário] --> App[Aplicação]
    App -- 1. Tem no Cache? --> Redis{Redis}
    Redis -- Sim --> User
    Redis -- Não --> DB[(Banco Postgres)]
    DB --> App
    App -- 2. Salva no Cache --> Redis
```

---

## 🕑 Expiração de Dados (TTL)
No cache, os dados não vivem para sempre.
*   `SET token "abc" EX 3600` (Valido por 1 hora). { .fragment }
*   Evita que o cache fique lotado de lixo antigo. { .fragment }
*   Ideal para sessões de login e tokens. { .fragment }

---

## 🪜 Escalabilidade: Vertical vs Horizontal
```mermaid
graph TD
    V[Vertical: Aumentar o Servidor]
    H[Horizontal: Adicionar + Servidores]
    V --- Cost[Custo Exponencial]
    H --- Scale[Escala Infinita]
```
*   NoSQL é mestre na escalabilidade **Horizontal**. { .fragment }

---

## 🌐 Onde usar cada um?
*   **E-commerce (Carrinho)**: Redis. { .fragment }
*   **Rede Social (Posts/Feeds)**: MongoDB. { .fragment }
*   **Financeiro (Transações)**: Postgres (SQL). { .fragment }
*   **Logs**: ElasticSearch. { .fragment }

---

## 🔄 Consistência Eventual
O "problema" do NoSQL.
*   Em sistemas gigantes, pode levar milissegundos para o dado sincronizar em todos os servidores. { .fragment }
*   **Exemplo**: O número de likes de uma foto pode variar um pouco entre usuários por instantes. { .fragment }

---

## 🪟 Ferramentas Visuais
*   **MongoDB Compass**: Explorar documentos visualmente. { .fragment }
*   **Beekeeper Studio**: Client moderno para NoSQL e SQL. { .fragment }
*   **Redis Insight**: Monitorar o uso de memória. { .fragment }

---

## 🚀 Performance na Prática
Imagine buscar o perfil de um usuário famoso:
*   No SQL: 50ms (muitos joins). { .fragment }
*   No NoSQL: 10ms (objeto pronto). { .fragment }
*   No Cache: 1ms (direto da RAM). { .fragment }

---

## 📦 Modelagem no MongoDB
"Embed" (Embutir) vs "Link" (Referenciar).
*   Se os dados mudam pouco, salve dentro do documento. { .fragment }
*   Se os dados são gigantes, use a ID (referência). { .fragment }

---

## 🛡️ Quando NÃO usar NoSQL?
*   Quando a integridade dos dados e relações complexas são críticas. { .fragment }
*   Sistemas contábeis e ERPs tradicionais. { .fragment }
*   Quando você não tem volume de dados que justifique a troca. { .fragment }

---

## 📈 O Futuro: Multi-Model
Bancos modernos (como Postgres) já suportam campos JSON.
*   A linha entre SQL e NoSQL está ficando cada vez mais tênue! { .fragment }

---

## 🏆 Checklist NoSQL Pro
*   [ ] Entende o formato JSON/Documento. { .fragment }
*   [ ] Sabe explicar para que serve o Cache. { .fragment }
*   [ ] Reconhece que Redis vive na Memória RAM. { .fragment }
*   [ ] Diferencia escala vertical de horizontal. { .fragment }

---

## 📝 Prática de Hoje
1.  Criar um documento JSON de perfil.
2.  Instalar o MongoDB localmente.
3.  Simular um cenário de cache para uma notícia famosa.

---

## 🏁 Dúvidas?
Otimize seu app para milhões de usuários! 🚀⚡

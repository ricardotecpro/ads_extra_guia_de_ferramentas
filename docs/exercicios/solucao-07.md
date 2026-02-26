# Resolução: Aula 07 - NoSQL e Cache ⚡

### 🟢 Básicos (Fixação)

**1. JSON Schema**
As marcações em chaves, com strings isoladas entre aspas para atributos e colchetes para vetores marcam o formato JSON universal:
```json
{
  "marca": "Samsung",
  "modelo": "S23",
  "ano": 2023,
  "recursos": [
    "Câmera 48MP",
    "Bateria 5000mAh",
    "NFC"
  ]
}
```

**2. Identificação de Uso**
Aplicativos onde a latência ultra-baixa reflete diretamente na emoção e na usabilidade dos clientes. Por exemplo: A cotação do mercado financeiro e de *criptomoedas* ao vivo (onde 1 segundo dá muita diferença), ou um grupo de mensagens com milhares de participantes que exigem ver envios textuais em alta prioridade via tela de smartphone. O Redis os mantém salvos direto na RAM momentaneamente (Cache).

---

### 🟡 Intermediários (Aplicação)

**3. Comparativo Técnico**
Comentários são documentos amorfos: algumas pessoas enviam gifs, outras enviam arquivos de texto com 3 folhas, formatação *rich*, avatares colados etc. Criar e manter colunas no banco MySQL causaria enrijecimento no tráfego altíssimo pelas verificações duras de Foreign Key. O **MongoDB** não apenas aceita documentos "sem estrutura rígida" (schema-less), como é programado para espalhar seus dados por diversos servidores na horizontal facilmente para absorver os milhões de leitores daquele blog instantaneamente.

**4. Comandos Redis**
Podemos executar ambos os procedimentos em uma única entrada parametrizada (no CLI do Redis, os dados textuais entram como pares de chaves simples e expirações (`EX` em segundos):
```redis
SET user:1 "Joao" EX 60
```
Isso guardou `'Joao'` e programou ele para expirar (se autodestruir) em 60 segundos.

---

### 🔴 Desafio (Exploração)

**5. Arquitetura Híbrida**
Nessa mescla (A Receita de Ouro), nós utilizamos a força garantida matemática de bancos SQL somada ao Cache temporário de RAM do banco Redis. 
**O Fluxo**: O usuário pede informações do seu perfil. A CPU do servidor pesquisa PRIMEIRO na memória temporária super-veloz (Redis). Caso não exista a informação (isso é o famoso *Cache Miss*), a CPU avisa: "Ok, precisaremos bater à porta do Postgres." Dessa forma, vai até o Postgres (que roda em disco, de forma duradoura mas demorada), puxa a leitura e envia o perfil do cara no site... entretanto... **Antes de despachar isso**, nós salvamos o resultado da query na memória do Redis de novo! Se o usuário de fato pedir o mesmo pacote em cinco minutos depois? O Redis já possui o dado (*Cache Hit*) e serve de forma cem vezes mais célere sem estressar a máquina principal.

---

[**⬅️ Voltar para o Exercício**](./exercicio-07.md)

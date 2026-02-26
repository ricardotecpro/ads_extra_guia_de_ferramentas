# Resolução: Aula 11 - CI/CD Moderno 🚀

### 🟢 Básicos (Fixação)

**1. Conceito de Pipeline**
Ao invés do envio caótico manual do seu notebook direto para o Data Center, o código entra na **Continuous Integration (CI)**: um computador "Robô" na nuvem (GitHub Actions/Jenkins) baixa sua arte, compila, resolve as bibliotecas de pacote (ex: `npm install`), execta com unhas de ferro todos os testes e linters em 2 minutos. Com luz verde, procede-se o  **Continuous Delivery (CD)**: o executor compila em formato de contêiner ou binário otimizado, joga a pasta na nuvem final com chaves sigilosas, reinicia a malha de rede em produção ou reverte automaticamente perante erros críticos de subida. 

**2. Eventos do GitHub**
*   O evento `push`: Aciona o pipeline cada e toda bendita vez que você interage salvando em linha reta com a ramagem. É usado comumente nos ambientes "dev" apenas para atestar funcionalidade de pacote e testes em tempo real da tua produção do dia.
*   O evento `pull_request`: Age como juiz do guardião. O pipeline não opera ao acaso, só tracionando nos momentos sacros de tentativa de `Merge` num projeto vital (impedindo a incorporação de bugs num repositório *Master/Main* partilhado perante os mantenedores chefes em tempo limite de revisão).

---

### 🟡 Intermediários (Aplicação)

**3. Falha na Integração**
Completamente impedido (*Blocked on Rules*). O pressuposto principal que financia o maquinário de CI é o estabelecimento da malha fina de falhas; caso ele não sirva como barreira física (Branch Protection Rule), toda a engenharia seria inócuo "perfumaria" com testes falsos ignorados, esvaziando a integridade do código que corrompe as bases centrais. 

**4. YAML Syntax**
A sintaxe hierárquica base original das automações Github não lida textualizada no singular; um ciclo (*Job*) de execução engloba passos em profusão, e de tal forma a declaração matriz deveria evocar listagem (array) pluralizada na key correspondente: `steps:`.

---

### 🔴 Desafio (Exploração)

**5. Matriz de Testes (Build Matrix)**
Criar uma "Build Matrix" exime o mantenedor de redigir longos 3 *Jobs* e scripts isolados massivos caso um projeto (como o próprio NodeJS) precise rodar e atestar estabilidade cruzada em Microsoft Windows, CentOS GNU/Linux e MacOSX. Através de um array indexado no `.yml` (tipo `os: [ubuntu-latest, windows-latest, macos-latest]`), o Github lê o comando solitário multiplicando virtualmente a execução paralelizada criando 3 Máquinas instantâneas operacionais a partir das regras básicas. Isso poupa 80% do texto base scriptado, conferindo escalabilidade de automação para testadores.

---

[**⬅️ Voltar para o Exercício**](./exercicio-11.md)

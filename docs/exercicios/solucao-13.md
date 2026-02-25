# Resolução: Aula 13 - Docker e Docker Compose 📦

### 🟢 Básicos (Fixação)

**1. Analogia de Contêiner**
O contêiner original de aço mudou os portos pois os estivadores não precisavam mais empacotar mil coisas soltas (caixas, sacos de café, barris) no navio; fechava-se toda mercadoria numa caixa padronizada garantida de caber na embarcação. O software ganha a mesma "padronização universal de execução". Quer o seu software seja um banco PostgreSQL em C, uma API Node ou um serviço em Python, as máquinas executoras só verão um "quadrado padrão estanque", e o executarão blindado sem contaminar ou depender dos pacotes nativos corrompidos da máquina servidora.

**2. Imagens vs Contêineres**
Não compartilharão dados em tempo de processamento. A **Imagem** que você baixou é a "planta do prédio" e os **Contêineres** são instâncias de 3 prédios vivos construídos espelhados dessa planta. O dado de inserção do Contêiner A não refletirá no Contêiner B pois eles processam sob amarras estritas e isoladas por regras rígidas de kernel do Docker. 

---

### 🟡 Intermediários (Aplicação)

**3. Docker Compose**
Trabalhar com componentes micro servidos exige regras pesadas de intercomunicação na virtualização de rede (ex: `docker run --network minha_rede...`). O Compose elimina a bagunça do terminal shell; toda a arquitetura transita para um manuscrito `.yml` imutável. Um singelo `docker-compose up` criará com elegância as pontes da network provada e ligará API e DB com laços resolutos e interconectados de nomes que podem ser passados via versão nos repositórios git.

**4. Mapeamento de Portas**
A sintaxe lida com *Host:Container*. Portanto ao evocar `8080:80`, bateremos via web browser na porta `http://localhost:8080` do nosso PC (Host hospedeiro), que roteará no escuro essa requisição para a porta `:80` (dentro) da redoma operante Nginx.
Caso o dev usasse o genérico `80:80`, as requisições cairiam na interface limpa de http. Isso falharia com colapso ("Bind Error") caso a nossa máquina servidora já albergasse um Apache rodando solto pela 80.

---

### 🔴 Desafio (Exploração)

**5. Persistência com Volumes**
A anatomia do Contêiner prega "efemeridade" (ser inato para morrer e renascer em limpeza de kernel pura). Isso é terrível para um SGBD onde cadastramos usuários vitais. O recurso **Docker Volumes** prega-se contornando a malha restritiva mapeando uma "pasta no disco físico exterior inabalável" (`/var/meus_dados_c:\`) diretamente e transparentemente numa "pasta virtual frágil" lá dentro no Docker (`/var/lib/postgresql/data`). A aplicação gravará os zeros e uns no falso interior iludida, repassando o chumbo na pedra duradoura física. Quando o contêiner colapsar ou atualizar imagem, a pasta enraizada persevera as gravações seguras para serem reacopladas em continentes novos.

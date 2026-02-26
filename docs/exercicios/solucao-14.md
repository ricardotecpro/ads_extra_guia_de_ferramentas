# Resolução: Aula 14 - Orquestração com Kubernetes ☸️

### 🟢 Básicos (Fixação)

**1. Escalabilidade**
Quando os microsserviços do ecosistema ultrapassaram a governança da simples visualização unitária via Compose. O Docker gerenciará excelentemente cinco serviços em servidor estrito. Mas ao gerenciar a explosão tráfega da *Black Friday*, com picos necessitando subidas e balanceamento dinâmico sem intervenção humana para dezena de servidores AWS paralelos espalhados atestados por health check de segundos de latência, nós atingimos a barreira funcional solitária. Entra o Orquestrador K8s. 

**2. Pod vs Node**
*   **Node (Nó)**: É a chapa fria computacional em si; o servidor ou máquina virtual Amazon/Google (com GPU, RAM, vCpus).
*   **Pod**: Unidade lógica orgânica mínima e envolvente do K8s (o saquinho orgânico onde circulam um a três contêineres colados de Docker estritos operantes servindo uma única função acoplada). Portanto, os imensos **Nodes** alojam/albergam e instanciam fisicamente centenas de pequenos **Pods**.

---

### 🟡 Intermediários (Aplicação)

**3. Auto-Cura (Self-Healing)**
O "Control Plane" operará a mágica analítica de "Desejado" versus "Real". Se você definiu no artefato Kubernetes que almeja **Três** pods do site ativos de guarda, o ReplicaSet sondará em loops eternos via Pings e Metrics os referidos saquinhos virtuais (Health check probes). Falido o ping no container A via travamentos generalizados em rede, ele não tentará reanimar o zumbi de forma ineficaz; matará ele completamente e re-solicitará o provisionamento imediato de uma cópia impecável noutra ala atestando de novo as "Três instâncias" imaculadas sem nenhum humano avistando. 

**4. Disponibilidade (Nodes)**
A tolerância a intempéries de hardware (Incêndio florestal atinge CPD e cessa um Node VM físico na Amazon) causa mortandade de massa instestinal (os Pods que residiam na máquina pulverizam). Clusterizando no mínimo em malha cruzada de 2 Nodes distintos, o Control plane que habita soberano redireciona requisições imediatamente pela portagem de Ingress roteador para o Node B saudável (que já possuía cópias dos seus pods) neutralizando interrupções de tráfego sistêmico nos acessos VIP.

---

### 🔴 Desafio (Exploração)

**5. O Ecossistema K8s (Pronto para estudos local)**
Estudantes e freelancers que carecem faturar orçamentos trilionários aliciando *EKS/GKE* atestam doções enxutas de emulação nativa como as ferramentas do tipo **Minikube** ou a tecnologia atrativa **Kind (Kubernetes in Docker)**. O truque base dessa segunda versão provê a simulação orgânica enganadora de arquitetura clusterizada multi-nodes pesada operando como efêmeros "nózinhos leves" confinados nas jaulas já conhecidas dos docker contêineres nativos rodando na interface básica de desktops 8GB RAM de discentes.

---

[**⬅️ Voltar para o Exercício**](./exercicio-14.md)

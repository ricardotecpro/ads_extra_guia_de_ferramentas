# Resolução: Aula 12 - Automação e IaC ⚙️

### 🟢 Básicos (Fixação)

**1. Diferenciação de Papéis**
*   Para alocar IP's das redes, balanceadores e materializar 5 esquadras (instâncias "casca/ferro") na Amazon Cloud **Terraform** deve atuar no front processando chamadas API infraestruturais de criação crua no Datacenter.
*   Ao acessar a massa estática já acesa de forma crua, visando manipular permissões de log, descarregar frameworks nativos de **Python** ou criar os daemons contínuos das portas Linux, utilizamos a gerência interna do **Ansible**. 

**2. Vantagem do IaC**
Imutabilidade garantida e rastreabilidade total (Git Commit Logs). Ao perder o engajamento humano das anotações (que esquecem de refazer uma regra no iptables ou erram um prefixo na digitação estressada as de madrugada), o engenheiro invoca instâncias na precisão matemática do arquivo base; e ao cometerem injeções falhas de segurança de rede o arquiteto rolará no tempo através da reversibilidade de re-aplicar o arquivamento testado *IaC* do dia anterior perfeitamente livre da memória corrompida do servidor.

---

### 🟡 Intermediários (Aplicação)

**3. Playbooks do Ansible**
O Ansible destaca-se da velha guarda de gerência infra não requerendo agentes clientes (malwares contínuos de verificação como no Puppet) na máquina do alvo principal; Ele opera estritamente o protocolo nativo encriptado **SSH (Secure Shell)** conectando-se remotamente sob ordens, transportando na memória de rede módulozinhos operacionais, manipulando os states Linux, finaliza seu engajamento e some com leveza e excelência sem deixar sujeira computacional nativa acesa na AWS.

**4. Estado do Terraform**
O arquivo criptografado de matriz `terraform.tfstate` opera como o cérebro das amarras virtuais, ele detém o dicionário cartográfico (a chave mestre de ligações com os códigos abstratos em linguagem `.tf` traduzidos para o serial ID de hardwares materializados na Azure/AWS). Perdido esse estado primordial o código local esquece do que originou na nuvem, ficando prostrado incapaz de deletar recursos ou alterá-los já que ao tentar a re-aplicação criará milhares de componentes redundantes encarecendo e conflitualizando IPs em redes fantasmas no ecossistema (Orphaned Infra).

---

### 🔴 Desafio (Exploração)

**5. DevOps na Prática (Integração)**
Um devops criaria as conexões da linha em um diretório automatizado (`.github/workflows/deploy.yml`):
Na esteira de CI, ele provisionaria as credenciais seguras e injetaria o comando `terraform apply -auto-approve`, cujo script retornaria um *Output Array* de endereços IPv4 originados e elásticos de produção das três webclouds. O Action do repositório transferiria essa matriz de IPs instantaneamente para o inventário do `ansible-playbook setup.yml -i ./outputs` rodando no container efêmero a inserção final das dependências logísticas e de bibliotecas na máquina, acoplando simultaneamente o provisionamento cru do HashiCorp com a gerência do RedHat culminando em Servidor Produtivo (100% humano livre na entrega global).

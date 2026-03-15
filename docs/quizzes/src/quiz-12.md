# Quiz: Aula 12 - Automação e Infraestrutura como Código (IaC) ⚙️

1.  **O que caracteriza a "Infraestrutura como Código" (IaC)?**
    - [ ] Digitar o código no terminal do servidor manualmente.
    - [x] Gerenciar servidores e redes através de arquivos de configuração, como se fossem software.
    - [ ] Trocar as peças físicas do computador usando código.
    - [ ] Apenas um nome bonito para Cloud Computing.
    *   *Explicação: IaC permite versionar, testar e repetir a criação de ambientes inteiros.*

2.  **Para que serve o Terraform?**
    - [ ] Para editar arquivos de texto.
    - [x] Para provisionar infraestrutura (criar servidores, bancos e redes) em diversos provedores de nuvem.
    - [ ] Para gerenciar as tarefas da equipe no Jira.
    - [ ] Para substituir o Git.
    *   *Explicação: O Terraform é o "arquiteto" que molda os recursos na nuvem.*

3.  **Qual a principal função do Ansible?**
    - [ ] Criar servidores do zero na AWS.
    - [x] Gerenciar a configuração e instalação de softwares dentro de servidores já existentes.
    - [ ] Desenhar as telas do aplicativo (UI).
    - [ ] Compilar código C++.
    *   *Explicação: O Ansible é focado em automação de tarefas de S.O. e configuração de apps.*

4.  **Em IaC, o que significa um recurso ser "Declarativo"?**
    - [ ] Que ele precisa ser gritado no microfone.
    - [x] Você descreve o "estado final" desejado e a ferramenta descobre como chegar lá.
    - [ ] Você escreve passo a passo cada comando que o computador deve rodar.
    - [ ] É um tipo de comentário no código.
    *   *Explicação: Ferramentas como Terraform e Ansible são declarativas; você diz "quero 3 servidores", não "crie 1, depois 1, depois 1".*

5.  **Qual a vantagem do Ansible ser "Agentless" (Sem Agente)?**
    - [ ] Ele não precisa de internet para funcionar.
    - [x] Você não precisa instalar nada nos servidores que vai configurar, apenas ter acesso via SSH.
    - [ ] Ele não possui interface gráfica.
    - [ ] Ele é imune a vírus.
    *   *Explicação: Isso facilita a adoção, pois basta o acesso remoto para começar a automação.*

6.  **O que é um Terraform State file (.tfstate)?**
    - [ ] Um arquivo com as senhas da conta.
    - [x] O arquivo onde o Terraform guarda o conhecimento atual do que ele criou na vida real.
    - [ ] Uma lista de desejos do desenvolvedor.
    - [ ] O histórico de commits do Git.
    *   *Explicação: É vital para o Terraform saber o que precisa ser mudado ou destruído.*

7.  **No Ansible, o que é um "Playbook"?**
    - [ ] Um tablet usado em reuniões.
    - [x] Um arquivo YAML que contém a lista de tarefas e configurações a serem aplicadas no servidor.
    - [ ] O manual de instruções do software.
    - [ ] Uma branch de testes.
    *   *Explicação: É onde os "plays" (jogadas) de automação são definidos.*

8.  **O que significa "Idempotência" em ferramentas de automação?**
    - [ ] Que a ferramenta apaga tudo se der erro.
    - [x] Rodar a mesma ferramenta várias vezes terá o mesmo resultado final, sem duplicar tarefas desnecessárias.
    - [ ] Que o código só roda uma única vez e depois se deleta.
    - [ ] Que a ferramenta exige muita memória RAM.
    *   *Explicação: Se o software já está instalado, o Ansible não tenta o instalar novamente.*

9.  **Dizer que uma infraestrutura racha (Mutable vs Immutable):**
    - [ ] Infraestrutura Mutável é impossível de hackear.
    - [x] Mutável é quando você altera o servidor vivo; Imutável é quando você destrói o velho e cria um novo a cada mudança.
    - [ ] Mutável é o Docker; Imutável é o Git.
    - [ ] Não existem esses termos em infraestrutura.
    *   *Explicação: A cultura moderna prefere a imutabilidade para evitar desvios de configuração.*

10. **Qual a maior vantagem de usar IaC em grandes empresas?**
    - [ ] Eliminar a necessidade de contratar pessoas de infraestrutura.
    - [x] Velocidade, consistência e capacidade de recriar ambientes de desastre em minutos.
    - [ ] Deixar o banco de dados mais rápido.
    - [ ] Manter as senhas em arquivos de texto simples.
    *   *Explicação: A automação permite escalar e recuperar sistemas complexos com precisão matemática.*

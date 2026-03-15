# Quiz 12

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que caracteriza a "Infraestrutura como Código" (IaC)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Digitar o código no terminal do servidor manualmente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Gerenciar servidores e redes através de arquivos de configuração, como se fossem software.">Gerenciar servidores e redes através de arquivos de configuração, como se fossem software.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Trocar as peças físicas do computador usando código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Apenas um nome bonito para Cloud Computing.
    *   *Explicação: IaC permite versionar, testar e repetir a criação de ambientes inteiros.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Para que serve o Terraform?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para editar arquivos de texto.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para provisionar infraestrutura (criar servidores, bancos e redes) em diversos provedores de nuvem.">Para provisionar infraestrutura (criar servidores, bancos e redes) em diversos provedores de nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para gerenciar as tarefas da equipe no Jira.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para substituir o Git.
    *   *Explicação: O Terraform é o "arquiteto" que molda os recursos na nuvem.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Qual a principal função do Ansible?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Criar servidores do zero na AWS.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Gerenciar a configuração e instalação de softwares dentro de servidores já existentes.">Gerenciar a configuração e instalação de softwares dentro de servidores já existentes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Desenhar as telas do aplicativo (UI).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Compilar código C++.
    *   *Explicação: O Ansible é focado em automação de tarefas de S.O. e configuração de apps.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **Em IaC, o que significa um recurso ser "Declarativo"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que ele precisa ser gritado no microfone.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Você descreve o "estado final" desejado e a ferramenta descobre como chegar lá.">Você descreve o "estado final" desejado e a ferramenta descobre como chegar lá.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Você escreve passo a passo cada comando que o computador deve rodar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">É um tipo de comentário no código.
    *   *Explicação: Ferramentas como Terraform e Ansible são declarativas; você diz "quero 3 servidores", não "crie 1, depois 1, depois 1".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **Qual a vantagem do Ansible ser "Agentless" (Sem Agente)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele não precisa de internet para funcionar.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Você não precisa instalar nada nos servidores que vai configurar, apenas ter acesso via SSH.">Você não precisa instalar nada nos servidores que vai configurar, apenas ter acesso via SSH.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele não possui interface gráfica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Ele é imune a vírus.
    *   *Explicação: Isso facilita a adoção, pois basta o acesso remoto para começar a automação.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **O que é um Terraform State file (.tfstate)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um arquivo com as senhas da conta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O arquivo onde o Terraform guarda o conhecimento atual do que ele criou na vida real.">O arquivo onde o Terraform guarda o conhecimento atual do que ele criou na vida real.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma lista de desejos do desenvolvedor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O histórico de commits do Git.
    *   *Explicação: É vital para o Terraform saber o que precisa ser mudado ou destruído.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **No Ansible, o que é um "Playbook"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um tablet usado em reuniões.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um arquivo YAML que contém a lista de tarefas e configurações a serem aplicadas no servidor.">Um arquivo YAML que contém a lista de tarefas e configurações a serem aplicadas no servidor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O manual de instruções do software.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Uma branch de testes.
    *   *Explicação: É onde os "plays" (jogadas) de automação são definidos.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **O que significa "Idempotência" em ferramentas de automação?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que a ferramenta apaga tudo se der erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Rodar a mesma ferramenta várias vezes terá o mesmo resultado final, sem duplicar tarefas desnecessárias.">Rodar a mesma ferramenta várias vezes terá o mesmo resultado final, sem duplicar tarefas desnecessárias.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que o código só roda uma única vez e depois se deleta.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Que a ferramenta exige muita memória RAM.
    *   *Explicação: Se o software já está instalado, o Ansible não tenta o instalar novamente.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **Dizer que uma infraestrutura racha (Mutable vs Immutable):**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Infraestrutura Mutável é impossível de hackear.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Mutável é quando você altera o servidor vivo; Imutável é quando você destrói o velho e cria um novo a cada mudança.">Mutável é quando você altera o servidor vivo; Imutável é quando você destrói o velho e cria um novo a cada mudança.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Mutável é o Docker; Imutável é o Git.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não existem esses termos em infraestrutura.
    *   *Explicação: A cultura moderna prefere a imutabilidade para evitar desvios de configuração.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Qual a maior vantagem de usar IaC em grandes empresas?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Eliminar a necessidade de contratar pessoas de infraestrutura.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Velocidade, consistência e capacidade de recriar ambientes de desastre em minutos.">Velocidade, consistência e capacidade de recriar ambientes de desastre em minutos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deixar o banco de dados mais rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Manter as senhas em arquivos de texto simples.
    *   *Explicação: A automação permite escalar e recuperar sistemas complexos com precisão matemática.*</div>
  <div class="quiz-feedback"></div>
</div>


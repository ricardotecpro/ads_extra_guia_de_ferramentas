# Quiz: Aula 14 - Orquestração com Kubernetes e Runners ☸️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual o papel principal do Kubernetes (K8s)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Editar o Dockerfile dos desenvolvedores.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Diferente do Docker (que gerencia o contêiner), o K8s orquestra milhares de contêineres em um cluster de servidores.">Diferente do Docker (que gerencia o contêiner), o K8s orquestra milhares de contêineres em um cluster de servidores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Substituir a necessidade de usar o GitHub.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas monitorar o consumo de bateria do servidor.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é um "Pod" no Kubernetes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma pasta de arquivos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A menor unidade do K8s, que pode conter um ou mais contêineres que compartilham recursos.">A menor unidade do K8s, que pode conter um ou mais contêineres que compartilham recursos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O nome do servidor físico.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um comando para apagar o banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que acontece se um Pod "morre" ou o servidor falha em um cluster Kubernetes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O sistema fica fora do ar até o técnico chegar.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O K8s percebe e automaticamente cria um novo Pod em outro servidor disponível (Auto-Cura).">O K8s percebe e automaticamente cria um novo Pod em outro servidor disponível (Auto-Cura).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O GitHub apaga o repositório por segurança.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Todos os outros Pods são desligados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que é um "Cluster" Kubernetes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de banco de dados NoSQL.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um conjunto de máquinas (Nodes) que trabalham juntas gerenciadas pelo Kubernetes.">Um conjunto de máquinas (Nodes) que trabalham juntas gerenciadas pelo Kubernetes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma extensão do VS Code para orquestração.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma branch secreta do Git.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a diferença entre o Control Plane e os Worker Nodes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não há diferença.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Control Plane é o "cérebro" que toma decisões; os Worker Nodes são as máquinas que realmente rodam as aplicações.">O Control Plane é o "cérebro" que toma decisões; os Worker Nodes são as máquinas que realmente rodam as aplicações.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O Control Plane é pago; os Nodes são gratuitos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Control Plane é para o Windows e Nodes para o Linux.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que significa "Escalabilidade Horizontal" (Horizontal Scaling)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Comprar um servidor mais potente (CPU/RAM).</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Adicionar mais cópias (réplicas) da aplicação em execução para dividir a carga.">Adicionar mais cópias (réplicas) da aplicação em execução para dividir a carga.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Mudar o site de cor conforme o número de usuários.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar contêineres que estão lentos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que serve um "Runner" em uma pipeline de CI/CD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Para fazer o deploy manual.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o agente ou contêiner encarregado de executar os comandos definidos no seu workflow.">É o agente ou contêiner encarregado de executar os comandos definidos no seu workflow.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um desenvolvedor que trabalha rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É um tipo de teste unitário.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Por que grandes empresas usam Kubernetes em vez de apenas Docker?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque é mais bonito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Pela necessidade de alta disponibilidade, auto-escala e gerenciamento complexo de rede e tráfego.">Pela necessidade de alta disponibilidade, auto-escala e gerenciamento complexo de rede e tráfego.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque o Docker não funciona em servidores profissionais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque o Kubernetes é mais fácil de aprender.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que é o "HPA" (Horizontal Pod Autoscaler)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um comando para apagar contêineres.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um recurso que aumenta ou diminui o número de Pods automaticamente baseado no consumo de CPU ou memória.">Um recurso que aumenta ou diminui o número de Pods automaticamente baseado no consumo de CPU ou memória.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O nome do criador do Kubernetes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma lei de proteção de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Sobre o Kubernetes, é correto afirmar:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele substitui o Docker completamente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele utiliza tecnologias de contêiner (como o Docker) por baixo dos panos para rodar as aplicações.">Ele utiliza tecnologias de contêiner (como o Docker) por baixo dos panos para rodar as aplicações.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele só pode ser usado se você tiver um servidor físico no seu quarto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele é um software de design para arquitetos.</div>
  <div class="quiz-feedback"></div>
</div>


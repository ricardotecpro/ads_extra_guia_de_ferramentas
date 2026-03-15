# Quiz: Aula 14 - Orquestração com Kubernetes e Runners ☸️

1.  **Qual o papel principal do Kubernetes (K8s)?**
    - [ ] Editar o Dockerfile dos desenvolvedores.
    - [x] Diferente do Docker (que gerencia o contêiner), o K8s orquestra milhares de contêineres em um cluster de servidores.
    - [ ] Substituir a necessidade de usar o GitHub.
    - [ ] Apenas monitorar o consumo de bateria do servidor.
    *   *Explicação: O K8s é o maestro que gerencia onde e como os contêineres devem rodar em larga escala.*

2.  **O que é um "Pod" no Kubernetes?**
    - [ ] Uma pasta de arquivos.
    - [x] A menor unidade do K8s, que pode conter um ou mais contêineres que compartilham recursos.
    - [ ] O nome do servidor físico.
    - [ ] Um comando para apagar o banco de dados.
    *   *Explicação: No K8s, você não sobe contêineres diretamente, você sobe Pods.*

3.  **O que acontece se um Pod "morre" ou o servidor falha em um cluster Kubernetes?**
    - [ ] O sistema fica fora do ar até o técnico chegar.
    - [x] O K8s percebe e automaticamente cria um novo Pod em outro servidor disponível (Auto-Cura).
    - [ ] O GitHub apaga o repositório por segurança.
    - [ ] Todos os outros Pods são desligados.
    *   *Explicação: Essa resiliência é um dos maiores trunfos do Kubernetes.*

4.  **O que é um "Cluster" Kubernetes?**
    - [ ] Um tipo de banco de dados NoSQL.
    - [x] Um conjunto de máquinas (Nodes) que trabalham juntas gerenciadas pelo Kubernetes.
    - [ ] Uma extensão do VS Code para orquestração.
    - [ ] Uma branch secreta do Git.
    *   *Explicação: O cluster combina o poder de vários servidores em um único sistema lógico.*

5.  **Qual a diferença entre o Control Plane e os Worker Nodes?**
    - [ ] Não há diferença.
    - [x] O Control Plane é o "cérebro" que toma decisões; os Worker Nodes são as máquinas que realmente rodam as aplicações.
    - [ ] O Control Plane é pago; os Nodes são gratuitos.
    - [ ] Control Plane é para o Windows e Nodes para o Linux.
    *   *Explicação: Esta separação garante a organização e controle do ambiente.*

6.  **O que significa "Escalabilidade Horizontal" (Horizontal Scaling)?**
    - [ ] Comprar um servidor mais potente (CPU/RAM).
    - [x] Adicionar mais cópias (réplicas) da aplicação em execução para dividir a carga.
    - [ ] Mudar o site de cor conforme o número de usuários.
    - [ ] Deletar contêineres que estão lentos.
    *   *Explicação: É o ato de expandir o sistema adicionando mais unidades, não aumentando o tamanho da unidade atual.*

7.  **Para que serve um "Runner" em uma pipeline de CI/CD?**
    - [ ] Para fazer o deploy manual.
    - [x] É o agente ou contêiner encarregado de executar os comandos definidos no seu workflow.
    - [ ] É um desenvolvedor que trabalha rápido.
    - [ ] É um tipo de teste unitário.
    *   *Explicação: O runner é quem "coloca a mão na massa" no GitHub Actions ou GitLab CI.*

8.  **Por que grandes empresas usam Kubernetes em vez de apenas Docker?**
    - [ ] Porque é mais bonito.
    - [x] Pela necessidade de alta disponibilidade, auto-escala e gerenciamento complexo de rede e tráfego.
    - [ ] Porque o Docker não funciona em servidores profissionais.
    - [ ] Porque o Kubernetes é mais fácil de aprender.
    *   *Explicação: O K8s resolve problemas de software em escala global.*

9.  **O que é o "HPA" (Horizontal Pod Autoscaler)?**
    - [ ] Um comando para apagar contêineres.
    - [x] Um recurso que aumenta ou diminui o número de Pods automaticamente baseado no consumo de CPU ou memória.
    - [ ] O nome do criador do Kubernetes.
    - [ ] Uma lei de proteção de dados.
    *   *Explicação: Garante que seu site não caia no pico de acessos e economize dinheiro no silêncio da noite.*

10. **Sobre o Kubernetes, é correto afirmar:**
    - [ ] Ele substitui o Docker completamente.
    - [x] Ele utiliza tecnologias de contêiner (como o Docker) por baixo dos panos para rodar as aplicações.
    - [ ] Ele só pode ser usado se você tiver um servidor físico no seu quarto.
    - [ ] Ele é um software de design para arquitetos.
    *   *Explicação: K8s e Docker são complementares: um faz a "caixa" (docker), o outro gerencia o "empilhamento" (k8s).*

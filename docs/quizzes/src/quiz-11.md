# Quiz: Aula 11 - CI/CD Moderno (GitHub Actions) 🚀

1.  **O que significa a sigla CI?**
    - [ ] Core Integration.
    - [x] Continuous Integration (Integração Contínua).
    - [ ] Code Identification.
    - [ ] Computer Intelligence.
    *   *Explicação: CI foca na integração frequente do código de vários desenvolvedores, validada por testes automáticos.*

2.  **Qual o principal benefício do CD (Continuous Delivery/Deployment)?**
    - [ ] Deletar o código antigo automaticamente.
    - [x] Automatizar a entrega do software para os ambientes de teste ou produção, reduzindo processos manuais.
    - [ ] Fazer o backup do banco de dados na máquina do desenvolvedor.
    - [ ] Substituir a necessidade de ter um servidor.
    *   *Explicação: O CD garante que o deploy seja um processo repetível e seguro.*

3.  **No GitHub Actions, o que é um "Workflow"?**
    - [ ] O nome do cargo do desenvolvedor.
    - [x] Um processo automatizado configurável que executará um ou mais jobs.
    - [ ] Uma pasta onde guardamos imagens.
    - [ ] O layout visual do GitHub.
    *   *Explicação: Workflows são as pipelines descritas em arquivos YAML.*

4.  **Em qual formato de arquivo as configurações do GitHub Actions são escritas?**
    - [ ] JSON.
    - [x] YAML (.yml ou .yaml).
    - [ ] HTML.
    - [ ] XML.
    *   *Explicação: YAML é o padrão da indústria para arquivos de configuração devido à sua legibilidade.*

5.  **O que é um "Trigger" (Gatilho) no Actions?**
    - [ ] Um erro que para a pipeline.
    - [x] Um evento que inicia a execução do workflow (ex: push, pull_request).
    - [ ] O botão de deletar o repositório.
    - [ ] Uma senha secreta do desenvolvedor.
    *   *Explicação: O trigger define "quando" a automação deve começar.*

6.  **Para que serve um "Runner" no contexto de CI/CD?**
    - [ ] Para o desenvolvedor correr atrás dos prazos.
    - [x] É o servidor/máquina virtual que realmente executa os comandos do seu workflow.
    - [ ] É um tipo de plugin do VS Code.
    - [ ] É o comando para deletar arquivos temporários.
    *   *Explicação: O Runner é o "trabalhador" que roda os testes e faz o build do seu app.*

7.  **O que acontece se um Job da sua pipeline falhar?**
    - [ ] O GitHub deleta sua conta.
    - [x] O workflow é interrompido, o GitHub sinaliza com um "X" vermelho e avisa o desenvolvedor.
    - [ ] O código é enviado para o servidor de qualquer forma.
    - [ ] Nada, o processo continua sem problemas.
    *   *Explicação: A falha serve para alertar que algo no código novo não está correto.*

8.  **O que são "GitHub Secrets"?**
    - [ ] Segredos sobre a história da empresa.
    - [x] Variáveis de ambiente criptografadas (como senhas e chaves de API) que a pipeline usa com segurança.
    - [ ] Comentários escondidos no código.
    - [ ] Membros ocultos da equipe.
    *   *Explicação: Secrets permitem usar dados sensíveis na automação sem expô-los no código.*

9.  **Qual a vantagem de usar `on: [pull_request]` em vez de apenas `on: [push]`?**
    - [ ] Não há vantagem.
    - [x] Permite testar o código antes mesmo dele entrar na branch principal, auxiliando no Code Review.
    - [ ] Economiza dinheiro para o GitHub.
    - [ ] Faz o deploy ser mais rápido.
    *   *Explicação: Testar PRs garante que a integração só ocorra se o código estiver estável.*

10. **O que é um "Step" dentro de um Job do GitHub Actions?**
    - [ ] Um degrau na escada da empresa.
    - [x] Uma tarefa individual que executa um comando ou uma ação específica.
    - [ ] O nome do arquivo YAML.
    - [ ] Um tipo de branch.
    *   *Explicação: Jobs são compostos por vários Steps executados em sequência.*

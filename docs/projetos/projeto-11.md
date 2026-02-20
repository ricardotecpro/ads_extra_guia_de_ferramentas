# Projeto 11 - Minha Primeira Pipeline 🚀

### 🎯 Objetivo
Criar e disparar seu primeiro fluxo de automação (Workflow) no GitHub para entender como as ferramentas de CI/CD funcionam na nuvem.

### 📋 Passo a Passo

1.  **Pasta de Configuração**: No seu repositório do GitHub (criado no Projeto 05), crie uma pasta chamada `.github` e, dentro dela, uma pasta chamada `workflows`.
2.  **Arquivo de Workflow**: Crie um arquivo chamado `hello-ci.yml` dentro de `workflows`.
3.  **Conteúdo do YAML**: Cole o código abaixo:
    ```yaml
    name: Teste de Automacao
    on: [push]
    jobs:
      check-hello:
        runs-on: ubuntu-latest
        steps:
          - name: Say Hello
            run: echo "Minha pipeline está funcionando!"
    ```
4.  **Commit e Push**: Envie essa alteração para o GitHub.
5.  **Monitoramento**: Vá na aba **Actions** do seu repositório e clique no workflow "Teste de Automacao". Veja ele sendo executado e verifique se o log mostra a mensagem do comando `echo`.

---
**Entrega**: O link da aba "Actions" do seu repositório mostrando o workflow com sucesso (verde).
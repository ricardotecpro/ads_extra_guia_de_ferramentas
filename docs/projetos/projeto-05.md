# Projeto 05 - Meu Código na Nuvem ☁️

### 🎯 Objetivo
Aprender a sincronizar um repositório local com o GitHub e entender a importância do backup e colaboração online.

### 📋 Passo a Passo

1.  **Novo Repo no GitHub**: No seu GitHub, crie um repositório **Público** chamado `git-hands-on-ads`.
2.  **Conexão Remota**: No terminal, dentro da pasta do Projeto 04, execute:
    ```bash
    git remote add origin https://github.com/SEU-USUARIO/git-hands-on-ads.git
    ```
3.  **Envio de Código**: Envie seu commit local para a nuvem:
    ```bash
    git push -u origin main
    ```
4.  **Verificação**: Recarregue a página do GitHub e veja seu arquivo `index.html` lá.
5.  **Edição Online**: Edite o arquivo diretamente no site do GitHub (usando o botão de lápis) e faça o commit por lá.
6.  **Sincronização Inversa**: Volte ao terminal e traga essa mudança para sua máquina:
    ```bash
    git pull origin main
    ```

---
**Entrega**: O link do seu repositório público no GitHub.
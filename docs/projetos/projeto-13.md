# Projeto 13 - Empacotando com Docker 📦

### 🎯 Objetivo
Aprender a criar uma imagem personalizada no Docker para garantir que o seu projeto rode da mesma forma em qualquer servidor.

### 📋 Passo a Passo

1.  **Ambiente**: Abra a pasta do seu Projeto 04 (`meu-legacy-projeto`).
2.  **Criação do Dockerfile**: Crie um arquivo chamado `Dockerfile` (sem extensão).
3.  **Configuração da Imagem**:
    ```dockerfile
    # Usar uma imagem base leve de servidor web
    FROM nginx:alpine
    # Copiar seu arquivo index.html para dentro da pasta do servidor
    COPY index.html /usr/share/nginx/html/index.html
    ```
4.  **Criação da Imagem (Terminal)**: Execute o comando:
    ```bash
    docker build -t meu-site-docker .
    ```
5.  **Execução do Contêiner**: Rode seu site dentro do Docker:
    ```bash
    docker run -d -p 8080:80 meu-site-docker
    ```
6.  **Teste**: Acesse `localhost:8080` no seu navegador e veja se o seu `index.html` aparece.

---
**Entrega**: Um print do navegador acessando o `localhost:8080` e um print do comando `docker ps` no terminal.
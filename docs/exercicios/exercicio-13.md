# Exercícios: Aula 13 - Docker e Docker Compose 📦

### 🟢 Básicos (Fixação)

1.  **Analogia de Contêiner**: Por que usamos a metáfora de um contêiner de navio para explicar o Docker? O que o software ganha com esse "empacotamento"?
2.  **Imagens vs Contêineres**: Se você baixar a imagem do `nginx` do Docker Hub e rodar 3 contêineres a partir dela, os 3 serão iguais? Eles compartilham os mesmos arquivos em tempo de execução?

### 🟡 Intermediários (Aplicação)

3.  **Docker Compose**: Explique por que é melhor usar um arquivo `docker-compose.yml` para rodar uma aplicação com Banco de Dados do que rodar dois comandos `docker run` separados.
4.  **Mapeamento de Portas**: Se você rodar um contêiner com o comando `docker run -p 8080:80`, em qual porta você deve acessar a aplicação no seu navegador? O que aconteceria se você usasse `80:80`?

### 🔴 Desafio (Exploração)

5.  **Persistência com Volumes**: Por padrão, se você deletar um contêiner de banco de dados, todos os dados somem. Pesquise o que são **Volumes** no Docker e como eles resolvem o problema de salvar os dados mesmo quando o contêiner morre.

---

[**🔍 Ver Solução e Lógica do Exercício**](./solucao-13.md)
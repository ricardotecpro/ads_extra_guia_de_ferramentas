# Exercícios: Aula 11 - CI/CD Moderno 🚀

### 🟢 Básicos (Fixação)

1.  **Conceito de Pipeline**: Explique o que acontece com o código de um desenvolvedor entre o momento do `git push` e o momento em que ele aparece no site oficial, em um ambiente com CI/CD.
2.  **Eventos do GitHub**: Qual a diferença entre disparar um workflow no `push` e disparar apenas no `pull_request`?

### 🟡 Intermediários (Aplicação)

3.  **Falha na Integração**: Se o workflow de testes falhar no GitHub Actions, o desenvolvedor deve ser impedido de fazer o "Merge" para a branch principal? Por quê?
4.  **YAML Syntax**: Identifique o erro no trecho de código abaixo:
    ```yaml
    jobs:
      build:
        step: # Aqui falta algo
          - run: npm install
    ```

### 🔴 Desafio (Exploração)

5.  **Matriz de Testes**: Pesquise o que é uma "Build Matrix" no GitHub Actions. Como ela permite que você teste seu código em várias versões do Windows, Linux e Mac simultaneamente com um único arquivo?

---

[**🔍 Ver Solução e Lógica do Exercício**](./solucao-11.md)
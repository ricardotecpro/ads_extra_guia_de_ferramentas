# Resolução: Aula 05 - Plataformas de Colaboração 🤝

### 🟢 Básicos (Fixação)

**1. Dicionário Remix**
*   **`git push`**: Pense na palavra "empurrar" (Push). Você está pegando o código pronto da sua máquina e empurrando-o para a "nuvem" (GitHub). Como subir uma foto para o Instagram.
*   **`git pull`**: Pense na palavra "puxar" (Pull). Você quer jogar o código que está atualizado na nuvem para a sua máquina física. Como baixar para o celular uma imagem que está no Google Drive.

**2. Segurança de Código**
A branch `main` (ou `master`) é a versão oficial do seu projeto, aquela que os clientes estão usando em produção. Trabalhar direto nela não permite revisão de terceiros. Se você subir um bug crítico direto na `main`, o sistema sairá do ar. O correto é sempre criar uma branch paralela (`feature/login`, por exemplo), isolando suas mudanças até que sejam aprovadas pelos outros desenvolvedores.

---

### 🟡 Intermediários (Aplicação)

**3. Fluxo de Pull Request**
1.  **Criar Branch Nova**: Basear seu ambiente a partir da `main` (`git checkout -b feature/botao`).
2.  **Codar e Comitar**: Realizar as alterações e salvar o histórico localmente.
3.  **Publicar a Branch (Push)**: Mandar a branch para o servidor do GitHub.
4.  **Abrir o Pull Request (PR)**: Na interface do GitHub, clicar no botão de PR comparando sua branch com a `main`, pedir para a equipe revisar o código e, quando aprovado, clicar em "Merge".

**4. Resolução de Conflitos**
Um conflito (`Merge Conflict`) surge quando duas pessoas tentam mexer na mesma parte de um arquivo simultaneamente. Exemplo: O Dev A muda o título `<title>` no arquivo `index.html` para "Site do José" e envia para a branch principal. O Dev B, com o arquivo antigo, muda a mesma linha `<title>` para "Portal do José" e tenta subir. O Git "trava" e pede que um erro humano julgue qual das duas linhas textuais deve prevalecer ou se as duas devem coexistir.

---

### 🔴 Desafio (Exploração)

**5. Contribuição Open Source**
(Esta resposta varia conforma a pesquisa do aluno). Contudo, nas comunidades open-source, um PR costuma ser rejeitado caso:
*   Não possua testes automatizados.
*   Não respeite o padrão de código da comunidade (Linting / Estilo de Identação).
*   Seja uma quebra na arquitetura base sem discussão na área de *Issues* primeiro.
Um PR aceito costuma ter discussão com os mantenedores, revisões em código visualizadas por "Approve" verdes e o clássico sinal de que os testes "passaram no CI".

---

[**⬅️ Voltar para o Exercício**](./exercicio-05.md)

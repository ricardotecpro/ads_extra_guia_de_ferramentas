# Aula 04: Controle de Versão com Git 🛠️

---

## 🎯 Nossa Missão
*   Entender por que usar Git.
*   Dominar o fluxo local (Add/Commit).
*   Configurar sua identidade de desenvolvedor.
*   Aprender a "viajar no tempo" com o histórico.

---

## 😫 O Problema do "Final_v2_Revise.zip"
*   Qual arquivo é o último? <!-- .element: class="fragment" -->
*   Como voltar se eu apagar tudo sem querer? <!-- .element: class="fragment" -->
*   Como saber quem mudou o quê? <!-- .element: class="fragment" -->
*   **O Git resolve tudo isso.** <!-- .element: class="fragment" -->

---

## 🧠 O que é o Git?
*   Sistema de Controle de Versão **Distribuído**. <!-- .element: class="fragment" -->
*   Criado por Linus Torvalds (o pai do Linux). <!-- .element: class="fragment" -->
*   Rápido, leve e focado na integridade dos dados. <!-- .element: class="fragment" -->

---

## ⚙️ Configuração Inicial
Antes de começar, o Git precisa saber quem você é.
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```
*   Configura apenas uma vez por computador. <!-- .element: class="fragment" -->

---

## 🏗️ As Três Áreas do Git
```mermaid
graph LR
    WD[Working Directory] -- git add --> SA[Staging Area]
    SA -- git commit --> LR[Local Repository]
```

---

## 1. Working Directory 📂
É a pasta onde seus arquivos estão agora.
*   Onde você edita, cria e deleta.
*   O Git está observando as mudanças "em aberto".

---

## 2. Staging Area (ou Index) 🎟️
É a "sala de espera" para os arquivos que você quer salvar.
*   Você escolhe o que entra no palco. <!-- .element: class="fragment" -->
*   Permite selecionar apenas alguns arquivos alterados. <!-- .element: class="fragment" -->
*   Comando: `git add <arquivo>`. <!-- .element: class="fragment" -->

---

## 3. Local Repository (Histórico) 📜
É onde as versões são salvas permanentemente na sua máquina.
*   Após o commit, a versão ganha um código (Hash). <!-- .element: class="fragment" -->
*   Imutável e seguro. <!-- .element: class="fragment" -->
*   Comando: `git commit -m "mensagem"`. <!-- .element: class="fragment" -->

---

## 🚀 Inicializando um Repositório
```termynal
$ mkdir meu-projeto
$ cd meu-projeto
$ git init
Initialized empty Git repository in /.../.git/
```
*   Isso cria a pasta mágica `.git`. <!-- .element: class="fragment" -->

---

## 🔍 Verificando o Estado
`git status`
*   Arquivos Vermelhos: Mudanças não preparadas. <!-- .element: class="fragment" -->
*   Arquivos Verdes: Mudanças no Staging (prontas para commit). <!-- .element: class="fragment" -->
*   Nada para comitar: Tudo limpo! <!-- .element: class="fragment" -->

---

## 📝 A Arte da Mensagem de Commit
❌ Má prática: `ajustes`, `fix`, `commmit`, `v1`
✅ Boa prática (Conventional Commits):
*   `feat: adicionar tela de login` <!-- .element: class="fragment" -->
*   `fix: corrigir erro no calculo de frete` <!-- .element: class="fragment" -->
*   `docs: atualizar cronograma da aula` <!-- .element: class="fragment" -->

---

## 📖 Consultando o Passado: `git log`
*   Lista todos os commits. <!-- .element: class="fragment" -->
*   Mostra Autor, Data e Mensagem. <!-- .element: class="fragment" -->
*   Exibe o **HASH** (ex: `a1b2c3d`). <!-- .element: class="fragment" -->
*   Use `git log --oneline` para uma lista curta. <!-- .element: class="fragment" -->

---

## 🕵️‍♂️ Ocultando o que não importa: `.gitignore`
Existem arquivos que **NÃO** devem ir para o Git:
*   Senhas e Chaves de API. <!-- .element: class="fragment" -->
*   Pastas de bibliotecas (`node_modules`). <!-- .element: class="fragment" -->
*   Arquivos temporários do Sistema (`.DS_Store`). <!-- .element: class="fragment" -->
*   Configurações pessoais do editor. <!-- .element: class="fragment" -->

---

## 💡 Como funciona o .gitignore?
Crie um arquivo chamado `.gitignore` e escreva os nomes das pastas/arquivos lá.
```text
node_modules/
.env
secret.txt
```

---

## 🔄 Fluxo Completo na Prática
1.  Edita o arquivo. <!-- .element: class="fragment" -->
2.  `git status` (Ver o que mudou). <!-- .element: class="fragment" -->
3.  `git add .` (Levar tudo para o palco). <!-- .element: class="fragment" -->
4.  `git commit -m "feat: x"` (Salvar!). <!-- .element: class="fragment" -->

---

## 🛳️ Diferença entre Git e GitHub
*   **Git**: O motor local. Funciona sem internet. <!-- .element: class="fragment" -->
*   **GitHub**: O estacionamento de nuvem. Ferramenta social. <!-- .element: class="fragment" -->
*   O Git envia para o GitHub (veremos na próxima aula!). <!-- .element: class="fragment" -->

---

## ⚠️ Atenção aos Erros Comuns
*   Esquecer de fazer o `git add` antes do `commit`. <!-- .element: class="fragment" -->
*   Tentar fazer `commit` sem mensagem. <!-- .element: class="fragment" -->
*   Sair comitando arquivos de 1GB (use .gitignore!). <!-- .element: class="fragment" -->

---

## 🏆 Checklist de Fundamentos
*   [ ] Repositório inicializado com `git init`. <!-- .element: class="fragment" -->
*   [ ] Usuário e Email configurados. <!-- .element: class="fragment" -->
*   [ ] Entende a diferença entre Add e Commit. <!-- .element: class="fragment" -->
*   [ ] Sabe ler o `git status`. <!-- .element: class="fragment" -->

---

## 📝 Prática de Hoje
1.  Criar uma pasta e iniciar o Git.
2.  Fazer 3 commits com mensagens diferentes.
3.  Criar um `.gitignore` e testar se funciona.

---

## 🏁 Dúvidas?
O Git é seu melhor amigo de agora em diante! 🚀

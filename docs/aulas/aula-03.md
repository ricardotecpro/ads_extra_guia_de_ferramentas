# Aula 03 - Ambiente de Desenvolvimento 💻

!!! tip "Objetivo"
    **Objetivo**: Customizar o ambiente de trabalho para máxima eficiência, conhecer a diferença entre Editores de Código e IDEs e dominar comandos básicos de terminal.

---

## 1. Editor vs IDE: Qual Escolher? 🧠

Embora pareçam iguais, ferramentas de escrita de código têm propósitos diferentes.

### 📄 Editores de Código (Ex: VS Code)
São leves, rápidos e "nascem" simples. Você os torna poderosos através de extensões.
*   **Vantagens**: Consome pouca memória, gratuito, ecossistema gigante.
*   **Desvantagens**: Exige configuração manual para algumas linguagens.

### 🏎️ IDEs - Ambientes Integrados (Ex: IntelliJ, PyCharm)
São "tanques de guerra" que já vêm com tudo o que um dev precisa (debugger, profiler, integração db).
*   **Vantagens**: Produtividade extrema para linguagens específicas (Java, Python, C#).
*   **Desvantagens**: Pesadas, muitas vezes pagas e com curva de aprendizado maior.

---

## 2. O Super Poder do VS Code 🚀

O **Visual Studio Code** é o editor mais popular do mundo. Para ele ser produtivo, você precisa do "kit básico" de extensões:

1.  **Portuguese (Brazil)**: Para traduzir a interface.
2.  **Material Icon Theme**: Para ícones de arquivos mais bonitos.
3.  **Prettier**: Para formatar seu código automaticamente.
4.  **Error Lens**: Para ver erros de código diretamente na linha.

---

## 3. Dominando o Terminal (CLI) ⌨️

O terminal é onde a magia acontece. Ele permite automatizar tarefas que levariam minutos na interface visual.

### Comandos Essenciais (Universal)

| Comando | Ação |
| :--- | :--- |
| `ls` (ou `dir`) | Listar arquivos da pasta |
| `cd` | Entrar em uma pasta |
| `mkdir` | Criar uma nova pasta |
| `touch` (ou `echo >`) | Criar um novo arquivo |
| `rm` (ou `del`) | Excluir um arquivo |

### Exemplo Prático de Fluxo no Terminal

```termynal
$ mkdir meu-projeto
$ cd meu-projeto
$ touch index.html
$ ls
index.html
$ code . 
# (Abre o projeto no VS Code)
```

---

## 4. Customização Profissional: ZSH e Oh My Zsh 🎨

Muitos desenvolvedores profissionais (especialmente em Mac e Linux) utilizam o **ZSH** com o **Oh My Zsh**. Ele adiciona temas e plugins que mostram em qual "branch" do Git você está, se há erros no comando anterior, entre outros.

> [!TIP]
> **Dica**: No Windows, você pode usar o **Windows Terminal** e configurar o **Oh My Posh** para ter uma experiência visual similar.

---

## 5. Mini-Projeto: Setup do Guerreiro(a) 🚀

Sua missão é deixar seu ambiente pronto para os próximos meses:

1.  Instale o **Visual Studio Code**.
2.  Instale as extensões citadas no capítulo 2.
3.  Abra o terminal do seu sistema e execute o comando `mkdir ads-ferramentas`.
4.  Entre na pasta e crie um arquivo chamado `config.txt` usando comandos de terminal.
5.  Configure o tema do seu VS Code para um que você goste (Ex: Dracula, One Dark Pro).

---

## 6. Exercício de Fixação 📝

1.  **Básico**: Explique uma diferença fundamental entre o VS Code e uma IDE da JetBrains.
2.  **Básico**: Para que serve o comando `cd ..` no terminal?
3.  **Intermediário**: Por que um desenvolvedor deveria preferir o terminal para criar uma estrutura de 10 pastas em vez de usar o explorador de arquivos?
4.  **Intermediário**: Qual a função da extensão "Prettier" no VS Code?
5.  **Desafio**: Pesquise o que é uma "Font with Ligatures" (como Fira Code) e qual o benefício visual que ela traz para o código.

---

**Próxima Aula**: Vamos mergulhar no [Controle de Versão com Git: Fundamentos](./aula-04.md)! 🛠️

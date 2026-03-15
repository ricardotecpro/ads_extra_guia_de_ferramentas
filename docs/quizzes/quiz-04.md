# Quiz 04

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que o Git faz essencialmente?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Hospeda sites na internet.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Gerencia o histórico de alterações de arquivos (versionamento).">Gerencia o histórico de alterações de arquivos (versionamento).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Compila código Java em linguagem de máquina.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Edita imagens e vídeos.
    *   *Explicação: O Git permite salvar "fotos" do seu projeto em diferentes momentos do tempo.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual o primeiro comando que você deve rodar ao iniciar um novo projeto com Git?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git commit`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! `git init`">`git init`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git push`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git add`
    *   *Explicação: `git init` cria o repositório local e a pasta oculta `.git`.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Para que serve a "Staging Area" (ou Index)?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para deletar arquivos permanentemente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para selecionar quais arquivos alterados devem ser incluídos no próximo commit.">Para selecionar quais arquivos alterados devem ser incluídos no próximo commit.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para ver o código de outros desenvolvedores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para hospedar o site online.
    *   *Explicação: Você usa o `git add` para mover arquivos para esta área de "preparação".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **Qual comando salva permanentemente as alterações no histórico local?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git save`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! `git commit`">`git commit`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git snapshot`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git store`
    *   *Explicação: O `commit` é o salvamento oficial de uma versão do código.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **O que a mensagem de commit deve descrever?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O que foi alterado e por que (de forma concisa e clara).">O que foi alterado e por que (de forma concisa e clara).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">A data e hora exatas do salvamento.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O número de linhas deletadas.
    *   *Explicação: Mensagens boas ajudam a entender a evolução do projeto no futuro.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **Como você verifica quais arquivos foram modificados mas ainda não foram "comitados"?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git check`</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! `git status`">`git status`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git verify`</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">`git show`
    *   *Explicação: O `git status` mostra o estado atual da sua pasta em relação ao último commit.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **O que acontece se você rodar `git log`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Git apaga o repositório.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O Git exibe a lista cronológica de todos os commits realizados.">O Git exibe a lista cronológica de todos os commits realizados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Git abre o editor de código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Git faz o upload dos arquivos para a nuvem.
    *   *Explicação: O `log` é o livro de história do seu projeto.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **Qual a diferença entre o Git na sua máquina e o GitHub?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não há diferença, são o mesmo software.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O Git é a ferramenta local; o GitHub é uma plataforma online que hospeda repositórios Git.">O Git é a ferramenta local; o GitHub é uma plataforma online que hospeda repositórios Git.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O GitHub é para designers e o Git para programadores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Git é pago e o GitHub é sempre gratuito.
    *   *Explicação: O Git funciona offline; o GitHub é o servidor onde você compartilha o código.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **O que o comando `git add .` faz?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deleta todos os arquivos da pasta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Adiciona todos os arquivos novos e modificados da pasta atual para a Staging Area.">Adiciona todos os arquivos novos e modificados da pasta atual para a Staging Area.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Cria um ponto final no histórico.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Envia os arquivos para o servidor remoto.
    *   *Explicação: O ponto `.` representa "tudo o que está no diretório atual".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **Por que o arquivo `.gitignore` é importante?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para esconder fotos pessoais do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para dizer ao Git quais arquivos e pastas ele deve ignorar (ex: senhas, pasta `node_modules`).">Para dizer ao Git quais arquivos e pastas ele deve ignorar (ex: senhas, pasta `node_modules`).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para deletar arquivos automaticamente do repositório.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para impedir que outros desenvolvedores editem o código.
    *   *Explicação: Evita que "lixo" ou arquivos sensíveis sejam enviados para o histórico de versão.*</div>
  <div class="quiz-feedback"></div>
</div>


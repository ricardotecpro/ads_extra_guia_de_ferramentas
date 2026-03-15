# Quiz 13

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. **O que é o Docker?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um tipo de banco de dados SQL.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Uma plataforma que permite empacotar e rodar aplicações em ambientes isolados chamados contêineres.">Uma plataforma que permite empacotar e rodar aplicações em ambientes isolados chamados contêineres.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um editor de código baseado na nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um sistema operacional que substitui o Windows.
    *   *Explicação: O Docker garante que o app rode igual em qualquer lugar, eliminando o "na minha máquina funciona".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. **Qual a diferença entre Imagem e Contêiner?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Imagem é o software instalado; Contêiner é o hardware.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Imagem é o molde/receita estática; Contêiner é a instância daquela imagem em execução.">Imagem é o molde/receita estática; Contêiner é a instância daquela imagem em execução.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Imagem é para Linux; Contêiner é para Windows.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Não há diferença, são o mesmo conceito.
    *   *Explicação: Você baixa uma Imagem e a "roda" como um Contêiner.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. **Qual o papel do arquivo `Dockerfile`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Guardar as senhas do banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Definir as instruções (passo a passo) para construir uma imagem Docker.">Definir as instruções (passo a passo) para construir uma imagem Docker.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Salvar o histórico de commits do projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Criar o design das telas.
    *   *Explicação: É onde você diz qual S.O. usar, quais pastas copiar e qual comando rodar.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. **O que o comando `docker run` faz?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Apenas instala o Docker no computador.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Cria e inicia um novo contêiner a partir de uma imagem.">Cria e inicia um novo contêiner a partir de uma imagem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deleta todas as imagens antigas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Envia a imagem para o GitHub.
    *   *Explicação: É o comando principal para colocar seu software "no ar" dentro de um contêiner.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. **Para que serve o Docker Compose?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para editar arquivos YAML.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Para orquestrar e rodar múltiplos contêineres (ex: API + Banco) simultaneamente com um único comando.">Para orquestrar e rodar múltiplos contêineres (ex: API + Banco) simultaneamente com um único comando.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para substituir o Kubernetes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Para diminuir o tamanho das imagens.
    *   *Explicação: Facilita gerenciar aplicações complexas que dependem de vários serviços.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. **Qual a vantagem do Docker em relação às Máquinas Virtuais (VMs) tradicionais?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Docker é mais caro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! O Docker é muito mais leve e rápido, pois compartilha o Kernel do sistema operacional hospedeiro.">O Docker é muito mais leve e rápido, pois compartilha o Kernel do sistema operacional hospedeiro.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O Docker permite rodar jogos de videogame.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">As VMs não permitem rodar bancos de dados.
    *   *Explicação: Contêineres não precisam de um S.O. completo dentro deles, apenas o estritamente necessário.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. **O que significa mapear portas (ex: `-p 8080:80`) no Docker?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Mudar a senha do roteador.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Ligar uma porta da sua máquina real (8080) à porta interna do contêiner (80).">Ligar uma porta da sua máquina real (8080) à porta interna do contêiner (80).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Acelerar a velocidade de download da imagem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Bloquear o acesso externo ao contêiner.
    *   *Explicação: Permite que você acesse o serviço rodando "dentro" do Docker pelo seu navegador.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. **O que é o Docker Hub?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um hub USB para conectar servidores.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Um registro online oficial onde pessoas e empresas compartilham suas imagens Docker.">Um registro online oficial onde pessoas e empresas compartilham suas imagens Docker.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">O nome do criador do Docker.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Um editor de texto para imagens.
    *   *Explicação: É como o "GitHub das imagens Docker".*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. **Ao deletar um contêiner, por padrão, o que acontece com os dados salvos dentro dele?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Eles são enviados para o e-mail do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Eles são perdidos permanentemente (o contêiner é efêmero).">Eles são perdidos permanentemente (o contêiner é efêmero).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Eles são salvos automaticamente no HD da máquina real.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Eles ficam suspensos no servidor até o próximo contêiner ligar.
    *   *Explicação: Contêineres são descartáveis; para salvar dados, usamos Volumes.*</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. **O que faz o comando `docker build`?**</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Testa a velocidade da rede.</div>
  <div class="quiz-option" data-correct="true" data-feedback="Correto! Lê o Dockerfile e cria uma imagem pronta para uso a partir dele.">Lê o Dockerfile e cria uma imagem pronta para uso a partir dele.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Formata o código fonte do projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. ">Deleta contêineres que não estão sendo usados.
    *   *Explicação: É o processo de "compilação" ou construção da sua imagem personalizada.*</div>
  <div class="quiz-feedback"></div>
</div>


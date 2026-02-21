# Quiz: Aula 13 - Contêineres com Docker 📦

1.  **O que é o Docker?**
    *   ( ) Um tipo de banco de dados SQL.
    *   (x) Uma plataforma que permite empacotar e rodar aplicações em ambientes isolados chamados contêineres.
    *   ( ) Um editor de código baseado na nuvem.
    *   ( ) Um sistema operacional que substitui o Windows.
    *   *Explicação: O Docker garante que o app rode igual em qualquer lugar, eliminando o "na minha máquina funciona".*

2.  **Qual a diferença entre Imagem e Contêiner?**
    *   ( ) Imagem é o software instalado; Contêiner é o hardware.
    *   (x) Imagem é o molde/receita estática; Contêiner é a instância daquela imagem em execução.
    *   ( ) Imagem é para Linux; Contêiner é para Windows.
    *   ( ) Não há diferença, são o mesmo conceito.
    *   *Explicação: Você baixa uma Imagem e a "roda" como um Contêiner.*

3.  **Qual o papel do arquivo `Dockerfile`?**
    *   ( ) Guardar as senhas do banco de dados.
    *   (x) Definir as instruções (passo a passo) para construir uma imagem Docker.
    *   ( ) Salvar o histórico de commits do projeto.
    *   ( ) Criar o design das telas.
    *   *Explicação: É onde você diz qual S.O. usar, quais pastas copiar e qual comando rodar.*

4.  **O que o comando `docker run` faz?**
    *   ( ) Apenas instala o Docker no computador.
    *   (x) Cria e inicia um novo contêiner a partir de uma imagem.
    *   ( ) Deleta todas as imagens antigas.
    *   ( ) Envia a imagem para o GitHub.
    *   *Explicação: É o comando principal para colocar seu software "no ar" dentro de um contêiner.*

5.  **Para que serve o Docker Compose?**
    *   ( ) Para editar arquivos YAML.
    *   (x) Para orquestrar e rodar múltiplos contêineres (ex: API + Banco) simultaneamente com um único comando.
    *   ( ) Para substituir o Kubernetes.
    *   ( ) Para diminuir o tamanho das imagens.
    *   *Explicação: Facilita gerenciar aplicações complexas que dependem de vários serviços.*

6.  **Qual a vantagem do Docker em relação às Máquinas Virtuais (VMs) tradicionais?**
    *   ( ) O Docker é mais caro.
    *   (x) O Docker é muito mais leve e rápido, pois compartilha o Kernel do sistema operacional hospedeiro.
    *   ( ) O Docker permite rodar jogos de videogame.
    *   ( ) As VMs não permitem rodar bancos de dados.
    *   *Explicação: Contêineres não precisam de um S.O. completo dentro deles, apenas o estritamente necessário.*

7.  **O que significa mapear portas (ex: `-p 8080:80`) no Docker?**
    *   ( ) Mudar a senha do roteador.
    *   (x) Ligar uma porta da sua máquina real (8080) à porta interna do contêiner (80).
    *   ( ) Acelerar a velocidade de download da imagem.
    *   ( ) Bloquear o acesso externo ao contêiner.
    *   *Explicação: Permite que você acesse o serviço rodando "dentro" do Docker pelo seu navegador.*

8.  **O que é o Docker Hub?**
    *   ( ) Um hub USB para conectar servidores.
    *   (x) Um registro online oficial onde pessoas e empresas compartilham suas imagens Docker.
    *   ( ) O nome do criador do Docker.
    *   ( ) Um editor de texto para imagens.
    *   *Explicação: É como o "GitHub das imagens Docker".*

9.  **Ao deletar um contêiner, por padrão, o que acontece com os dados salvos dentro dele?**
    *   ( ) Eles são enviados para o e-mail do desenvolvedor.
    *   (x) Eles são perdidos permanentemente (o contêiner é efêmero).
    *   ( ) Eles são salvos automaticamente no HD da máquina real.
    *   ( ) Eles ficam suspensos no servidor até o próximo contêiner ligar.
    *   *Explicação: Contêineres são descartáveis; para salvar dados, usamos Volumes.*

10. **O que faz o comando `docker build`?**
    *   ( ) Testa a velocidade da rede.
    *   (x) Lê o Dockerfile e cria uma imagem pronta para uso a partir dele.
    *   ( ) Formata o código fonte do projeto.
    *   ( ) Deleta contêineres que não estão sendo usados.
    *   *Explicação: É o processo de "compilação" ou construção da sua imagem personalizada.*

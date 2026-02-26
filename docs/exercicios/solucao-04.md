# Resolução: Aula 04 - Git Fundamentos 🛠️

### 🟢 Básicos (Fixação)

**1. Cinto de Comandos**
*   `git init`: Inicializa um repositório Git novo e vazio em um diretório (cria a pasta oculta `.git`).
*   `git add`: "Prepara" as alterações de um ou mais arquivos, mandando-os para a sala de espera (Staging Area).
*   `git commit`: "Tira a foto". Pega tudo o que estava na Staging Area e salva permanentemente no histórico local do repositório, exigindo uma mensagem descritiva.

**2. Mensagens de Commit**
A mensagem "ajustes" é terrível porque não diz o que foi ajustado, nem o porquê. Em um projeto com milhares de commits, se houver um bug, ninguém saberá o que esse commit alterou.
Exemplos profissionais:
1.  `Fix: Corrigir erro de cálculo na tela de pagamento`
2.  `Feat: Adicionar botão de login com Google`
3.  `Docs: Atualizar README com instruções de instalação`

---

### 🟡 Intermediários (Aplicação)

**3. Recuperação de Histórico**
Primeiro, seria necessário rodar `git log` para listar todo o histórico de alterações (as fotos). Ao encontrar o commit desejado de 3 versões atrás, eu precisaria copiar o código único (Hash) daquele commit e executar o comando `git checkout <hash>`.

**4. Staging Area**
A Staging Area serve para organizar seu trabalho de forma lógica. Se você editou 5 arquivos para consertar o rodapé do site e 2 arquivos para arrumar um erro de banco de dados, você não deveria salvar tudo em um único commit chamado "Ajustes". A Staging Area permite que você adicione primeiro apenas os arquivos do rodapé (`git add .`), faça um commit limpo, e depois adicione e comite separadamente a correção do banco de dados, mantendo o histórico cirúrgico.

---

### 🔴 Desafio (Exploração)

**5. O Desastre do .git**
Se você apagar a pasta `.git`, todos os **arquivos visíveis** (seu Working Directory) continuarão lá no exato momento que você deixou, intactos. O código não some. Contudo, todo o **histórico de versionamento (seus 50 commits)** é sumariamente destruído localmente, não sendo possível desfazê-lo pelo Git. Ele deixa de ser um repositório Git e vira uma pasta de arquivos comum. Se o código estiver espelhado no GitHub/GitLab, o histórico continua salvo nas nuvens.

---

[**⬅️ Voltar para o Exercício**](./exercicio-04.md)

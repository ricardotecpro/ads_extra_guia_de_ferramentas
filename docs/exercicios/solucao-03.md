# Resolução: Aula 03 - Ambiente de Desenvolvimento 💻

### 🟢 Básicos (Fixação)

**1. Extensões do VS Code**
A extensão **Error Lens** destaca os erros de sintaxe (como falta de ponto e vírgula, variáveis não declaradas ou parênteses não fechados) diretamente na linha em que você está digitando, pintando a linha de vermelho. Isso evita que o desenvolvedor perca tempo procurando onde errou só depois de tentar rodar a aplicação e ver a tela quebrar.

**2. Navegação no Terminal**
A sequência lógica de comandos seria:
```bash
$ mkdir teste
$ cd teste
$ touch info.md  # Ou 'echo > info.md' no Windows
$ cd ..
```

---

### 🟡 Intermediários (Aplicação)

**3. Produtividade (mv)**
Para renomear arquivos no terminal sem o uso do mouse, utilizamos o comando `mv` (move), que serve tanto para mover arquivos de diretório quanto para renomeá-los no mesmo lugar.
Comando: `$ mv script_velho.js app.js`

**4. CLI vs GUI**
Uma tarefa clássica é a criação de dezenas de pastas com nomes diferentes baseados em uma lógica. Ou, ainda mais comum, a instalação de dependências de um projeto (ex: rodar `npm install` no terminal leva segundos, enquanto baixar arquivos compactados via navegador, descompactar e colocar na pasta local consumiria minutos).

---

### 🔴 Desafio (Exploração)

**5. Customização Avançada (PATH)**
A variável de ambiente **PATH** é uma lista de caminhos (diretórios) que o sistema operacional consulta toda vez que você digita um comando no terminal. Por exemplo, quando você digita `node`, o sistema não sabe o que é isso, mas ele olha no PATH, acha a pasta de instalação do Node.js e executa o binário. Sem a configuração correta do PATH, você precisaria digitar o endereço completo do programa (ex: `C:\Program Files\Nodejs\node.exe`) toda vez que fosse usá-lo.

---

[**⬅️ Voltar para o Exercício**](./exercicio-03.md)

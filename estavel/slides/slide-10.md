# Aula 10: Qualidade de Código (Linters e Formatters) ✨

---

## 🎯 Nossa Missão
*   Entender a análise estática de código.
*   Dominar o ESLint (Linter).
*   Dominar o Prettier (Formatter).
*   Padronizar o ambiente de desenvolvimento do time.

---

## 🤔 Por que a qualidade importa?
*   **Legibilidade**: Código é mais lido do que escrito. <!-- .element: class="fragment" -->
*   **Manutenibilidade**: Mais fácil de consertar no futuro. <!-- .element: class="fragment" -->
*   **Conformidade**: Todo o time escreve do mesmo jeito. <!-- .element: class="fragment" -->
*   **Menos Bugs**: Erros bobos são pegos na hora. <!-- .element: class="fragment" -->

---

## 📖 O que é Análise Estática?
Analisar o código sem executá-lo.
*   Procura por padrões perigosos. <!-- .element: class="fragment" -->
*   Verifica se regras de estilo estão sendo seguidas. <!-- .element: class="fragment" -->
*   Informa o desenvolvedor instantaneamente no editor. <!-- .element: class="fragment" -->

---

## 🛑 Erros Comuns que Linters Pegam
*   Variáveis declaradas mas nunca usadas. <!-- .element: class="fragment" -->
*   Chamar funções que não foram definidas. <!-- .element: class="fragment" -->
*   Uso de `var` em vez de `const/let` no JS. <!-- .element: class="fragment" -->
*   Falta de ponto e vírgula (onde é obrigatório). <!-- .element: class="fragment" -->

---

## 🕵️‍♂️ ESLint: O Detetive do Código
*   O Linter mais popular do mundo JavaScript. <!-- .element: class="fragment" -->
*   Extremamente configurável. <!-- .element: class="fragment" -->
*   Possui conjuntos de regras prontos (ex: Airbnb, Google). <!-- .element: class="fragment" -->

---

## 🎨 Prettier: O Artista do Código
*   A única preocupação dele é o **estilo visual**.
*   Onde colocar o espaço? Onde quebrar a linha?
*   O Prettier é "opinativo": ele decide o melhor visual para você não perder tempo discutindo. <!-- .element: class="fragment" -->

---

## ⚖️ Linter vs Formatter
```mermaid
graph LR
    L[Linter - ESLint] --- Rules1[Qualidade/Logica]
    F[Formatter - Prettier] --- Rules2[Estilo/Aparencia]
    L --- Ex1(Variaveis nao usadas)
    F --- Ex2(Uso de Aspas Simples)
```

---

## ⚙️ Configurando o ESLint
Arquivo `.eslintrc.json`
```json
{
  "rules": {
    "no-console": "warn",
    "semi": ["error", "always"]
  }
}
```
*   **Off**: Desligado. <!-- .element: class="fragment" -->
*   **Warn**: Amarelo (Aviso). <!-- .element: class="fragment" -->
*   **Error**: Vermelho (Bloqueia o commit). <!-- .element: class="fragment" -->

---

## 💎 Configurando o Prettier
Arquivo `.prettierrc`
```json
{
  "singleQuote": true,
  "trailingComma": "all",
  "tabWidth": 2
}
```
*   Configura uma vez, aplica no projeto inteiro! <!-- .element: class="fragment" -->

---

## ⌨️ Integração com VS Code
*   Instala as extensões oficiais. <!-- .element: class="fragment" -->
*   Ativa o "Format on Save". <!-- .element: class="fragment" -->
*   **Mágica**: Você escreve o código bagunçado, aperta `Ctrl + S` e ele se organiza sozinho! <!-- .element: class="fragment" -->

---

## 🏗️ Extensões de Regras
Muitos frameworks trazem suas próprias regras de lint:
*   `eslint-plugin-react` <!-- .element: class="fragment" -->
*   `eslint-plugin-vue` <!-- .element: class="fragment" -->
*   `eslint-plugin-security` <!-- .element: class="fragment" -->

---

## 🛠️ Comando `fix`
O ESLint pode consertar os erros para você!
```bash
npx eslint . --fix
```
*   Resolve automaticamente problemas de indentação e erros simples de sintaxe. <!-- .element: class="fragment" -->

---

## 🤫 Por que não usar `console.log` em produção?
*   Exibe dados sensíveis no navegador. <!-- .element: class="fragment" -->
*   Diminui a performance do app. <!-- .element: class="fragment" -->
*   O Linter nos ajuda a lembrar de remover logs de teste. <!-- .element: class="fragment" -->

---

## 🧠 Dívida Técnica
Cada regra ignorada hoje é um problema amanhã.
*   O Linter ajuda a manter a dívida sob controle. <!-- .element: class="fragment" -->
*   Evita o "Código Espaguete". <!-- .element: class="fragment" -->

---

## 🤝 EditorConfig: O Irmão do Meio
O arquivo `.editorconfig` ajuda a manter a indentação correta mesmo em editores diferentes.
*   `indent_style = space` <!-- .element: class="fragment" -->
*   `indent_size = 2` <!-- .element: class="fragment" -->

---

## 🛡️ Linting no CI (GitHub Actions)
*   A build só passa se o Linter der "OK". <!-- .element: class="fragment" -->
*   Ninguém consegue enviar código "sujo" para a branch principal. <!-- .element: class="fragment" -->

---

## 🏆 Checklist de Qualidade Pro
*   [ ] ESLint e Prettier configurados no projeto. <!-- .element: class="fragment" -->
*   [ ] "Format on Save" ativado no VS Code. <!-- .element: class="fragment" -->
*   [ ] Entende a diferença entre aviso e erro. <!-- .element: class="fragment" -->
*   [ ] Arquivos de configuração versionados no Git. <!-- .element: class="fragment" -->

---

## 📝 Prática de Hoje
1.  Instalar o ESLint e Prettier via npm.
2.  Criar os arquivos de configuração.
3.  Bagunçar um código e deixar o editor consertar sozinho.

---

## 🏁 Dúvidas?
Código limpo é código profissional! 🚀✨
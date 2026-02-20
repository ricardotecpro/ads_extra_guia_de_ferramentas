# Projeto 10 - Limpeza Automática de Código ✨

### 🎯 Objetivo
Configurar e utilizar ferramentas de análise estática e formatação para garantir que o código siga padrões profissionais automaticamente.

### 📋 Passo a Passo

1.  **Ambiente**: Abra o VS Code em uma pasta vazia.
2.  **Arquivo Bagunçado**: Crie um arquivo `app.js` e cole o seguinte código (exatamente com essa má indentação):
    ```javascript
    function     soma(a,b){
    return a+b
    }
    const x = 10;
    console.log(soma(5,x))
    ```
3.  **Formatação Manual**: Pressione `Shift + Alt + F`. Veja o Prettier organizar os espaços e parênteses.
4.  **Automação**: Verifique se a opção "Format on Save" está ativa (Aula 10). Mude algo no código, salve e veja a mágica acontecer.
5.  **Desafio Linter**: Apague a linha `const x = 10;` mas mantenha a chamada `soma(5, x)`. Observe o VS Code sublinhar o erro em vermelho. Passe o mouse sobre o erro e leia a mensagem do Linter.

---
**Entrega**: Um print do seu VS Code com o código formatado e o erro do Linter visível.
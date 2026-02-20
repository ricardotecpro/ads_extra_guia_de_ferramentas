# Aula 13: Contêineres com Docker 📦

---

## 🎯 Nossa Missão
*   Resolver o problema "na minha máquina funciona".
*   Entender a tecnologia de contêineres.
*   Dominar Dockerfiles e Imagens.
*   Orquestração local com Docker Compose.

---

## 😫 O Conflito de Versões
*   Projeto A precisa de Node 14. { .fragment }
*   Projeto B precisa de Node 18. { .fragment }
*   Seu computador vira uma bagunça de versões conflitantes. { .fragment }
*   **O Docker isola tudo isso.** { .fragment }

---

## 🐳 O que é o Docker?
Não é uma máquina virtual!
*   **Contêiner**: Um processo isolado que compartilha o kernel do S.O. { .fragment }
*   **Imagem**: O "molde" ou fotografia do sistema pronto. { .fragment }
*   **Docker Hub**: Onde baixamos as imagens prontas. { .fragment }

---

## ⚖️ VM vs Contêiner
```mermaid
graph TD
    subgraph VM [Maquina Virtual]
        OS1[OS Hospedeiro] --- Hyp[Hypervisor]
        Hyp --- GOS[Guest OS]
        GOS --- App1[App + Libs]
    end
    subgraph CT [Conteiner]
        OS2[OS Hospedeiro] --- DE[Docker Engine]
        DE --- App2[App + Libs]
    end
```
*   Contêineres são muito mais leves e rápidos. { .fragment }

---

## 📜 O Dockerfile: A Receita
```dockerfile
# 1. Base (Qual S.O.?)
FROM node:20-alpine
# 2. Pasta de trabalho
WORKDIR /app
# 3. Copiar arquivos
COPY . .
# 4. Instalar dependencias
RUN npm install
# 5. Comando de inicio
CMD ["npm", "start"]
```

---

## 🛠️ Comandos Essenciais (Build)
*   `docker build -t meu-app .`: Criar a imagem. { .fragment }
*   `docker images`: Listar imagens no PC. { .fragment }
*   `docker rmi <id>`: Deletar imagem. { .fragment }

---

## 🚀 Comandos Essenciais (Run)
*   `docker run -p 8080:80 meu-app`: Rodar o app. { .fragment }
*   `docker ps`: Ver o que está rodando. { .fragment }
*   `docker stop <id>`: Parar o contêiner. { .fragment }
*   `docker exec -it <id> sh`: Entrar no contêiner. { .fragment }

---

## 🔗 Mapeamento de Portas
`8080:80`
*   **8080**: Porta do seu computador (Host). { .fragment }
*   **80**: Porta dentro do Docker (Container). { .fragment }
*   Permite acessar o serviço via browser no seu PC. { .fragment }

---

## 📂 Volumes: Persistência de Dados
Contêineres são efêmeros (se deletar, os dados somem).
*   **Volumes** conectam uma pasta do seu HD à pasta do Docker. { .fragment }
*   Os dados sobrevivem mesmo se o contêiner for destruído. { .fragment }

---

## 🗺️ Docker Compose: O Maestro Local
E se eu precisar de uma API + Banco de Dados?
*   Arquivo `docker-compose.yml`. { .fragment }
*   Define todos os serviços e suas redes. { .fragment }
*   Comando: `docker-compose up`. { .fragment }

---

## 🏗️ Exemplo de Docker Compose
```yaml
services:
  web:
    build: .
    ports: ["3000:3000"]
  db:
    image: postgres:alpine
    environment:
      POSTGRES_PASSWORD: root
```

---

## 🌐 Redes no Docker (Networks)
*   Contêineres podem falar uns com os outros pelo nome. { .fragment }
*   Isolamento de tráfego para maior segurança. { .fragment }

---

## 🦁 Otimizando Imagens
*   Use imagens `alpine` (ultra leves). { .fragment }
*   Evite instalar ferramentas desnecessárias na imagem. { .fragment }
*   Use `.dockerignore` para não copiar o `node_modules` local. { .fragment }

---

## 🛡️ Segurança no Docker
*   Não rode o app como usuário `root` dentro do Docker. { .fragment }
*   Mantenha suas imagens base sempre atualizadas. { .fragment }
*   Use ferramentas de scan de vulnerabilidades. { .fragment }

---

## 📉 Ciclo de Desenvolvimento Docker
```mermaid
graph LR
    C[Código] --> B[Build Image]
    B --> R[Run Container]
    R --> T[Test]
    T --> P[Push to Hub]
```

---

## 🌟 O Futuro: DevContainers
*   Use o Docker para configurar seu ambiente de VS Code. { .fragment }
*   Todo o time usa exatamente as mesmas extensões e ferramentas. { .fragment }

---

## 🏆 Checklist de Docker Pro
*   [ ] Entende a diferença entre Imagem e Contêiner. { .fragment }
*   [ ] Sabe escrever um Dockerfile básico. { .fragment }
*   [ ] Consegue rodar um banco de dados via Docker. { .fragment }
*   [ ] Entende para que serve o Docker Compose. { .fragment }

---

## 📝 Prática de Hoje
1.  Criar um Dockerfile para um site estático.
2.  Fazer o Build e conferir o tamanho da imagem.
3.  Rodar o contêiner e acessar via navegador.

---

## 🏁 Dúvidas?
Contêineres mudaram o mundo do software! 🚀📦

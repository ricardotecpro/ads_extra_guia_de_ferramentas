## 📝 **Tutorial Completo: Instalando e Configurando Neovim + LunarVim no Debian/Ubuntu**

**Inclui Node.js, Python, Rust, configuração de Bash/Zsh e desinstalação completa**

---

## ✅ **1. Atualizar o sistema**

```bash
sudo apt update && sudo apt upgrade -y
```

---

## ✅ **2. Instalar dependências básicas**

```bash
sudo apt install -y git curl wget unzip tar build-essential ripgrep fd-find python3 python3-pip python3-venv
```

---

## ⚙️ **3. Instalar o Neovim (escolha uma opção)**

### 🔹 **Opção 1: AppImage (recomendado)**

```bash
wget https://github.com/neovim/neovim/releases/latest/download/nvim.appimage
chmod u+x nvim.appimage
sudo mv nvim.appimage /usr/local/bin/nvim
```

---

### 🔹 **Opção 2: PPA (Ubuntu)**

```bash
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt update
sudo apt install -y neovim
```

---

### 🔹 **Opção 3: tar.gz (/opt/nvim)**

👍 Opção para **renomear `/opt/nvim-linux-x86_64` para `/opt/nvim`**, garantindo compatibilidade com o resto do tutorial, que já usa `/opt/nvim` como caminho principal.


```bash
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo tar -xzf nvim-linux-x86_64.tar.gz -C /opt
sudo mv /opt/nvim-linux-x86_64 /opt/nvim
```




✅ **Adicionar `/opt/nvim/bin` no PATH (`.bashrc` e `.zshrc`):**

```bash
echo 'export PATH="/opt/nvim/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="/opt/nvim/bin:$PATH"' >> ~/.zshrc
source ~/.bashrc
source ~/.zshrc
```

Verificar:

```bash
nvim --version
```

---

## ✅ **4. Instalar Node.js (com NVM)**

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
source ~/.zshrc
nvm install --lts
nvm use --lts
```

Verificar:

```bash
node -v
npm -v
```

---

## ✅ **5. Instalar Python para Neovim**

```bash
pip install --user pynvim
```


```bash
sudo apt install python3-pynvim
```

---

## ✅ **6. Instalar Rust**

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

✅ **Adicionar `$HOME/.cargo/bin` no PATH (se necessário):**

```bash
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.zshrc
source ~/.bashrc
source ~/.zshrc
```

Verificar:

```bash
rustc --version
cargo --version
```

---

## ✅ **7. Instalar LunarVim**

```bash
LV_BRANCH='release-1.4/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh)
```

✅ **Adicionar `$HOME/.local/bin` no PATH:**

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.bashrc
source ~/.zshrc
```

Verificar:

```bash
lvim --version
```

---

## ✅ **8. Instalar Nerd Fonts (opcional)**

```bash
cd ~/Downloads
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip
unzip FiraCode.zip -d ~/.fonts
fc-cache -fv
```

---

## ✅ **9. Instalar plugins extras (opcional)**

```bash
pip install --user black isort flake8
npm install -g eslint prettier typescript typescript-language-server
```

---

## 🗑️ **10. Como desinstalar tudo**

### 🔹 **Desinstalar LunarVim**

```bash
~/.local/share/lunarvim/uninstall.sh
rm -rf ~/.config/lvim ~/.local/share/lunarvim ~/.cache/lvim
```

---

### 🔹 **Desinstalar Neovim**

✅ **AppImage:**

```bash
sudo rm /usr/local/bin/nvim
```

✅ **PPA:**

```bash
sudo apt remove --purge neovim
sudo add-apt-repository --remove ppa:neovim-ppa/stable
```

✅ **tar.gz (/opt/nvim):**

```bash
sudo rm -rf /opt/nvim
```

✅ **Remover outros arquivos residuais em `/opt`:**

```bash
sudo rm -rf /opt/nvim-linux-x86_64
sudo rm -rf /opt/nvim
sudo rm -f /opt/nvim-linux-x86_64.appimage
sudo rm -f /opt/nvim-linux-x86_64.tar.gz
```

✅ **Remover arquivos no diretório home:**

```bash
rm -f ~/nvim-linux-x86_64
sudo rm -rf /opt/nvim
rm -f ~/nvim-linux-x86_64.appimage
rm -f ~/nvim-linux-x86_64.tar.gz
```

✅ **Remover arquivos no diretório Downloads:**

```bash
rm -f ~/Downloads/nvim-linux-x86_64
sudo rm -rf /opt/nvim
rm -f ~/Downloads/nvim-linux-x86_64.appimage
rm -f ~/Downloads/nvim-linux-x86_64.tar.gz
```

✅ **Remover arquivos no diretório `~/opt`:**

```bash
rm -f ~/opt/nvim-linux-x86_64
sudo rm -rf /opt/nvim
rm -f ~/opt/nvim-linux-x86_64.appimage
rm -f ~/opt/nvim-linux-x86_64.tar.gz
```

---

### 🔹 **Remover PATH do `.bashrc` e `.zshrc`:**

```bash
sed -i '/\/opt\/nvim\/bin/d' ~/.bashrc
sed -i '/\/opt\/nvim\/bin/d' ~/.zshrc
sed -i '/\$HOME\/\.cargo\/bin/d' ~/.bashrc
sed -i '/\$HOME\/\.cargo\/bin/d' ~/.zshrc
sed -i '/\$HOME\/\.local\/bin/d' ~/.bashrc
sed -i '/\$HOME\/\.local\/bin/d' ~/.zshrc
source ~/.bashrc
source ~/.zshrc
```

---

## ✅ **11. Testar se foi removido**

```bash
which nvim
which lvim
```

✅ Se não retornar nada, tudo foi removido com sucesso.

---

## 🎉 **Tutorial revisado, compatível e completo!**

O comando `sudo mv /opt/nvim-linux-x86_64 /opt/nvim` já garante que o PATH `/opt/nvim/bin` funciona corretamente sem alterações extras. Precisa incluir mais alguma configuração automática ou ajuste?




Claro! Aqui está a **versão atualizada do tutorial de instalação do Neovim no Debian/Ubuntu**, considerando o uso do arquivo `.tar.gz`, com:

- Download e extração
    
- Renomeação para `/opt/nvim`
    
- Configuração do PATH para Bash e Zsh
    
- Verificação
    
- Comandos de desinstalação
    

---

## 🧹 Desinstalação (caso necessário)

```bash
sudo rm -rf /opt/nvim
sudo rm -f /opt/nvim-linux-x86_64.tar.gz
sudo rm -f /opt/nvim-linux-x86_64
sudo rm -f /opt/nvim-linux-x86_64.appimage
rm -f ~/nvim-linux-x86_64*
rm -f ~/Downloads/nvim-linux-x86_64*
rm -f ~/opt/nvim-linux-x86_64*
```

Limpar o PATH do `.bashrc` e `.zshrc`:

```bash
sed -i '/\/opt\/nvim\/bin/d' ~/.bashrc
sed -i '/\/opt\/nvim\/bin/d' ~/.zshrc
source ~/.bashrc
source ~/.zshrc
```

---

Se quiser, posso também transformar esse tutorial em um script `.sh` executável. Deseja isso?


Ótima observação! Esse erro acontece porque **Debian/Ubuntu mais recentes** (como Debian 12, Ubuntu 22.04+) bloqueiam o `pip` para instalar pacotes **no sistema global** (para proteger o sistema).

Mas temos **soluções simples**! Vou explicar e sugerir a melhor:

---

## ✅ **🎯 Opção 1 (recomendada): usar o `--break-system-packages`**

Se você **não se importa em instalar globalmente**:

```bash
pip install --user --break-system-packages pynvim
```

✅ Isso resolve **imediatamente** sem mexer no sistema.

---

## ✅ **🎯 Opção 2: criar um ambiente virtual (recomendado se quiser isolar)**

Mais seguro, evita conflitos com o sistema:

```bash
python3 -m venv ~/.venvs/lunarvim
source ~/.venvs/lunarvim/bin/activate
pip install pynvim
```

Depois adicione o Python do venv ao `PATH` ou configure no LunarVim se necessário.

---

## ✅ **🎯 Opção 3: instalar via apt (versão empacotada)**

```bash
sudo apt install python3-pynvim
```

⚠️ Atenção: pode estar **desatualizado** no repositório da distro.

---

👉 **Minha recomendação rápida**: use **opção 1 (`--break-system-packages`)**, funciona direto e sem necessidade de venv se for uso pessoal.



---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)

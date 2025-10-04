# 🚀 YouDri - YouTube to Google Drive Automator

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube)
![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)

## 📖 Sobre o Projeto

YouDri é uma aplicação de console (CLI) robusta desenvolvida em Python que automatiza o processo de baixar um vídeo de uma URL do YouTube e enviá-lo diretamente para a sua conta do Google Drive.

O projeto foi construído do zero com foco em boas práticas de arquitetura de software, incluindo uma estrutura orientada a objetos com separação de responsabilidades, uma experiência de usuário interativa e um tratamento de erros robusto.

## ✨ Funcionalidades

* **Interface Interativa:** Um menu simples e claro no terminal guia o usuário durante todo o processo.
* **Confirmação de Título:** Antes de iniciar o download, o script busca e exibe o título do vídeo para confirmação, prevenindo o download de vídeos incorretos.
* **Fluxo Contínuo:** Permite baixar e enviar múltiplos vídeos em sequência sem a necessidade de reiniciar a aplicação.
* **Autenticação Segura:** Utiliza o fluxo OAuth2 padrão do Google para garantir um acesso seguro à conta do Drive, criando um token de autorização para sessões futuras.
* **Limpeza Automática:** Após um upload bem-sucedido, o arquivo de vídeo local é removido automaticamente para economizar espaço em disco.

## 🛠️ Stack de Tecnologias

* **Linguagem:** Python 3.7+
* **Ambiente:** venv
* **Download de Vídeo:** yt-dlp
* **API do Google:** google-api-python-client
* **Autenticação OAuth2:** google-auth-oauthlib

## 🚀 Como Começar

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

Você precisará ter o seguinte software instalado em sua máquina:
* Python - Versão 3.7 ou superior.
* pip (gerenciador de pacotes do Python).

### Configuração

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/MatheusFrazatto/YouDri---Youtube_To_Drive.git](https://github.com/MatheusFrazatto/YouDri---Youtube_To_Drive.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```sh
    cd YouDri---Youtube_To_Drive
    ```
3.  **Crie e ative um ambiente virtual:**
    * **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
4.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Configure a API do Google Drive:**
    * Acesse o [Google Cloud Console](https://console.cloud.google.com/) e crie um novo projeto.
    * Procure e ative a **"Google Drive API"**.
    * Vá para **"Credenciais"** > **"+ CRIAR CREDENCIAIS"** > **"ID do cliente OAuth"**.
    * Configure a **"Tela de permissão OAuth"** como **"Externo"** e preencha as informações básicas.
    * Selecione o tipo de aplicativo como **"Aplicativo para computador"**.
    * Faça o download do arquivo JSON. **Renomeie-o para `credentials.json`** e coloque-o na pasta raiz do projeto.
    * Na "Tela de permissão OAuth", vá para **"Testadores"** e adicione seu próprio e-mail como um usuário de teste.

### Executando a Aplicação

1.  Com o ambiente virtual ativado, execute o script principal:
    ```sh
    python Main.py
    ```
2.  Siga as instruções do menu interativo no terminal.

#### Primeiro Uso
Na primeira vez que você executar, uma aba do seu navegador será aberta para que você autorize o acesso à sua Conta Google. Siga os passos de autenticação para permitir que a aplicação funcione. Um arquivo `token.json` será criado para salvar sua autorização.

## 📜 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

# YouDri - YouTube para Google Drive

Script de automação em Python que baixa um vídeo de uma URL do YouTube, faz o upload diretamente para a conta do Google Drive do usuário e, em seguida, apaga o arquivo local para economizar espaço em disco.

Este projeto foi desenvolvido como uma solução para o processo seltivo da Tapps Games.

---

## Funcionalidades Principais

* **Interface de Menu Interativa:** Um menu simples no terminal guia o usuário através das opções.
* **Confirmação de Título:** Antes de iniciar o download, o script busca o título do vídeo e pede a confirmação do usuário para evitar erros de URL.
* **Loop de Execução Contínuo:** Permite baixar e enviar múltiplos vídeos em sequência sem precisar reiniciar o programa.
* **Autenticação Segura:** Utiliza o fluxo OAuth2 padrão do Google para garantir um acesso seguro à conta do Drive, criando um token de autorização para sessões futuras.
* **Limpeza Automática:** O arquivo de vídeo local é removido automaticamente após o upload bem-sucedido, mantendo o diretório do projeto limpo.

---

## 🛠️ Configuração e Instalação

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

* Python 3.13.5.
* OBS: O script foi desenvolvido utilizando o ambiente venv do Python.

### 1. Instalar as Dependências

Este projeto utiliza as bibliotecas listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

### 2. Configurar a API do Google Drive

Para que o aplicativo possa acessar sua conta do Google Drive, você precisa de credenciais da API.

1.  **Acesse o Google Cloud Console** e crie um novo projeto.
2.  Procure e ative a **"Google Drive API"**.
3.  Vá para a seção **"Credenciais"**, clique em **"+ CRIAR CREDENCIAIS"** e selecione **"ID do cliente OAuth"**.
4.  Configure a **"Tela de permissão OAuth"**:
    * Tipo de usuário: **Externo**.
    * Preencha as informações básicas (nome do app, e-mail de suporte).
5.  Na criação da credencial, selecione o tipo de aplicativo **"Aplicativo para computador"**.
6.  Faça o download do arquivo JSON de credenciais. **Renomeie o arquivo para `credentials.json`** e coloque-o na pasta raiz do projeto.
7.  Na "Tela de permissão OAuth", vá para a seção **"Testadores"** e adicione o seu endereço de e-mail como um usuário de teste autorizado.

---

## Como Executar

Siga as instruções do menu interativo no terminal.

### Primeiro Uso

Na primeira vez que você executar o script, uma aba do seu navegador será aberta para que você autorize o acesso à sua Conta Google.
1.  Faça login na conta que você adicionou como testador.
2.  Você verá um aviso de "App não verificado". Clique em **"Avançado"** e depois em **"Ir para [Nome do seu app] (não seguro)"**.
3.  Clique em **"Permitir"**.
4.  Após a autorização, um arquivo `token.json` será criado na pasta do projeto, e o script continuará o processo. Você não precisará fazer isso novamente nas próximas execuções.

---

## Tecnologias Utilizadas

* **Python**
* **yt-dlp:** Para um download robusto e confiável de vídeos do YouTube.
* **Google API Python Client:** Para interação com a API do Google Drive (autenticação e upload).

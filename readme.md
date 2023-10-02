
# Integração Python com Active Directory e Telegram Bot

Este é um projeto Python que demonstra como conectar-se a um servidor Active Directory e enviar solicitações para ele usando um bot do Telegram.

## Pré-requisitos

Antes de usar este código, certifique-se de que você tenha:

- Python instalado em sua máquina (versão 3.x recomendada).
- As bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte comando:

  ```bash
  pip install python-ldap python-telegram-bot
Um bot Telegram criado e o token de acesso do bot. Você pode criar um bot seguindo as instruções aqui.
Configuração
Clone este repositório para sua máquina:

bash
Copy code
git clone https://github.com/xavierg814/bot_liberacao_AD
Navegue até o diretório do projeto:

bash
Copy code
cd bot_liberacao_AD
Abra o arquivo conection.py e preencha as seguintes informações:

AD_SERVER: O endereço do servidor Active Directory.
AD_USERNAME: O nome de usuário para autenticação no Active Directory.
AD_PASSWORD: A senha correspondente ao nome de usuário.
TELEGRAM_BOT_TOKEN: O token de acesso do seu bot Telegram.
Uso
Execute o script Python main.py para conectar-se ao servidor Active Directory e enviar solicitações para ele via bot Telegram.

bash
Copy code
python main.py
O bot estará pronto para aceitar comandos Telegram para interagir com o Active Directory.

Comandos do Bot Telegram
/buscar_usuario <username>: Busca informações de um usuário no Active Directory com base no nome de usuário.
/listar_usuarios: Lista todos os usuários do Active Directory.
/buscar_grupo <groupname>: Busca informações sobre um grupo no Active Directory com base no nome do grupo.
/listar_grupos: Lista todos os grupos do Active Directory.
Contribuição
Sinta-se à vontade para contribuir para este projeto abrindo problemas (issues) ou enviando pull requests. Toda contribuição é bem-vinda!

Licença
Este projeto está sob a licença MIT.

css
Copy code

Lembre-se de substituir `<username>` e `<groupname>` pelos nomes de usuário e grupos reais que você deseja buscar no Active Directory. Certifique-se também de personalizar a seção de contribuição e a licença conforme necessário para seu projeto.
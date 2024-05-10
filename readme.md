# Chatbot de Vendas com IA

## Descrição
Este projeto é um chatbot de vendas desenvolvido para funcionar como um intermediário entre o usuário e um sistema de IA generativa, o Google Gemini. Ele facilita a consulta de informações de produtos e serviços, executando comandos SQL no banco de dados SQLite com base nas interações do usuário, e utiliza a IA para montar as instruções SQL e montar as respostas em linguagem.

Disclaimer: Este é um MVP criado para apresentar o conceito em tempo record. Então a arquitetura está super simplificada. Em um contexo de produção muitas melhorias serão necessárias. Serão bem vindas pull requests com com sugestões de melhorias para avançar a solução.
## Funcionalidades
- Interação em linha de comando com diferenciação de cores para mensagens do usuário (branco) e do bot (ciano).
- Execução de consultas SQL dinâmicas baseadas nas interações do usuário.
- Comunicação com a API de IA generativa para processamento de linguagem natural.

## Pré-requisitos
Para executar este projeto, você precisará de:
- Python 3.8 ou superior
- Bibliotecas Python: `sqlite3`, `json`, `re`, `colorama`, `requests`
- Banco de dados SQLite
- API Key do Gemini Pro

## Instalação
Siga estas instruções para configurar o ambiente necessário para executar o chatbot.

### Clonando o Repositório


### Instalando Dependências


### API Key

Windows:
set GOOGLE_API_KEY=sua_chave_api_aqui

MacOs ou Linux:
export GOOGLE_API_KEY=sua_chave_api_aqui


### Executando
Na primeira execução tire o comentário da linha 9 (#self.create_and_populate_db()) no fonte banco.py para que o banco seja populado com os dados de testes.
Antes da segunda execução volte a comentar essa linha.

execute o arquivo app.py
python app.py



## Exemplos de Uso
Interaja com o chatbot através da linha de comando:
- Cliente: "Qual o preço do arroz?"
- bot: "O preço do arroz branco é R$ 19,00 por pacote."

Vá conversando solicitando informações sobre produtos ao bot até finalizar o pedido.

você pode refinar o prompt no aquivo gemini.py função novo_chat()

## Contribuições
Contribuições são bem-vindas! Se você tem melhorias ou correções, por favor, faça um fork do repositório, faça suas alterações, e envie um pull request.

## Licença
Este projeto é distribuído sob a licença GNU.

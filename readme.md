# Chatbot de Vendas com IA

## Descrição
Este projeto é um chatbot de vendas desenvolvido para funcionar como um intermediário entre o usuário e um sistema de IA generativa, o Google Gemini.
O Objetivo dele é interagir com o cliente, passando informações sobre produtos e preços até o fechamento da venda e inserção do pedido no banco.
- Ele intercepta todas a mensagens do usuário e encaminha pra IA. 
- A IA conhece a estrutura do banco, mas somente o bot pode executar
- Quando a pergunta do usuário requer operação com o banco, a IA monta o SQL e devolve para o bot entre tags <sql>. 
- O Bot por sua vez executa no banco e devolve o resultado para a IA. 
- Com esses dados, a IA monta a resposta em liguagem natual e devolve para o bot entre tags <msg>. 
- Prontamente o bot extrai o texto e entrega pro cliente.

![Arquitetura](img/diagrama.png?raw=true "Arquitetura")

Porque um Bot entre o usuário e a IA?
- A IA (nesse contexto) não possui acesso ao banco (e nem sei se deveria ter)
- O Bot é um script python binário que não tem condições de montar SQL e mensagens amigáveis facilmente
- Juntano os dois temos:
    - Um contexto amigável para o cliente
    - Seguro para a base de dados
    - Mais asserivo pois é possível evitar alucinações via prompt
    - Dentre outros

Disclaimer: Este é um MVP criado para apresentar o conceito. Então a arquitetura está super simplificada. Em um contexo de produção muitas melhorias seriam necessárias. Serão bem vindas sugestões de melhorias para avançar a solução.

## Funcionalidades
- Interação em linha de comando com diferenciação de cores para mensagens do usuário (branco) e do bot (ciano).
- Execução de consultas SQL dinâmicas baseadas nas interações do usuário.
- Comunicação com a API de IA generativa para processamento de linguagem natural.

## Pré-requisitos
Para executar este projeto, você precisará de:
- Python 3.12 ou superior (não foi testado em versões anteriores nem posteriores)
- Banco de dados SQLite
- API Key do Gemini Pro

## Instalação
Siga estas instruções para configurar o ambiente necessário para executar o chatbot.

### Clonando o Repositório

`git clone https://github.com/fabiojrbraga/sales_assistant_gemini.git`

### Instalando Dependências

`pip install -r requirements.txt`


### API Key

Windows:
`set GOOGLE_API_KEY=sua_chave_api_aqui`

MacOs ou Linux:
`export GOOGLE_API_KEY=sua_chave_api_aqui`


### Executando

execute o arquivo app.py
`python app.py`



## Exemplos de Uso
Interaja com o chatbot através da linha de comando:
- Cliente: "Qual o preço do arroz?"
- bot: "O preço do arroz branco é R$ 19,00 por pacote."

Vá conversando solicitando informações sobre produtos ao bot até finalizar o pedido.

você refinar o prompt no aquivo gemini.py função novo_chat()

#### Segue um print dele em ação
![Alt text](img/print_chat.PNG?raw=true "Print do bot em ação")


## Contribuições
Contribuições são bem-vindas! Se você tem melhorias ou correções, por favor, faça um fork do repositório, faça suas alterações, e envie um pull request.


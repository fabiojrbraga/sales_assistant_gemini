import gemini

from colorama import Fore, Style
from banco import Banco
import logging
from logging.handlers import RotatingFileHandler

import re

log = logging.getLogger()
log.setLevel(logging.INFO)


handler = RotatingFileHandler(
    'logging.log',          # Nome do arquivo de log
    maxBytes=2*1024*1024,   # Tamanho máximo do arquivo em bytes antes de ser rotacionado (5 MB)
    backupCount=3,           # Número máximo de arquivos de backup a manter
    encoding='utf-8'
)

formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)

# Adiciona o handler ao logger
log.addHandler(handler)


class Bot():

    def __init__(self) -> None:
        log.info("Iniciando o Bot")
        self.chat = gemini.novo_chat()
        self.banco = Banco()

    def end_chat(self):
        self.banco.close_connection()

    def send_to_ia(self, msg):
        log.info(f"Bot to IA:\n {msg}")
        response = gemini.process_input(msg=msg, chat = self.chat)
        self.process_ia_response(response)

    def send_to_user(self, msg):
        log.info(f"Bot to User:\n {msg}")
        print("Bot: "+Fore.CYAN + msg + Style.RESET_ALL)


    def process_ia_response(self, ia_response):
        msg = ""
        for chunk in ia_response:
            msg += chunk.text

        log.info(f"IA to Bot: \n{msg}")
        if ("<sql>" in msg.lower()):
            json_data =  self.handle_database_query(msg)
            response = self.send_to_ia(str(json_data))
        elif("<msg>" in msg.lower()):
            self.send_to_user(self.handle_ia_msg(msg))
        else:
            response = self.send_to_ia("Sua resposta não contém as tags necessárias. Corrija por favor")
            self.process_ia_response(response)

    def handle_database_query(self, msg):        
        sql_code_search = re.search(r"<sql>(.*?)</sql>", msg, re.IGNORECASE)
        if sql_code_search:
            sql_code = sql_code_search.group(1).strip()  # Extrai o código SQL
            return self.banco.execute_query(sql_code)
        return "Erro: SQL não encontrado."
        

    def handle_ia_msg(self, msg) -> str:
        msg_search = re.search(r"<msg>(.*?)</msg>", msg, re.IGNORECASE | re.DOTALL)
        if msg_search:
            return msg_search.group(1).strip()  # Extrai a mensagem
        return "Erro: Mensagem não encontrada."
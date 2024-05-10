from colorama import Fore, Style
from bot import Bot
bot = Bot()
while True:
  msg = input("\n"+Fore.GREEN+"Cliente: "+ Style.RESET_ALL)
  if "sair" in msg.lower():
    bot.end_chat()
    break  
  bot.send_to_ia(msg)
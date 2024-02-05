from pyrogram import Client, idle
from MultiAzBot import *
import pyfiglet, os
from colorama import init, Fore, Style
from aiohttp import ClientSession

aiohttpsession = ClientSession()


if __name__ == "__main__":
    app.start()
    uname = app.get_me().username  
    ascii_banner = pyfiglet.figlet_format(uname)
    colored_banner = f"{Fore.YELLOW}{ascii_banner}{Style.RESET_ALL}"
    os.system('clear')
    print(colored_banner)
    print(f"{Fore.CYAN}\n xGuliyev tərəfindən yazılıb. Dəyişdirmək istəsəz bütün söyüşləri ağlınızdan keçirin :)")
    print(f"                 @{uname} Başladı!")
    idle()
    app.stop()
    os.system('clear')
    print(colored_banner)         
    print(f"{Fore.CYAN}\n xGuliyev tərəfindən yazılıb. Dəyişdirmək istəsəz bütün söyüşləri ağlınızdan keçirin :)") 
    print(f"                 @{uname} Dayandırıldı!{Style.RESET_ALL}")